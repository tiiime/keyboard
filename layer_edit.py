import json

def read():
    with open('omega45.json') as json_file:
        return json.load(json_file)

def write(data):
    with open('omega45_copy.json', 'w') as outfile:
        json.dump(data, outfile)

def copyLayer(config, source, target):
    keyboard = config['keyboard']
    keys = keyboard['keys'] 

    for key in keys:
        keycodes = key['keycodes']
        keycodes[source] = keycodes[target]

    return config

def switchLayer(config, source, target):
    keyboard = config['keyboard']
    keys = keyboard['keys'] 

    for key in keys:
        keycodes = key['keycodes']
        tmp = keycodes[source]
        keycodes[source] = keycodes[target] 
        keycodes[target] = tmp 

    return config



config = read()
# copyLayer(config, 0, 1)
# switchLayer(config, 3, 4)
write(config)
