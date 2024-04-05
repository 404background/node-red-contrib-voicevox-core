import os
import subprocess
import shutil
import requests
import glob

absdir = os.path.dirname(os.path.abspath(__file__))

# Execute downloader

if os.name == 'nt':
    url = 'https://github.com/VOICEVOX/voicevox_core/releases/latest/download/download-windows-x64.exe'
    pathLib = f'{absdir}/pyenv/Lib/site-packages'
    filename = f'{absdir}/download.exe'
# for aarch64(Raspberry Pi)
elif platform.system() == 'Linux':
    url='https://github.com/VOICEVOX/voicevox_core/releases/latest/download/download-linux-arm64'
    pathLib = glob.glob(f'{absdir}/pyenv/lib/*/site-packages')
    filename = f'{absdir}/download'

urlData = requests.get(url).content
with open(filename ,mode='wb') as f:
    f.write(urlData)
subprocess.run(filename)
os.remove(filename)
new_path = shutil.copy(f'{absdir}/voicevox_core/onnxruntime.dll', f'{pathLib}/voicevox_core/onnxruntime.dll')
