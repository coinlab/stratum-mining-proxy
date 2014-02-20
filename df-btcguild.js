var forever = require('forever-monitor');

var port = 51;
var command;
for (var i = 0; i < 49; i++) {
    real_port = 8300 + port
    real_stport = 3300 + port
    command = "./mining_proxy.py -o 50.31.149.57 -p 3333 -sp " + real_stport + " -oh 192.168.1.2 -gp " + real_port + " -nm -cu Alydian_d" + (port - 51);
    forever.start(command.split(' '), {
        'append': true,
        'silent': true,
        'errFile': "/home/ubuntu/src/stratum-mining-proxy/logs/d" + i + ".log"
    });
    port++;
}
