New-Item voicevox -ItemType Directory
Set-Location voicevox
Invoke-WebRequest https://github.com/VOICEVOX/voicevox_core/releases/latest/download/download-windows-x64.exe -OutFile ./download.exe
.\download.exe
pip install https://github.com/VOICEVOX/voicevox_core/releases/download/0.14.5/voicevox_core-0.14.5+cpu-cp38-abi3-win_amd64.whl
Copy-Item .\voicevox_core\onnxruntime.dll ..\
Remove-Item .\download.exe
Set-Location ..
