var forever = require('forever-monitor');

var port = 51;
var command;
for (var i = 0; i < 25; i++) {
    command = "./mining_proxy.py -o 50.31.149.57 -p 3333 -sp 33" + port + " -oh 10.85.134.127 -gp 83" + port + " -nm -cu Alydian_w" + (port - 51);
    forever.start(command.split(' '), {
        'append': true,
        'silent': true,
        'errFile': "/home/ubuntu/src/stratum-mining-proxy/logs/w" + i + ".log"
    });
    port++;
}
