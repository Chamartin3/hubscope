<template lang="pug">
.container
    .row
        .col    
            Card(color="#25AAE1")        
        .col    
            Card(color="#0c3173") 
        .col    
            Card(color="#F27023")
        .col
            
</template>
<script>
import Card from '@/components/OptionsCard'
export default {
    components: { Card }


}
</script>
