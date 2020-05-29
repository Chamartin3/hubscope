<template lang="pug">
.container
    .row
        .col
            Card(
            icon="fa-file-excel"
            titulo="Informes"
            subtitle=""
            color="primary" )        
        .col
            Card(
            icon="fa-chart-bar"
            titulo="Reporte"
            subtitle=""
            color="secondary" )        
        .col
            Card(
            icon="far fa-clipboard"
            titulo="Asignación"
            subtitle=""
            color="terciary" )        
    .row
        .col
            Card(
            icon="fas fa-globe-americas"
            titulo="Prueba de Color suave"
            subtitle="tarjeta solo de pruebas"
            color="primary lighten-2" )        
        .col
            Card(
            icon="fas fa-globe-americas"
            titulo="Prueba de Color suave"
            subtitle="tarjeta solo de pruebas"
            color="secondary lighten-2" )        
        .col
            Card(
            icon="fas fa-globe-americas"
            titulo="Prueba de Color suave"
            subtitle="tarjeta solo de pruebas"
            color="terciary lighten-2" )
    .row
        .col
            Card(
            icon="fas fa-globe-americas"
            titulo="Prueba de Color oscuro"
            subtitle="tarjeta solo de pruebas"
            color="primary darken-2" )        
        .col
            Card(
            icon="fas fa-globe-americas"
            titulo="Prueba de Color oscuro"
            subtitle="tarjeta solo de pruebas"
            color="secondary darken-2" )        
        .col
            Card(
            icon="fas fa-globe-americas"
            titulo="Prueba de Color oscuro"
            subtitle="tarjeta solo de pruebas"
            color="terciary darken-2" )    
    .row
        .col
            Card(
            icon="fas fa-globe-americas"
            titulo="Prueba de Color acetuado"
            subtitle="tarjeta solo de pruebas"
            color="primary accent-4" )        
        .col
            Card(
            icon="fas fa-globe-americas"
            titulo="Prueba de Color acetuado"
            subtitle="tarjeta solo de pruebas"
            color="secondary accent-4" )        
        .col
            Card(
            icon="fas fa-globe-americas"
            titulo="Prueba de Color acetuado"
            subtitle="tarjeta solo de pruebas"
            color="terciary accent-4" )
            
</template>
<script>
import Card from '@/components/OptionsCard'
export default {
    components: { Card }


}
</script>
