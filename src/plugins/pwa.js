Notification.requestPermission(function(result) {
    console.log('Notification permission status:', result);
    if (result === 'denied') {
      console.log('Permission wasn\'t granted. Allow a retry.');
      return;
    } else {

      navigator.serviceWorker.register('./service_worker').then(function(reg){
          reg.pushManager.getSubscription().then(function(sub) {
            console.log(sub)
            if (sub === null) {
              // Update UI to ask user to register for Push
              console.log('Not subscribed to push service!');
            } else {
              // We have a subscription, update the database
              console.log('Subscription object: ', sub);
            }
          });
          console.log(navigator.serviceWorker.ready)
      },fail=>{
        console.error(fail.code)
        console.error(fail.message)
      })

    }
});
