import json
import time

device_map = None

with open("device_map.json", "r") as file:
    # Load the JSON data
    device_map = json.load(file)

source = None

def move(exp_tm):
    for tm in range(0, exp_tm):
    # cur = '<=' if movement_options[0]['moving'] == 'backward' else '=>'
        time.sleep(1)
        print('<=', end=' ', flush=True)


while True:
        
    with open('source.txt', 'r') as f:
        source = f.read()

    with open('destination.txt', 'r') as g:
        destination = g.read()
        
    if source != destination:
        movement_options = list(filter(lambda y: y['end'] == destination, list(filter(lambda x : x['start'] == source, device_map['combinations']))))
        exp_tm = movement_options[0]['time']
        print('From:: ', source, 'Destination:: ', destination, 'Expected Time:: ', exp_tm)
        
        move(exp_tm)
        
        
