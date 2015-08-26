
import json

HOST_IP_CONFIG_PATH = '../../../configs/host_ip.json'
ORC_SAAS_CONFIG_PATH = '../../../juarez/scripts/role/orc_saas.json'

with open(HOST_IP_CONFIG_PATH, 'r') as f:
	json_contents = f.read()

HOST_IPS = json.loads(json_contents)
#print HOST_IPS

with open(ORC_SAAS_CONFIG_PATH, 'r') as f:
	jj2 = f.read()

IP_ROLES = json.loads(jj2)
#print IP_ROLES

with open('../../../configs/.secret', 'r') as f:
	secret_d = f.read()

USERNAME=secret_d.split(':')[0]
PASSWORD=secret_d.split(':')[1]

APIGW_BASEDIR='/opt/magima/apigw'






