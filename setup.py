import os
import subprocess
import json

absDir = os.path.dirname(os.path.abspath(__file__))
subprocess.run(['python', '-m', 'venv', 'pyenv'])

if os.name == 'nt':
    subprocess.run([f'{absDir}/pyenv/Scripts/python.exe', '-m', 'pip', 'install', '--upgrade', 'pip'])
    path = {
        'NODE_PYENV_PYTHON': f'{absDir}/pyenv/Scripts/python.exe',
        'NODE_PYENV_PIP': f'{absDir}/pyenv/Scripts/pip.exe'
    }
else:
    subprocess.run([f'{absDir}/pyenv/bin/python', '-m', 'pip', 'install', '--upgrade', 'pip'])
    path = {
        'NODE_PYENV_PYTHON': f'{absDir}/pyenv/bin/python',
        'NODE_PYENV_PIP': f'{absDir}/pyenv/bin/pip'
    }

with open(f'{absDir}/path.json', 'w') as f:
    json.dump(path, f, indent=2)

package = ''

# package of Voicevox Core
# https://github.com/VOICEVOX/voicevox_core/releases
if os.name == 'nt':
    package = 'https://github.com/VOICEVOX/voicevox_core/releases/download/0.15.3/voicevox_core-0.15.3+cpu-cp38-abi3-win_amd64.whl'

if package == '':
    print('Not supported for your OS')
else:
    subprocess.run([path['NODE_PYENV_PIP'], 'install', 'requests'])
    subprocess.run([path['NODE_PYENV_PIP'], 'install', package])
    subprocess.run([path['NODE_PYENV_PYTHON'], 'downloader.py'])
    subprocess.run([path['NODE_PYENV_PYTHON'], 'id_list.py'])
