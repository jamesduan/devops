import json

with open('../../../configs/host_ip.json', 'r') as f:
	j = f.read()

HOST_IPS = json.loads(j)

with open('../../../configs/domain.json', 'r') as f:
	dj = f.read()

DOMAINS = json.loads(dj)

with open('../../../configs/.secret', 'r') as f:
	secret_content = f.read()

USERNAME = secret_content.split(':')[0]
PASSWORD = secret_content.split(':')[1]

TEMPLATE_FILE = 'template/hosts.temp'
TEMPLATE_FILE_P = 'template/hosts.p.temp'

LFILEPATH = 'hosts'
RFILEPATH = '/etc/hosts'

ADDITIONAL_DISK = '/dev/vdb'
DATA_DIRECTORY = '/var/magima/'

# /var/magima/logs/pqa/zabbix/
ZABBIX_LOG = 'logs/pqa/zabbix/'.join([DATA_DIRECTORY])

ZABBIX_AGENT_TPL = 'template/zabbix_agentd.conf'

