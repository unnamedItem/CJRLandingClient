<template>
    <div>
        <div class="container">
            <div id="carouselExampleCaptions" class="carousel slide">
            <div class="carousel-indicators">
                <button v-for="(item, index) in eventsList.length" :key="index" :class="{'active':index==0}" type="button" data-bs-target="#carouselExampleCaptions" :data-bs-slide-to="`${index}`" :aria-label="`Slide ${index}`"></button>
            </div>
            <div class="carousel-inner">
                <div class="carousel-inner">
                    <div 
                      v-for="(item, index) in eventsList" 
                      :key="index" 
                      class="carousel-item" 
                      :class="{'active': index === 0}">                  
                      <img :src="`/src/assets/img/${item.image[0]}`" class="d-block w-100" :alt="item.altText">                  
                      <div class="carousel-caption">
                        <h5>{{ item.title }}</h5>
                        <h5 v-if="item.description">{{ item.description }}</h5>
                        <h5><a class="nav-link" v-if="item.detail" :href="`/event/${item.id}`">+ info</a></h5>
                      </div>
                    </div>
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Anterior</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Siguiente</span>
            </button>
            </div>
        </div>
    </div>
</template>

<script>
import eventsData from '../assets/data/events.json';

export default {
 
  data() {
    return {
      eventsList: []
    }
  },
  components: {
  },
  created() {
    this.loadEvents();
  },
  methods: {
    loadEvents() {
      this.eventsList = eventsData.events.filter(event => event.active);
    }
  }
}
</script>

<style scoped>
img {
  height: 70vh;
  max-width: 100%;
  object-fit: contain;
}

.carousel-item-body {
  height: 70vh;
}

.carousel-caption {
  background-color: rgba(0, 0, 0, 0.7);
  border-radius: 20px;
  padding: 1%;
  font-size: small;
}

.carousel-control-prev-icon, .carousel-control-next-icon {
  background-color: rgba(0, 0, 0, 0.7);
  border-radius: 10px;
}

h1, h2, h3, h4 {
  text-shadow: 0 0 20px rgba(0, 0, 0, 0.4);
}

h1, h2, h3, h4 {
  color: azure
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