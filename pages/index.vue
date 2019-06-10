<template>
  <div class="col">
    <h1>J.K. Rowling Bot</h1>
    <p>Have you ever wondered what happens when you run all of J.K. Rowling's 'Harry Potter' plot related tweets through a neural network and ask it to create some more? Well I did, and this is the result!</p>
    <p>
      <nuxt-link to="/about">
        More Info
      </nuxt-link>
    </p>
    <tweet :current-acc="currentAcc" />
    <div class="accuracy-range">
      <input id="current-accuracy" v-model="currentAcc" type="range" min="10" max="90" step="10">
      <label for="current-accuracy" :class="labelClass">Accuracy: {{ currentAcc }}%</label>
    </div>
  </div>
</template>

<script>
import Tweet from '~/components/Tweet.vue'

export default {
  components: {
    Tweet
  },

  data: () => ({
    currentAcc: '50'
  }),

  computed: {
    labelClass: function() {
      return 'current-accuracy-' + this.currentAcc
    }
  }
}
</script>

<style lang="scss" scoped>
.page-enter-active {
  animation: transitionEnter .5s;
}

.page-leave-active {
  animation: transitionLeave .5s;
}

@keyframes transitionEnter {
  0% {
    transform: translateY(-100vh);
  }

  100% {
    transform: translateY(0);
  }
}

@keyframes transitionLeave {
  0% {
    transform: translateY(0);
  }

  100% {
    transform: translateY(-100vh);
  }
}

.accuracy-range {
  $range-track-height: 10px;
  $range-track-border-radius: 25px;
  $range-track-bg: #fff;

  position: relative;

  input[type=range] {
    appearance: none;
    margin: 4.8px 0;
    width: 100%;

    &::-webkit-slider-runnable-track {
      background: $range-track-bg;
      border: 0;
      border-radius: $range-track-border-radius;
      cursor: pointer;
      height: $range-track-height;
      width: 100%;
    }

    &::-webkit-slider-thumb {
      -webkit-appearance: none;
      background: #3b94d9;
      border: 0;
      border-radius: 19px;
      cursor: pointer;
      height: 19px;
      margin-top: -4.8px;
      width: 19px;
    }

    &::-moz-range-track {
      background: $range-track-bg;
      border: 0;
      border-radius: $range-track-border-radius;
      cursor: pointer;
      height: $range-track-height;
      width: 100%;
    }

    &::-moz-range-thumb {
      background: #3b94d9;
      border: 0;
      border-radius: 19px;
      cursor: pointer;
      height: 19px;
      width: 19px;
    }

    &::-ms-track {
      background: transparent;
      border-color: transparent;
      color: transparent;
      cursor: pointer;
      height: $range-track-height;
      transition: background .2s;
      width: 100%;
    }

    &::-ms-fill-lower {
      background: $range-track-bg;
      border: 0;
      border-radius: $range-track-border-radius;
    }

    &::-ms-fill-upper {
      background: $range-track-bg;
      border: 0;
      border-radius: $range-track-border-radius;
    }

    &::-ms-thumb {
      background: #3b94d9;
      border: 0;
      border-radius: 19px;
      cursor: pointer;
      height: 19px;
      height: $range-track-height;
      width: 19px;
    }

    &:focus {
      outline: none;
    }
  }

  label {
    color: #bbb;
    font-size: .9em;
    font-weight: 300;
  }
}
</style>
