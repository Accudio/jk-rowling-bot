<template>
  <nuxt />
</template>

<style lang="scss">
$family-1: 'Roboto', sans-serif;

* {
  box-sizing: border-box;
}

body {
  background-color: #ebebeb;
  display: flex;
  font-family: $family-1;
  height: 100vh;
  justify-content: center;
  line-height: 1.4;
  margin: 0;
  overflow: hidden;

  @media screen and (min-width: 768px) {
    align-items: center;
  }
}

.col {
  color: #444;
  max-height: 100vh;
  max-width: 100vw;
  overflow: auto;
  padding: 15px;
  text-align: center;
  width: 430px;

  &.wide {
    width: 830px;
  }
}

a {
  color: inherit;
}

hr {
  border: 0;
  border-top: 1px solid #d6d6d6;
  margin: 2em 0;
}

.screen-reader-text {
  border: 0;
  clip: rect(1px, 1px, 1px, 1px);
  clip-path: inset(50%);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute !important;
  width: 1px;
  word-wrap: normal !important;
}
</style>
