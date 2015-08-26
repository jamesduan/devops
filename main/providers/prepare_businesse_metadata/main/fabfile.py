
from fabric.api import *
from settings import *
import datetime

for key, val in HOST_IPS.items():

	if 'opsserver' not in key:
		env.hosts.append(val['bindPublicIP'])

env.user = USERNAME
env.password = PASSWORD

def go():

	sudo('chef-client -o recipe["testonly"] 2>&1 | tee ~/testonly.log')
	sudo('chef-client 2>&1 | tee ~/prepare_metadata_'+str(datetime.datetime.now()).split('.')[0]+'_.log')

