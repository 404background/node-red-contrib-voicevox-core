module.exports = function(RED) {
    function Voicevox(config) {
        RED.nodes.createNode(this,config)
        let node = this
        node.on('input', function(msg) {
            const exec = require('child_process').exec
            const fs = require('fs')
            const path = require('path')

            const path_voicevox = path.join(__dirname, 'voicevox.py')
            const path_voice = path.join(__dirname, 'voice', msg.payload + '.wav')
            const jsonPath = path.join(__dirname, 'path.json')
            const json = fs.readFileSync(jsonPath)
            const pythonPath = JSON.parse(json).NODE_PYENV_PYTHON
            const command = pythonPath + ' ' + path_voicevox + ' ' + msg.payload + ' ' + Number(config.id)

            exec(command, (err, stdout, stderr) => {
                if (err) { console.log(err) }
                console.log(stdout)
            })
            msg.payload = path_voice
            node.send(msg)
        })
    }
    RED.nodes.registerType("voicevox",Voicevox)
}
