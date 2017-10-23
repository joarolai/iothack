var ttn = require("ttn")

var appID = "nuapp"
var accessKey = "ttn-account-v2.2G-9uzFhWozpOzWtilEnBqzFAANme6QVKaQeAnqQ-S8"

var io = require('socket.io')(3000);


ttn.data(appID, accessKey)
  .then(function (client) {
    client.on("uplink", function (devID, payload) {

      console.log(devID)
      console.log(payload);
      console.log(payload.metadata.gateways)

      console.log("Received uplink from ", devID)

      var maTemp = payload.payload_fields.temperature;

      var telenorString ='{"state":{"reported":{"temperature":' + maTemp + '}}}';

      console.log("Emit message");
      io.emit('broadcast', {message: telenorString});

    })
  })
  .catch(function (error) {
    console.error("Error", error)
    process.exit(1)
  })
