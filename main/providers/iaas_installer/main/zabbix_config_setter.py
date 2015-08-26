# encoding:utf8

import StringIO

from fabric.api import *
from settings import *

from mako.template import Template

for key, val in HOST_IPS.items():
	env.hosts.append(val['bindPublicIP'])

env.user = USERNAME
env.password = PASSWORD

hostname_buffer = StringIO.StringIO()

def current_hostname():
	hostname = sudo('hostname', shell=False,
					stdout=hostname_buffer)
	return hostname

def go():
	#put(ZABBIX_AGENT_TPL, '/etc/zabbix/')
	put(ZABBIX_AGENT_TPL, '~/zabbix_agentd.conf')
	sudo('cp ~/zabbix_agentd.conf /etc/zabbix/zabbix_agentd.conf')

	sudo('sed -i -e "s/^Hostname=.*/Hostname=new_pqa_'+current_hostname()+'/g" /etc/zabbix/zabbix_agentd.conf')

	sudo('ls /etc/zabbix/zabbix_agentd.conf')
	
	

