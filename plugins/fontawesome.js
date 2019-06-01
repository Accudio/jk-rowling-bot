import Vue from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faSyncAlt, faReply, faRetweet, faHeart } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

// font awesome icon library
library.add(faSyncAlt, faReply, faRetweet, faHeart)
Vue.component('font-awesome-icon', FontAwesomeIcon)