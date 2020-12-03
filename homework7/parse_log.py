import re
import json

json_data = {"get": 0, "all_requests": 0, "post": 0, 'put': 0, "delete": 0, "error": [], "top_ip": {}}

regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)'
with open("nginx.log") as file_handler:
    for line in file_handler:
        json_data['all_requests'] += 1
        var = (re.match(regex, line).groups())
        if var[2][:3] == 'GET':
            json_data['get'] += 1
        elif var[2][:4] == 'POST':
            json_data['post'] += 1
        elif var[2][:3] == 'PUT':
            json_data['put'] += 1
        elif var[2][:6] == 'DELETE':
            json_data['delete'] += 1
        if var[3] != '200':
            a = var[2].split()
            json_data["error"].append(re.search(r'^[^ ]+', var[2]).group() + ', ' + var[2].split()[1] + ', ' + var[3])
        if var[0] in json_data["top_ip"].keys():
            json_data['top_ip'][var[0]] += 1
        else:
            json_data['top_ip'][var[0]] = 1
        list_top_ip = list(json_data['top_ip'].items())
        list_top_ip.sort(key=lambda i: i[1], reverse=True)
        if len(list_top_ip) > 10:
            list_top_ip = list_top_ip[:10]
        json_data['top_ip'] = dict(list_top_ip)


with open('result.json', 'w') as f:
    json.dump(json_data, f, indent=4)
