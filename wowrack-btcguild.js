var forever = require('forever-monitor');

var port = 51;
var command;
for (var i = 0; i < 121; i++) {
    real_port = 8300 + port
    real_stport = 3300 + port
    command = "./mining_proxy.py -o 50.31.149.57 -p 3333 -sp " + real_stport + " -oh 10.100.0.9 -gp " + real_port + " -nm -cu Alydian_w" + (port - 51);
    forever.start(command.split(' '), {
        'append': true,
        'silent': true,
        'errFile': "/home/ubuntu/src/stratum-mining-proxy/logs/w" + i + ".log"
    });
    port++;
}
