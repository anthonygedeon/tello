const dgram = require('dgram');
const { EventEmitter } = require('events');

const socket = dgram.createSocket('udp4');

const PORT = 8889;

socket.on('error', (err) => {
	console.log(`socket error:\n${err.stack}`);
	socket.close();
});

socket.on('message', (msg, rinfo) => {
	console.log(`socket got: ${msg} from ${rinfo.address}:${rinfo.port}`);
});

socket.on('connect', () => {
    socket.send('takeoff', (error) => {
        
    })
});

socket.connect(PORT, '192.168.10.1', (error) => {
    
});

