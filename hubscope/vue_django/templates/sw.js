
self.addEventListener('install', function () {
  event.waitUntil(
    caches.open('v1').then(function(cache) {
      cache.addAll([])
    })
  )
  this.console.log('instaled SW')
})

self.addEventListener('fetch', function (event){
  this.console.log(event)
}
