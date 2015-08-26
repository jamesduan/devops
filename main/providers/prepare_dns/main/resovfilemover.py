
from fabric.api import *

from settings import *

for key,val in HOST_IPS.items():
	env.hosts.append(val['bindPublicIP'])

env.user = USERNAME
env.password = PASSWORD

def go():
	#put(RESOLV_CONF, DEST_DIR)
	put(RESOLV_CONF, '/tmp')
	sudo('cp -v /tmp/resolv.conf ' + DEST_DIR)
	sudo('rm -fv /tmp/resolv.conf')

