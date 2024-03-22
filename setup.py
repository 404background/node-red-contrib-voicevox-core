import os
import subprocess
import shutil
import requests
import json

absdir = os.path.dirname(os.path.abspath(__file__))

subprocess.run(['python', '-m', 'venv', 'pyenv'])

if os.name == 'nt':
    subprocess.run([f'{absdir}/pyenv/Scripts/python.exe', '-m', 'pip', 'install', '--upgrade', 'pip'])
    path = {
        'NODE_PYENV_PYTHON': f'{absdir}/pyenv/Scripts/python.exe',
        'NODE_PYENV_PIP': f'{absdir}/pyenv/Scripts/pip.exe'
    }
else:
    subprocess.run([f'{absdir}/pyenv/bin/python', '-m', 'pip', 'install', '--upgrade', 'pip'])
    path = {
        'NODE_PYENV_PYTHON': f'{absdir}/pyenv/bin/python',
        'NODE_PYENV_PIP': f'{absdir}/pyenv/bin/pip'
    }

with open(f'{absdir}/path.json', 'w') as f:
    json.dump(path, f, indent=2)



#pip install

## for Windows
if os.name == 'nt':
    package = 'https://github.com/VOICEVOX/voicevox_core/releases/download/0.15.0/voicevox_core-0.15.0+cpu-cp38-abi3-win_amd64.whl'
    subprocess.run([f'{absdir}/pyenv/Scripts/pip.exe', 'install', 'requests'])
    subprocess.run([f'{absdir}/pyenv/Scripts/pip.exe', 'install', f'{package}'])


# Execute downloader

## for Windows
if os.name == 'nt':
    url='https://github.com/VOICEVOX/voicevox_core/releases/latest/download/download-windows-x64.exe'
    filename=f'{absdir}/download.exe'
    urlData = requests.get(url).content
    with open(filename ,mode='wb') as f:
        f.write(urlData)
    subprocess.run(filename)
    os.remove(filename)
    new_path = shutil.copy(f'{absdir}/voicevox_core/onnxruntime.dll', f'{absdir}/pyenv/Lib/site-packages/voicevox_core/onnxruntime.dll')
