# encoding:utf8

import json, sys

NODES = []
with open('../../../configs/domain.json', 'r') as f:
	domain_d =f.read()

with open('../../../configs/host_ip.json', 'r') as f:
	host_ips = f.read()

with open('../../../configs/.secret', 'r') as f:
	secret_d = f.read()

USERNAME = secret_d.split(':')[0]
PASSWORD = secret_d.split(':')[1]

HOST_IPS = json.loads(host_ips)

DOMAINS = json.loads(domain_d)
for key,val in DOMAINS.items():
	NODES.append(key)
if not NODES:
	print "ERROR: host name empty!"
	sys.exit()

DOMAIN_NAME = DOMAINS[NODES[0]].split('.')[1]

CONF_TEMPLATE_PATH='template/named.conf.temp'

CONF_FILE_PATH = 'generate_files/named.conf'

RFC1912_TEMP_PATH = 'template/named.rfc1912.zones.temp'
RFC1912_PATH = 'generate_files/named.rfc1912.zones'

ZONES_FILE_TEMP_PATH = 'template/xxxx.com.temp'
ZONES_FILE_PATH = 'generate_files/' + DOMAIN_NAME + '.com'

RESOLV_CONF_TEMP = 'template/resolv.conf.temp'
RESOLV_CONF = 'generate_files/resolv.conf'

NAMED_CONF = {
	'listen_ip' : 'any',
	'allow_query_ip': 'any',
	'forwarders_ip' : '10.0.0.21',
}

DEST_DIR = '/etc'
NAMED_DIR = '/var/named/'

NAMED_TEMPLATE_FILES = 'generate_files/named.*'
ZONE_FILES = 'generate_files/*.zone'
