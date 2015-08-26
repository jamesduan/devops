
import tempfile

from fabric.api import *
from settings import *

for key ,val in HOST_IPS.items():
	if 'opsserver' in key:
		env.hosts.append(val['bindPublicIP'])

env.user = USERNAME
env.password = PASSWORD

def go():
	#put(NAMED_TEMPLATE_FILES, DEST_DIR)
	put(NAMED_TEMPLATE_FILES, '/tmp')
	sudo('cp -v /tmp/named.* ' + DEST_DIR)

	#put(RESOLV_CONF, DEST_DIR)
	#put(ZONE_FILES, NAMED_DIR)
	put(ZONE_FILES, '/tmp')
	sudo('cp -v /tmp/*.zone ' + NAMED_DIR)
	sudo('chown named:named -R ' + NAMED_DIR)
	sudo('/etc/init.d/named restart')
	
	sudo('chkconfig named on')
	sudo('chkconfig --list')

