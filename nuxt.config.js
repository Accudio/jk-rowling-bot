import pkg from './package'
const styleLintPlugin = require('stylelint-webpack-plugin')

export default {
  mode: 'universal',

  /*
  ** Headers of the page
  */
  head: {
    title: pkg.name,
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: pkg.description }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Roboto:400,700,900&display=swap' }
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },

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
    theme_color: '#ebebeb',
    background_color: '#ebebeb',
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
