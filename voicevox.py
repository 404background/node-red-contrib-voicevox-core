import os, sys
from pathlib import Path
from voicevox_core import VoicevoxCore

absdir = os.path.dirname(os.path.abspath(__file__))
core = VoicevoxCore(open_jtalk_dict_dir=Path(f'{absdir}/voicevox_core/open_jtalk_dic_utf_8-1.11'))

speaker_id = 2
if len(sys.argv) == 3:
    speaker_id = int(sys.argv[2])

text = sys.argv[1]
if not core.is_model_loaded(speaker_id):
    core.load_model(speaker_id)
wave_bytes = core.tts(text, speaker_id)
with open(f'{absdir}/voice/' + text + '.wav', 'wb') as f:
    f.write(wave_bytes)
