<template>
    <div class="container">
        <div class="row d-flex align-items-center">
          <div class="col">
            <h1 class="display-4">
              <span> {{event.title}} </span>
            </h1>
            <h1> {{ event.description}}</h1>
            <p class="about" v-html="event.detail"></p>
            <img :src="`/src/assets/img/${event.image}`" class="d-block w-100">
            <p class="lead"></p>
          </div>
        </div>
      </div>
</template>

<script setup>
    import {useRoute} from 'vue-router';
    import eventsData from '../assets/data/events.json';

    var event = {title:"", description:"", image:"", detail:""};

    const eventId = useRoute().params.id;
    const data = eventsData.events.find(e => e.id === parseInt(eventId,10));
    if(data){
        event.title = data.title;
        event.description = data.description;
        event.image = data.image;
        event.detail = data.detail;
    }
</script>

<style scoped>
.container {
    text-align: center;
    background-color: rgb(0, 0, 0, 0.7);
    box-shadow: 0 0 100px rgba(0, 0, 0, 0.9);
    color: azure;
    padding-left: 30px;
    padding-right: 30px;
    padding-top: 30px;
    padding-bottom: 30px;
    border-radius: 30px;
  }

  .about {
    text-align: justify;
  }

  img {
    height: 70vh;
    max-width: 100%;
    object-fit: contain;
    margin: 16px;
  }
</style>