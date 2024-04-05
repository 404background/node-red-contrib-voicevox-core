import os
import subprocess
import json
import platform

absdir = os.path.dirname(os.path.abspath(__file__))
pathPython = ''
pathPip = ''

# Create venv

subprocess.run(['python', '-m', 'venv', 'pyenv'])
if os.name == 'nt':
    pathPython = f'{absdir}/pyenv/Scripts/python.exe'
    pathPip = f'{absdir}/pyenv/Scripts/pip.exe'
    path = {
        'NODE_PYENV_PYTHON': f'{pathPython}',
        'NODE_PYENV_PIP': f'{pathPip}'
    }
    subprocess.run([f'{pathPython}', '-m', 'pip', 'install', '--upgrade', 'pip'])
else:
    pathPython = f'{absdir}/pyenv/bin/python',
    pathPip = f'{absdir}/pyenv/bin/pip'
    path = {
        'NODE_PYENV_PYTHON': f'{pathPython}',
        'NODE_PYENV_PIP': f'{pathPip}'
    }
    subprocess.run(['sudo', f'{pathPython}', '-m', 'pip', 'install', '--upgrade', 'pip'])

with open(f'{absdir}/path.json', 'w') as f:
    json.dump(path, f, indent=2)

# pip isntall

if platform.system() == 'Windows':
    package = 'https://github.com/VOICEVOX/voicevox_core/releases/download/0.15.0/voicevox_core-0.15.0+cpu-cp38-abi3-win_amd64.whl'
# for aarch64(Raspberry Pi)
elif platform.system() == 'Linux':
    package = 'https://github.com/VOICEVOX/voicevox_core/releases/download/0.15.0/voicevox_core-0.15.0+cpu-cp38-abi3-linux_aarch64.whl'

subprocess.run([f'{pathPip}', 'install', f'{package}'])
subprocess.run([f'{pathPip}', 'install', 'requests'])
if os.name == 'nt':
    subprocess.run([f'{pathPython}', 'download.py'])
else:
    subprocess.run(['sudo', f'{pathPython}', 'download.py'])
