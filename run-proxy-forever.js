var forever = require('forever-monitor');

var command = "./mining_proxy.py -o us.ozco.in -p 3333 -oh 10.253.15.125 -gp 8330 -nm -cu 28123 -cp jKTaqE";

var coinlabChild = forever.start(command.split(' '), {
    'append': true,
    'silent': true,
    'errFile': '/home/ubuntu/src/stratum-mining-proxy/logs/forever.log'
});
