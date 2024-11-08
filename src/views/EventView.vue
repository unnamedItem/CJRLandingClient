<template>
    <div class="container">
        <div class="row d-flex align-items-center">
          <div class="col">
            <h1 class="display-4">
              <span> {{event.title}} </span>
            </h1>
            <h1> {{ event.description}}</h1>
            <p class="detail" v-html="event.detail"></p>

            <div id="carouselExampleCaptions" class="carousel slide">
            <div v-if="event.image.length > 1" class="carousel-indicators">
                <button v-for="(item, index) in event.image.length" :key="index" :class="{'active':index==0}" type="button" data-bs-target="#carouselExampleCaptions" :data-bs-slide-to="`${index}`" :aria-label="`Slide ${index}`"></button>
            </div>
            <div class="carousel-inner">
                <div class="carousel-inner">
                    <div 
                        v-for="(item, index) in event.image" 
                        :key="index" 
                        class="carousel-item" 
                        :class="{'active': index === 0}">                  
                        <img :src="`/src/assets/img/${event.image[index]}`" class="d-block w-100">                  
                        <div class="carousel-caption">
                        <h5>{{ item.title }}</h5>
                        </div>
                    </div>
                </div>
            </div>
            <button v-if="event.image.length > 1" class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Anterior</span>
            </button>
            <button v-if="event.image.length > 1" class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Siguiente</span>
            </button>
            </div>

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

  .detail {
    text-align: justify;
  }

  img {
    height: 70vh;
    max-width: 100%;
    object-fit: contain;
    margin: 16px;
  }
</style>