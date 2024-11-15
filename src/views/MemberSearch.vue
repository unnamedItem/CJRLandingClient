<template>
    <div class="container">
        <div class="text-center card text-white mb-3">
            <div class="card-body">
                <h1 class="card-title">Miembros</h1>
                <input v-model="querySearch" class="form-control" type="text" placeholder="Buscar...">
            </div>
        </div>

        <div class="card text-white mb-3">
            <div class="card-body">
                <table class="table table-dark table-striped">
                    <tr>
                        <th>DNI</th>
                        <th>Nombre</th>
                        <th>Apellido</th>
                        <th>Abonado</th>
                        <th>Credencial</th>
                    </tr>
                    <tr v-for="member in filteredMembers" :key="member.id">
                        <td>{{ formatId(member.id) }}</td>
                        <td>{{ member.firstname }}</td>
                        <td>{{ member.lastname }}</td>
                        <td>{{ member.subscriber ? 'Si' : 'No' }}</td>
                        <td><a :href="`/members/${member.id}`" target="_blank">Ver</a></td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue';
import _members from '../assets/data/members.json'

const members = ref([]);
const querySearch = ref('');

onMounted(() => {
    members.value = _members
})

function formatId(id) {
    // Validamos que el string tenga 8 caracteres y sean todos dígitos
    if (String(id).length !== 8 || !/^\d+$/.test(String(id))) {
        throw new Error("El string debe tener exactamente 8 dígitos numéricos.");
    }
    // Formateamos con puntos
    return String(id).replace(/(\d{2})(\d{3})(\d{3})/, "$1.$2.$3");
}

// Filtrar los miembros por sus campos
const filteredMembers = computed(() => {
    if (!querySearch.value) return members.value
    return members.value.filter(member => {
        return String(member.id).toLowerCase().includes(querySearch.value.toLowerCase()) ||
            member.firstname.toLowerCase().includes(querySearch.value.toLowerCase()) ||
            member.lastname.toLowerCase().includes(querySearch.value.toLowerCase());
    });
});
</script>