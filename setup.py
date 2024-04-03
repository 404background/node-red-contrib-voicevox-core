import os
import subprocess
import shutil
import requests
import json
import platform

absdir = os.path.dirname(os.path.abspath(__file__))
pathPython = ''
pathPip = ''

subprocess.run(['python', '-m', 'venv', 'pyenv'])

if os.name == 'nt':
    pathPython = f'{absdir}/pyenv/Scripts/python.exe'
    pathPip = f'{absdir}/pyenv/Scripts/pip.exe'
    subprocess.run([f'{pathPython}', '-m', 'pip', 'install', '--upgrade', 'pip'])
    path = {
        'NODE_PYENV_PYTHON': f'{pathPython}',
        'NODE_PYENV_PIP': f'{pathPip}'
    }
else:
    pathPython = f'{absdir}/pyenv/bin/python',
    pathPip = f'{absdir}/pyenv/bin/pip'
    subprocess.run([f'{pathPython}', '-m', 'pip', 'install', '--upgrade', 'pip'])
    path = {
        'NODE_PYENV_PYTHON': f'{pathPython}',
        'NODE_PYENV_PIP': f'{pathPip}'
    }

with open(f'{absdir}/path.json', 'w') as f:
    json.dump(path, f, indent=2)


#pip install

## for Windows
if platform.system() == 'Windows':
    package = 'https://github.com/VOICEVOX/voicevox_core/releases/download/0.15.0/voicevox_core-0.15.0+cpu-cp38-abi3-win_amd64.whl'
    pathPip = f'{absdir}/pyenv/Scripts/pip.exe'
elif platform.system() == 'Linux':
    package=''
    pathPip = f'{absdir}/pyenv/bin/pip'

subprocess.run([f'{pathPip}', 'install', 'requests'])
subprocess.run([f'{pathPip}', 'install', f'{package}'])

# Execute downloader

## for Windows
if os.name == 'nt':
    url = 'https://github.com/VOICEVOX/voicevox_core/releases/latest/download/download-windows-x64.exe'
    pathLib = f'{absdir}/pyenv/Lib/site-packages'
elif platform.system() == 'Linux':
    url=''
    pathLib = f'{absdir}/pyenv/lib/pythonX.Y/site-packages'

filename=f'{absdir}/download.exe'
urlData = requests.get(url).content
with open(filename ,mode='wb') as f:
    f.write(urlData)
subprocess.run(filename)
os.remove(filename)
new_path = shutil.copy(f'{absdir}/voicevox_core/onnxruntime.dll', f'{pathLib}/voicevox_core/onnxruntime.dll')

