#!/usr/bin/env python3
"""Assemble public/index.html = src/app.src.html + data/data.json + data/use.json"""
import json, pathlib
r = pathlib.Path(__file__).parent
d = json.load(open(r/'data/data.json', encoding='utf-8'))
d.pop('W', None)                       # anciens échauffements, inutilisés
d['USE'] = json.load(open(r/'data/use.json', encoding='utf-8'))
blob = json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
src = (r/'src/app.src.html').read_text(encoding='utf-8')
assert '__DATA__' in src
(r/'public/index.html').write_text(src.replace('__DATA__', blob), encoding='utf-8')
print('OK public/index.html', (r/'public/index.html').stat().st_size, 'octets')
