<template>
    <div class="container">
        <div class="card">
            <div class="row">
                <div class="col-md-3">
                    <div class="card-image-container">
                        <img v-if="memberData.image" :src="memberData.image" alt="Card Image" class="card-image" width="250px"/>
                        <img v-else src="../assets/icons/avatar.svg" alt="Card Image" class="card-image" width="250px"/>
                    </div>
                </div>
                <div class="col-md-9">
                    <div class="card-body">
                        <h1 class="card-title">{{ memberData.firstname }} {{ memberData.lastname }}</h1>
                        <p class="card-text">DNI: {{ formatId(memberData.id) }}</p>
                        <p class="card-text">Abonado: {{ memberData.subscriber ? 'Si' : 'No' }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, defineProps, ref } from 'vue';
import _members from '../assets/data/members.json'
import router from '@/router';

const members = ref([]);
const memberData = ref({});
const memberExists = ref(null);

const props = defineProps({
    id: String
})

onMounted(() => {
    members.value = _members;

    memberExists.value = members.value.some((member) => {
        if (member.id == props.id) {
            memberData.value = member;
            return true;
        }
    })

    if (!memberExists.value) {
        router.push({ name: 'members' });
    }
})

function formatId(id) {
    // Validamos que el string no sea nulo
    if (!id) {
        return '';
    }
    // Validamos que el string tenga 8 caracteres y sean todos dígitos
    if (String(id).length !== 8 || !/^\d+$/.test(String(id))) {
        throw new Error("El string debe tener exactamente 8 dígitos numéricos.");
    }
    // Formateamos con puntos
    return String(id).replace(/(\d{2})(\d{3})(\d{3})/, "$1.$2.$3");
}
</script>