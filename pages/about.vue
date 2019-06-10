<template>
  <div class="col wide">
    <nuxt-link to="/" class="back">
      <font-awesome-icon :icon="['fas', 'arrow-up']" />
      <span class="screen-reader-text">Back to Homepage</span>
    </nuxt-link>
    <p>At a social evening in early 2019, a few friends and I were discussing the tweets <a href="https://twitter.com/jk_rowling" target="_blank" rel="noopener">J.K. Rowling</a> made over several years making what some people saw as changes to the Harry Potter canon after the fact. Although some of these were in fact reiteration or her perspective as author on what she had written, many people found it ridiculous, entertaining, or found it added to that world. Regardless, that evening we were all joking about it. A suggestion came up that someone should come up with a J.K. Rowling tweet generator, and as I was already messing around with neural networks and machine learning, I took it upon myself to give it a shot.</p>
    <p>I don't claim this is good enough to really be that generator, but with my limited knowledge and a limited dataset I consider it good enough to show off. You can see all of the source code using the link below, but it's a fairly simple implementation of a word-level neural language model using an LTSM neural network. I feed it a list of formatted words and punctation, it converts it into a pattern, and then we train the model on the patterns of those numbers. I can then use this model to, given a 'seed' of text, predict what word or punctuation would come next.</p>
    <p>The slider below the tweet allows you to set the accuracy of the output tweets, with 0% being totally random words, and 100% just reciting the original. The lower values give amusing results as the network gets stuck on certain words, while the higher feels like J.K. has just forgotten how the English language works. Between 40% and 70% I find is the sweet spot of making enough sense to be readable, yet not enough to still result in some wild combinations.</p>
    <p>This was made without the permission of J.K. Rowling, or any of the other Harry Potter copyright holders, and is intended as parody. If there are any issues with any particular generated 'tweets', or with the 'Bot' in general, please contact me at <a href="mailto:alistair@accudio.com">alistair@accudio.com</a></p> 
    <hr>
    <p>
      <a href="https://github.com/Accudio/jk-rowling-bot">Source available on Github</a><br>
      Neural Network powered by <a href="https://keras.io/" target="_blank" rel="noopener">Keras</a> and <a href="https://www.tensorflow.org/" target="_blank" rel="noopener">Tensorflow</a><br>
      Website built using <a href="https://nuxtjs.org/" target="_blank" rel="noopener">Nuxt.js</a> and hosted with <a href="https://www.netlify.com/" target="_blank" rel="noopener">Netlify</a><br>
      List of tweets came from <a href="https://www.reddit.com/r/harrypotter/comments/5jwr40/compilation_of_all_jk_rowlings_harry_potter/" target="_blank" rel="noopener">u/ibid-11962</a> on Reddit.
    </p>
    <hr>
    <p>
      Made by Alistair Shepherd<br>
      <a href="https://alistairshepherd.uk">alistairshepherd.uk</a><br>
      <a href="https://github.com/accudio">github.com/accudio</a><br>
      <a href="https://twitter.com/accudio">@accudio</a>
    </p>
  </div>
</template>

<style lang="scss" scoped>
.page-enter-active {
  animation: transitionEnter .5s;
}

.page-leave-active {
  animation: transitionLeave .5s;
}

@keyframes transitionEnter {
  0% {
    transform: translateY(100vh);
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
    transform: translateY(100vh);
  }
}

.back {
  display: block;
  margin-bottom: 3rem;
  text-align: center;
}
</style>
