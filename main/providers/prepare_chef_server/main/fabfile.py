
import tempfile

from fabric.api import *
from settings import HOST_IPS, CHEF_VALIDATE_PEM, DEST_DIR, ADMIN_PEM, USERNAME, PASSWORD

for key, val in HOST_IPS.items():
	if 'opsserver' in key:
		env.hosts.append(key)
		
env.user = USERNAME
env.password = PASSWORD

#temp_dir_path = tempfile.mkdtemp()

def go():
	
	sudo("chef-server-ctl reconfigure")
	get(ADMIN_PEM, DEST_DIR)
	get(CHEF_VALIDATE_PEM, DEST_DIR)

