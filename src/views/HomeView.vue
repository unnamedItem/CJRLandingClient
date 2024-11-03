<script setup>
import EventCarousel from '../components/EventCarousel.vue';
</script>

<template>
  <div class="home">
    <!-- Encabezado -->
    <header id="inicio" class="jumbotron jumbotron-fluid text-center bg">
      <div class="container">
        <div class="row d-flex align-items-center">
          <div class="col">
            <h1 class="display-4">
              <span> Club de Juegos Rosario </span>
            </h1>
            <p class="lead">Un lugar donde disfrutar de los mejores juegos de mesa modernos.</p>
            <a class="btn btn-primary btn-lg" href="/collection" role="button">Explora nuestros juegos</a>
          </div>
        </div>
      </div>
    </header>

    <!-- Eventos -->
    <section id="events" class="py-4 bg">
      <EventCarousel />
    </section>

    <!-- Sección Sobre Nosotros -->
    <section id="about">
      <div class="container">
        <h2 class="text-center mb-3">Sobre nosotros</h2>
        <p class="about">¡Bienvenido al Club de Juegos Rosario! Si eres un apasionado de los juegos de mesa modernos, este es tu lugar. Tenemos dos espacios para reunirnos: La Fortaleza Pichincha (Salta 2845) e Invictvs (San Lorenzo 1167). Nuestras reuniones incluyen el martes de Catan, todos los martes a partir de las 18:30 hasta las 21:00 en Invictvs, disfrutar de la ludoteca de Invictvs todos los miercoles a partir de las 17:00 hasta las 21:00, y jugar con nuestra ludoteca en La Fortaleza todos los viernes y sábados a partir de las 21:00 hasta las 03:00. ¡Únete a nosotros y forma parte de la comunidad de jugadores más entusiasta de Rosario!</p>
      </div>
    </section>

    <!-- Sección Contacto -->
    <section id="contact" class="py-4 bg">
      <div class="container">
        <h2 class="text-center mb-4">Redes Sociales</h2>
        <div class="row justify-content-center">
          <a href="https://chat.whatsapp.com/J7888YH88f2IKlqye0q9XX" target="_blank" class="col d-flex justify-content-center" style="color: gray;">
            <i class="bi bi-whatsapp" style="font-size: 4rem;"></i>
          </a>
          <a href="https://www.instagram.com/clubdejuegos_rosario/" target="_blank" class="col d-flex justify-content-center" style="color: gray;">
            <i class="bi bi-instagram" style="font-size: 4rem;"></i>
          </a>
          <a href="https://www.facebook.com/ClubdeJuegosRosario" target="_blank" class="col d-flex justify-content-center" style="color: gray;">
            <i class="bi bi-facebook" style="font-size: 4rem;"></i>
          </a>
          <a href="https://twitter.com/ClubDeJuegosRos" target="_blank" class="col d-flex justify-content-center" style="color: gray;">
            <i class="bi bi-twitter-x" style="font-size: 4rem;"></i>
          </a>
          <a href="https://www.youtube.com/@clubdejuegosrosario2391" target="_blank" class="col d-flex justify-content-center" style="color: gray;">
            <i class="bi bi-youtube" style="font-size: 4rem;"></i>
          </a>
        </div>
      </div>
    </section>
  </div>
</template>


<style scoped>
img {
  height: 70vh;
  max-width: 100%;
  object-fit: contain;
}

.card {
  display: flex;
  justify-content: center;
  align-items: center;
}

.home {
  height: 80vh;
}

.btn {
  box-shadow: 0 0 100px rgba(0, 0, 0, 0.6);
}

i {
  text-shadow: 0 0 20px rgba(0, 0, 0, 0.6);
  cursor: pointer;
}

i:hover {
  text-shadow: 0 0 20px rgba(0, 0, 0, 0.8);
  color: var(--bs-primary-1);
}

h1, h2, h3, h4 {
  text-shadow: 0 0 20px rgba(0, 0, 0, 0.4);
}

h1, h2, h3, h4 {
  color: azure
}

.main-logo {
  height: 20vh;
  width: 20vh;
}

.about {
  text-align: justify;
}

.container {
  background-color: rgb(0, 0, 0, 0.7);
  box-shadow: 0 0 100px rgba(0, 0, 0, 0.9);
  color: azure;
  padding-left: 30px;
  padding-right: 30px;
  padding-top: 30px;
  padding-bottom: 30px;
  border-radius: 30px;
}
</style>