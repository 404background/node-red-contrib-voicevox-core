import os
import subprocess
import requests
import shutil

absDir = os.path.dirname(os.path.abspath(__file__))

# Execute downloader

## for Windows
if os.name == 'nt':
    url='https://github.com/VOICEVOX/voicevox_core/releases/latest/download/download-windows-x64.exe'
    filename=f'{absDir}/download.exe'
    urlData = requests.get(url).content
    with open(filename ,mode='wb') as f:
        f.write(urlData)
    subprocess.run(filename)
    os.remove(filename)
    new_path = shutil.copy(f'{absDir}/voicevox_core/onnxruntime.dll', f'{absDir}/pyenv/Lib/site-packages/voicevox_core/onnxruntime.dll')
