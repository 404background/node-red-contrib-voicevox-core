import os
from voicevox_core import METAS
import json

absdir = os.path.dirname(os.path.abspath(__file__))
jsonList = absdir+'/id_list.json'

# for display METAS
from pprint import pprint
# pprint(METAS)

id_list = {}
options_list = []
options = {}

if os.path.isfile(jsonList):
    os.remove(jsonList)

for i in METAS:
    name = i.name
    for j in i.styles:
        id = j.id
        style = j.name
        id_list = {}
        id_list['value'] = id
        id_list['label'] = f'{name}, {style}'
        options[id] = f'{name}, {style}'   
# pprint(options)

with open(jsonList, 'a', encoding="utf-8") as f:
    json.dump(options, f, indent=2, ensure_ascii=False)
