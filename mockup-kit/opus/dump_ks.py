"""Read keyswitch (articulation) maps out of EastWest Opus .oib patch files."""
import zlib, json, sys, pathlib
out = {}
for f in sys.argv[1:]:
    b = open(f, 'rb').read()
    o = json.loads(zlib.decompressobj(31).decompress(b[20:]))
    a = o.get('articulations', {})
    trig = [{'name': t['name'], 'key': t['key'], 'useKey': t.get('useKey'), 'trigger': t.get('triggerName')} for t in a.get('trigger', [])]
    cc = [{'label': c.get('label'), 'cc': c.get('mappedCC'), 'name': c.get('name')} for c in o.get('controllerMap', {}).get('controls', [])]
    out[pathlib.Path(f).stem] = {'file': f, 'locator': o.get('locator'), 'keyMin': o.get('keyMin'), 'keyMax': o.get('keyMax'),
        'legato': o.get('legato'), 'currentKeySwitch': a.get('currentKeySwitch'), 'articulations': trig, 'controls': cc,
        'rows': [r['name'] for r in o.get('layerMatrix', {}).get('rows', [])]}
json.dump(out, sys.stdout, indent=1)
