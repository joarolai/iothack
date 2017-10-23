var ttn = require("ttn")

var appID = "todo"	// Update to match your application
var accessKey = "todo"	// Updated to match your application

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
