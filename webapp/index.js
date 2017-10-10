var awsIot = require('aws-iot-device-sdk');
var io = require('socket.io')(3000);

var thingName = '00000569'; // Replace with your own thing name

var device = awsIot.device({
   keyPath: './certs/privkey.pem',
  certPath: './certs/cert.pem',
    caPath: './certs/ca.pem',
  clientId: thingName,
      host: 'a31ovqfkmg1ev8.iot.eu-west-1.amazonaws.com'
});

device.on('connect', function() {
  console.log('Client connected');
  device.subscribe('$aws/things/' + thingName + '/shadow/update');
});

device.on('message', function(topic, payload) {
  console.log('Message: ', topic, payload.toString());

  // Broadcast the message to any connected socket clients
  io.emit('broadcast', {topic, message: payload.toString()});
});
