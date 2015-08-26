# encoding:utf8

from fabric.api import *
from settings import *

for key, val in HOST_IPS.items():
	env.hosts.append(val['bindPublicIP'])

env.user = USERNAME
env.password = PASSWORD

def go():
	put(TEMPLATE_FILE, RFILEPATH)
	sudo('rm -rvf /etc/yum.repos.d/*')
	put('magima.repo', '~/magima.repo')
	sudo('cp -v ~/magima.repo /etc/yum.repos.d/')
	run('yum clean all ;yum makecache')
	# zabbix 

