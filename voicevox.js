module.exports = function(RED) {
    function Voicevox(config) {
        RED.nodes.createNode(this,config)
        let node = this
        const path = require('path')
        const fs = require('fs')
        const exec = require('child_process').exec
        const jsonPath = path.join(__dirname, 'path.json')
        const json = fs.readFileSync(jsonPath)
        const voicevoxPath = path.join(__dirname, 'voicevox.py')
        const pythonPath = JSON.parse(json).NODE_PYENV_PYTHON

        node.on('input', function(msg) {
            const command = pythonPath + ' ' + voicevoxPath + ' ' + msg.payload + ' ' + Number(config.id)
            const path_voice = __dirname + '/voice/' + msg.payload + '.wav'

            exec(command, (err, stdout, stderr) => {
                if (err) {
                    console.log(err)
                }
                console.log(stdout)
            })
            msg.payload = path_voice
            node.send(msg)
        })
    }
    RED.nodes.registerType("voicevox",Voicevox)
}
