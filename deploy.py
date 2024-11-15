import ftplib, os, argparse, subprocess

# Argumentos
parser = argparse.ArgumentParser()
parser.add_argument("--dist_folder", type=str, default='dist')
parser.add_argument("--ftp_host", type=str)
parser.add_argument("--ftp_user", type=str)
parser.add_argument("--ftp_pass", type=str)
args = parser.parse_args()

# Vars
dist_folder: str = args.dist_folder

# Datos del servidor FTP
ftp_host: str = args.ftp_host    # Dirección del servidor FTP
ftp_user: str = args.ftp_user    # Nombre de usuario
ftp_pass: str = args.ftp_pass    # Contraseña

# Compilar Vue App
subprocess.call(['npm', 'install'], shell=True)
subprocess.call(['npm', 'run', 'build'], shell=True)

# Conexión al servidor FTP
ftp = ftplib.FTP(ftp_host)
ftp.login(ftp_user, ftp_pass)

def clean_remote_dir(dir):
    ftp.cwd(dir)
    files = [file for file in ftp.nlst() if file != '.' and file != '..']
    for file in files:
        print('Borrando ' + file)
        ftp.delete(file)
    ftp.cwd('..')

if __name__ == '__main__':
    ftp.cwd('/cjr.org.ar')

    # Copiar los archivos de la carpeta static
    clean_remote_dir('static')
    ftp.cwd('static')
    for file in os.listdir(dist_folder + '/static'):
        if file not in ftp.nlst(): # Si el archivo no existe
            with open(dist_folder + '/static/' + file, 'rb') as f:
                print('Copiando ' + file)
                ftp.storbinary('STOR ' + file, f)
    ftp.cwd('..')

    # Copiar archivos de la carpeta dist
    for file in [f for f in os.listdir(dist_folder) if os.path.isfile(os.path.join(dist_folder, f))]:
        if file in ftp.nlst(): # Si el archivo ya existe
            print('Borrando ' + file)
            ftp.delete(file)
        with open(dist_folder + '/' + file, 'rb') as f:
            print('Copiando ' + file)
            ftp.storbinary('STOR ' + file, f)

    # Cerrar la conexión
    ftp.quit()

    print("Deploy realizado con éxito!")
