export default {
  name: "",
  data(){
    return {
      dialog: false,
      activator: false,
      loading: true,

      modalColor:null,
      modalDark:false,
      maxWidth:null,
      modalTitle:null,
      buttomText:null,
    }
  },
  methods:{
    open () {
      this.dialog = true
    },
    close () {
      this.dialog = false
      this.instance = null
    },

  }
}
