import csv
import json
import requests


def get_object(data):
    cr = csv.reader(data.splitlines(), delimiter=',')
    raw = list(cr)
    headers = [h.lower() for h in raw[0]]
    output = []
    for row in raw[1:]:
        obj = {}
        for idx, header in enumerate(headers):
            obj[header] = row[idx]
        output.append(obj)
    return output


def get_nodes(data, offset=0):
    nodes = []
    for idx, obj in enumerate(data):
        nodes.append({
            'name': obj['name'],
            'image': obj['image'],
            'group': idx + offset,
        })
    return nodes


# Local Data
tools = get_object(open('./data/tools.csv').read())
capabilities = get_object(open('./data/capabilities.csv').read())
services = get_object(open('./data/services.csv').read())

# -- or --

# # Google Spreadsheet (publicly viewable spreadsheet)
# tools_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSo5F3scO-IsXqffA23snCp3GqVpJdi7LFYfglwVDY82s5TiwB8lXkIoeXWAVmX6QBcLhoap6PTT0af/pub?gid=0&single=true&output=csv'  # noqa
# tools = get_object(requests.get(tools_url).content.decode('utf-8'))
# capabilities_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSo5F3scO-IsXqffA23snCp3GqVpJdi7LFYfglwVDY82s5TiwB8lXkIoeXWAVmX6QBcLhoap6PTT0af/pub?gid=1665220217&single=true&output=csv'  # noqa
# capabilities = get_object(requests.get(capabilities_url).content.decode('utf-8'))
# services_url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSo5F3scO-IsXqffA23snCp3GqVpJdi7LFYfglwVDY82s5TiwB8lXkIoeXWAVmX6QBcLhoap6PTT0af/pub?gid=1267609835&single=true&output=csv'  # noqa
# services = get_object(requests.get(services_url).content.decode('utf-8'))

nodes = get_nodes(tools, offset=0) + get_nodes(services, offset=len(tools))
node_names = [n['name'] for n in nodes]
links = []
for capability in capabilities:
    links.append({
        'source': node_names.index(capability['tool']),
        'target': node_names.index(capability['ability']),
        'value': 1,
    })

output = json.dumps({
    'nodes': nodes,
    'links': links,
})

with open('graph.json', 'w') as fp:
    fp.write(output)
