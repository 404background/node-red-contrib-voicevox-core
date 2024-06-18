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

        voiceID = Number(config.voiceID)
        voiceFolder = config.voiceFolder

        node.on('input', function(msg) {
            if(typeof msg.voiceID !== 'undefined' && msg.voiceID !== '') {
                voiceID = msg.voiceID
            }
            if(typeof msg.voiceFolder !== 'undefined' && msg.voiceFolder !== '') {
                voiceFolder = msg.voiceFolder
            }

            fileName = msg.payload + '_' + voiceID + '.wav'
            voicePath = path.join(voiceFolder, fileName)

            let command = pythonPath + ' ' + voicevoxPath + ' ' + msg.payload + ' ' + voiceID+ ' ' + voicePath
            exec(command, (err, stdout, stderr) => {
                if (err) { console.log(err) }
                console.log(stdout)
            })
            msg.payload = voicePath
            node.send(msg)
        })
    }
    RED.nodes.registerType("voicevox",Voicevox)
}
