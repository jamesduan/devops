import json

with open('../../../configs/host_ip.json', 'r') as f:
	j = f.read()

HOST_IPS = json.loads(j)

with open('../../../configs/.secret', 'r') as f:
	s_c = f.read()

USERNAME=s_c.split(':')[0]
PASSWORD=s_c.split(':')[1]

