var forever = require('forever-monitor');

var command = "./mining_proxy.py -o us.ozco.in -p 3333 -sp 3334 -oh 10.253.15.125 -gp 8330 -nm -cu alydian.96board -cp oi09hy";

forever.start(command.split(' '), {
    'append': true,
    'silent': true,
    'errFile': '/home/ubuntu/src/stratum-mining-proxy/logs/96board.log'
});

command = "./mining_proxy.py -o us.ozco.in -p 3333 -sp 3333 -oh 10.253.15.125 -gp 8331 -nm -cu alydian.256boards -cp f8ywo9";

forever.start(command.split(' '), {
    'append': true,
    'silent': true,
    'errFile': '/home/ubuntu/src/stratum-mining-proxy/logs/256boards.log'
});
