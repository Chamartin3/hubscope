<template lang="pug">
div.d-block.mx-auto.text-center
  v-text-field(v-if="type=='text'"
    v-model="form.val"
    :value="val"
    :placeholder="name"
    :label="name"
    :error-messages="error"
    required)

  v-textarea(v-if="type=='textarea'"
    rows="1"
    :auto-grow="true",
    :clearable="true",
    v-model="form.val"
    :value="val"
    :placeholder="name"
    :label="name"
    :error-messages="error"
    required)


  v-text-field(v-if="type=='email'"
    type="email"
    v-model="form.val"
    :placeholder="name"
    :label="name"
    :error-messages="error"
    required)

  v-text-field(v-if="type=='number'"
    type="number"
    v-model="form.val"
    :placeholder="name"
    :label="name"
    :error-messages="error"
    required)

  v-text-field(v-if="type=='url'"
    type="url"
    v-model="form.val"
    :placeholder="name"
    :label="name"
    :error-messages="error"
    required)

  v-color-picker(v-if="type=='color'"
    hide-canvas
    hide-inputs
    hide-mode-switch
    mode.sync="hex"
    show-swatches
    v-model="form.val"
    :label="name"
    :error-messages="error"
    required)

  v-menu(v-if="type=='date'"
    ref="menu"
    v-model='menu'
    :close-on-content-click='false'
    transition='scale-transition'
    offset-y=''
    min-width='290px')
    template(v-slot:activator='{ on }')
      v-text-field(
        v-model='form.val'
        :label='name'
        prepend-icon='fas fa-calendar-alt'
        readonly
        v-on='on')
    v-date-picker(v-model='form.val' no-title scrollable)
      .flex-grow-1
      v-btn(text='' color='primary' @click='menu = false') Cancelar
      v-btn(text='' color='primary' @click='$refs.menu.save(form)') OK


  v-menu(v-if="type=='time'"
    ref="menu"
    v-model='menu'
    :close-on-content-click='false'
    transition='scale-transition'
    offset-y=''
    min-width='290px')
    template(v-slot:activator='{ on }')
      v-text-field(
        v-model='form.val'
        :label='name'
        prepend-icon='fas fa-clock'
        readonly
        v-on='on')
    v-time-picker(
      landscape
      ampm-in-title
      format="ampm"
      v-model="form.val"
      :placeholder="name"
      :label="name"
      :error-messages="error"
      required)

  DateTimeField(v-if="type=='datetime'"
    v-model="form.val"
    :placeholder="name"
    :label="name"
    required
  )

  v-avatar.elevation-6(size='180' v-if="image")
    img(:src="image")
  v-file-input(v-if="type=='image'"
    accept="image/png, image/jpeg, image/jpg"
    prepend-icon="fas fa-camera-retro"
    :placeholder="name"
    :label="name"
    v-model="form.val"
    required)

  v-file-input(v-if="type=='file'"
    v-model="form.val"
    :placeholder="name"
    :label="name"
    required)

  v-select(v-if="type=='select'"
  :label="name"
  item-text="value"
  item-value="key"
  :items="itemOptions"
  required
  v-model="form.val"
  )


  v-autocomplete(v-if="type=='country'"
    v-model="form.val"
    placeholder="Seleccione un pais."
    :items="countries"
    label="Pais"
    required)

  v-row.justify-center(v-if="type=='gender'")
    v-col()
      v-btn(
        rounded
        @click.native="form.val='M'"
        :disabled="form.val=='M'"
        color="primary")
        v-icon() fas fa-mars
    v-col()
      v-btn(
        rounded
        @click.native="form.val='F'"
        :disabled="form.val=='F'"
        color="primary")
        v-icon() fas fa-venus
</template>
<script>
import {baseSubForm} from '#/Forms'

import DateTimeField from './DateTimeForm'
// :rules="[() => !!name || 'This field is required']"
export default {
mixins:[baseSubForm],
components:{DateTimeField},
props:{
  type:{
    type: String,
    default:"text",
    validator: (prop) => [
      'text',
      'number',
      'email',
      'url',
      'country',
      'color',
      'date',
      'time',
      'image',
      'file',
      'textarea',
      'select',
      'datetime',
    ].includes(prop)
  },
  name:{
    type:String,
  },
  val:{},
  itemOptions:{
    type:Array
  }
},
watch:{
  type(val){
    if(val==='color') this.form.val=""
    if(val==='image') this.form.val=""
  },
  val(val){
    this.form.val = val ? val : null
  }
},
computed:{
  error(){
    if(this.errors instanceof Object) return this.errors[0]
    return this.errors
  },
  image(){
    if(this.type==='image' && this.form.val) {
      let file = this.form.val
      if(typeof file=== 'string') return file
      return URL.createObjectURL(file)
    }
    return null
  }
},
data(){
  return {
    form:{
      val:''
    },
    menu:false,
    countries: ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua &amp; Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia &amp; Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Cape Verde', 'Cayman Islands', 'Chad', 'Chile', 'China', 'Colombia', 'Congo', 'Cook Islands', 'Costa Rica', 'Cote D Ivoire', 'Croatia', 'Cruise Ship', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Estonia', 'Ethiopia', 'Falkland Islands', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Polynesia', 'French West Indies', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kuwait', 'Kyrgyz Republic', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Namibia', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Pierre &amp; Miquelon', 'Samoa', 'San Marino', 'Satellite', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'St Kitts &amp; Nevis', 'St Lucia', 'St Vincent', 'St. Lucia', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', "Timor L'Este", 'Togo', 'Tonga', 'Trinidad &amp; Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks &amp; Caicos', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Virgin Islands (US)', 'Yemen', 'Zambia', 'Zimbabwe'],
  }
},
created(){
  this.form.val = this.val ? this.val : null
}
}
</script>
