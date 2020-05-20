// https://vuex.vuejs.org/en/state.html

let vdcontext = {...DJANGO_CONTEXT}

let user
let profile
let socio

if(vdcontext.user){
  user = vdcontext.user
  profile = vdcontext.user.profile
  socio = vdcontext.user.socio
}
export default {
  django: vdcontext,
  user:user,
  profile:profile,
  socio:socio,
}
