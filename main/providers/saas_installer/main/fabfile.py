
from fabric.api import *
from settings import *
import datetime

for hostname, ips in HOST_IPS.items():
	if 'opsserver' not in hostname:
		env.hosts.append(ips['bindPublicIP'])

env.user = USERNAME
env.password = PASSWORD

def go():
	sudo('chef-client 2>&1 | tee ~/SAAS_'+str(datetime.datetime.now())+'_ERR.log')

