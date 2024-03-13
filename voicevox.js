module.exports = function(RED) {
    function Voicevox(config) {
        RED.nodes.createNode(this,config);
        let node = this;
        node.on('input', function(msg) {
            const exec = require('child_process').exec;
            let path = require('path');
            const path_voicevox = path.join(__dirname, 'voicevox.py')
            const command = 'python ' + path_voicevox + ' ' + msg.payload + ' ' + Number(config.id);
            const path_voice = __dirname + '/voice/' + msg.payload + '.wav';

            exec(command, (err, stdout, stderr) => {
                if (err) { console.log(err); }
                console.log(stdout);
            });
            msg.payload = path_voice;
            node.send(msg);
        });
    }
    RED.nodes.registerType("voicevox",Voicevox);
}
