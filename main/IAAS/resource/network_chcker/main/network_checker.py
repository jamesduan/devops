# encoding:utf8

import json

from fabric.api import *
from settings import *

# define user and password for host list
env.user = DEFAULT_USER
env.password = DEFAULT_PASSWD

# read config file for host list
with open(CONF_FILE, 'r') as f:
	jsondata =  json.loads(f.read())

host_list = []
for key, val in jsondata.items():
	host_list += [ str(ip) for ip in val if str(ip) != '' ]

env.hosts = host_list

# action task
def _ping_host():

	for i in env.hosts:
		if not i or i == u'':
			continue
		print local('ping ' + i + ' -c 5')
		print run('ping ' + i + ' -c 5')

def network_check():
	_ping_host()


