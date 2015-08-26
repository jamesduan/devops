import json

with open('../../../configs/host_ip.json', 'r') as f:
	j = f.read()

HOST_IPS = json.loads(j)

with open('../../../configs/domain.json', 'r') as f:
	dj = f.read()

with open('../../../configs/.secret' , 'r') as f:
	secret_c = f.read()

USERNAME = secret_c.split(':')[0]
PASSWORD = secret_c.split(':')[1]

DOMAINS = json.loads(dj)

BOOTSTRAP_AUTH = {
	'user': 'root',
	'password': 'magima.1',
}

ADMIN_PEM = '/etc/chef-server/admin.pem'
CHEF_VALIDATE_PEM = '/etc/chef-server/chef-validator.pem'

DEST_DIR = '/etc/chef-server'

