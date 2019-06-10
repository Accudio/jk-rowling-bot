<template>
  <div class="tweet-wrap">
    <div class="tweet">
      <div class="tweet-head">
        <div class="tweet-image">
          <img src="https://avatars.io/twitter/jk_rowling/" alt="avatar">
        </div>
        <div class="tweet-author">
          <div class="name">
            J.K. Rowling
          </div>
          <div class="handle">
            @jk_rowling
          </div>
        </div>
        <button id="refresh-tweet" class="tweet-refresh" :class="{ 'active': refreshing }" title="Refresh Tweet" @click="refreshTweet" @animationend="refreshing = false">
          <font-awesome-icon :icon="['fas', 'sync-alt']" />
        </button>
      </div>
      <div class="tweet-body">
        <p id="tweet-text">
          {{ currentTweet }}
        </p>
      </div>
      <div class="tweet-footer">
        <div class="icons">
          <font-awesome-icon :icon="['fas', 'reply']" />
          <font-awesome-icon :icon="['fas', 'retweet']" />
          <font-awesome-icon :icon="['fas', 'heart']" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import tweets from '~/data/data.json'

export default {
  props: {
    currentAcc: {
      type: Number,
      default: 50
    }
  },

  data: () => ({
    tweets: tweets,
    currentTweet: '',
    lastTweet: '',
    refreshing: false
  }),

  watch: {
    currentAcc: function() {
      this.changeTweet()
    }
  },

  mounted: function() {
    this.changeTweet()
  },

  methods: {
    changeTweet: function() {
      this.lastTweet = this.currentTweet
      do {
        this.currentTweet = this.tweets[this.currentAcc / 100][Math.floor(Math.random()*this.tweets[this.currentAcc / 100].length)]
      } while (this.currentTweet === this.lastTweet)
    },
    refreshTweet: function() {
      this.refreshing = true
      this.changeTweet()
    }
  }
}
</script>

<style lang="scss">
$accent-colour: #3b94d9;
$light-colour: #697882;
$family-1: 'Roboto', sans-serif;

.tweet-wrap {
  align-items: center;
  display: flex;
  margin: 30px 0;
  min-height: 200px;
}

.tweet {
  background-color: #fff;
  border: 1px solid #e1e8ed;
  border-radius: 5px;
  color: #000;
  cursor: pointer;
  max-width: 100vw;
  padding: 20px;
  position: relative;
  text-align: left;
  transition: border-color .1s;
  width: 100%;
  
  &:hover {
    border-color: #ccd6dd;
  }
  
  .tweet-head {
    display: flex;
    line-height: 1.2;
    
    .tweet-image {
      align-items: center;
      display: flex;
      margin-right: 9px;
      
      img {
        border-radius: 999px;
        height: 38px;
        width: 38px;
      }
    }
    
    .tweet-author {
      display: flex;
      flex-direction: column;
      justify-content: center;
      
      &:hover .name {
        color: $accent-colour;
      }
      
      .name {
        font-weight: 800;
        transition: color .1s;
      }
      
      .handle {
        color: $light-colour;
        font-size: .875rem;
      }
    }
    
    .tweet-refresh {
      appearance: none;
      background: none;
      border: 0;
      color: $light-colour;
      cursor: pointer;
      font-size: 1rem;
      margin-bottom: auto;
      margin-left: auto;
      outline: 0;
      padding: .4rem;
      transition: color .1s;
      
      &:hover {
        color: inherit;
      }
      
      &.active svg {
        animation: refresh .4s ease-in-out;
      }
    }
  }

  .tweet-body {
    min-height: 3rem;
    padding: 1em 0;

    p {
      margin: 0 0 1em;

      &:last-child {
        margin: 0;
      }
    }
  }
  
  .tweet-footer {
    .icons {
      svg {
        color: $light-colour;
        margin-right: 1rem;
        max-height: 1em;
        max-width: 1.5em;
        transition: color .1s;
        
        .icon-number {
          font-family: $family-1;
          font-size: 1rem;
          font-weight: normal;
        }
      }
      
      .fa-reply:hover {
        color: $accent-colour;
      }

      .fa-retweet:hover {
        color: #3da50d;
      }

      .fa-heart:hover {
        color: #e0245e;
      }
    }
  }
}

@keyframes refresh {
  0% {
    transform: rotate(0);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>
