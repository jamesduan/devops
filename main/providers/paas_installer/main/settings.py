import json

with open('../../../configs/host_ip.json', 'r') as f:
	j = f.read()

with open('../../../configs/.secret', 'r') as f:
	secret_d = f.read()
USERNAME = secret_d.split(':')[0]
PASSWORD = secret_d.split(':')[1]

HOST_IPS = json.loads(j)

