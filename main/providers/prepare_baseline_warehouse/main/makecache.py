
from fabric.api import *
from settings import *

for hostname, ip in HOST_IPS.items():
	if 'opsserver' not in hostname:
		env.hosts.append(hostname)

env.user = 'root'
env.password = 'magima.1'

def go():
	sudo('yum clean all; yum makecache')

