
import json, os
PATH="data/config.json"

def load():
    if not os.path.exists(PATH): return {}
    return json.load(open(PATH))

def save(d):
    json.dump(d, open(PATH,"w"), indent=2)
