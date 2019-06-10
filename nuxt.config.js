import pkg from './package'
const styleLintPlugin = require('stylelint-webpack-plugin')

export default {
  mode: 'universal',

  /*
  ** Headers of the page
  */
  head: {
    title: 'J.K. Rowling Bot - Harry Potter tweets with machine learning',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Have you ever wondered what happens when you run all of J.K. Rowling\'s \'Harry Potter\' plot related tweets through a neural network and ask it to create some more? Well I did, and this is the result!' }
    ],
    link: [
      { rel: 'apple-touch-icon', sizes: '180x180', href: '/apple-touch-icon.png' },
      { rel: 'icon', type: 'image/png', sizes: '32x32', href: '/favicon-32x32.png' },
      { rel: 'icon', type: 'image/png', sizes: '16x16', href: '/favicon-16x16.png' },
      { rel: 'manifest', href: '/site.webmanifest' },
      { rel: 'mask-icon', href: '/safari-pinned-tab.svg', color: '#3b94d9' },
      { name: 'apple-mobile-web-app-title', content: 'J.K. Rowling Bot' },
      { name: 'application-name', content: 'J.K. Rowling Bot' },
      { name: 'msapplication-TileColor', content: '#3b94d9' },
      { name: 'theme-color', content: '#3b94d9' },
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Roboto:300,400,700,900&display=swap' },
      { property: 'og:image:width', content: '1190' },
      { property: 'og:image:height', content: '623' },
      { property: 'og:description', content: 'Ever wondered what happens when you run J.K. Rowling\'s \'Harry Potter\' plot related tweets through a neural network and make it create more? This is the result!' },
      { property: 'og:title', content: 'J.K. Rowling Bot - Harry Potter tweets with machine learning' },
      { property: 'og:url', content: 'https://jkrowling.alistairshepherd.uk' },
      { property: 'og:image', content: 'https://jkrowling.alistairshepherd.uk/og-image.jpg' }
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: false,

  generate: {
    fallback: true,
    minify: {
      collapseWhitespace: false
    }
  },

  /*
  ** Global CSS
  */
  css: [
  ],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    '~/plugins/fontawesome.js'
  ],

  /**
   ** Manifest
   */
  manifest: {
    author: 'Alistair Shepherd',
    name: 'JK Rowling Bot',
    short_name: 'JK Rowling Bot',
    lang: 'en',
    theme_color: '#3b94d9',
    background_color: '#3b94d9',
    description: 'JK Rowling Bot',
    display: 'standalone',
    nativeUI: true
  },

  /*
  ** Nuxt.js modules
  */
  modules: [
    '@nuxtjs/pwa'
  ],

  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
      // Run ESLint on save
      if (ctx.isDev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    },
    plugins: [
      new styleLintPlugin({
        configFile: '.stylelintrc.js',
        files: ['**/*.scss', '**/*.sass', '**/*.vue'],
        failOnError: false,
        quiet: false,
      })
    ],
  }
}
