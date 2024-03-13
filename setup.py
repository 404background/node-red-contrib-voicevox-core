import os
import subprocess
import shutil
import requests

absdir = os.path.dirname(os.path.abspath(__file__))


#pip install

## for Windows
if os.name == 'nt':
    package = 'https://github.com/VOICEVOX/voicevox_core/releases/download/0.15.0/voicevox_core-0.15.0+cpu-cp38-abi3-win_amd64.whl'
    subprocess.run(f'pip install requests')
    subprocess.run(f'pip install {package}')


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
    new_path = shutil.copy(f'{absdir}/voicevox_core/onnxruntime.dll', f'{absdir}/onnxruntime.dll')
