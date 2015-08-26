import StringIO, sys

from fabric.api import *
from fabric.colors import green
from settings import *

for hostname, ip in HOST_IPS.items():
	if 'opsserver' in hostname:
		env.hosts.append(hostname)

env.user = USERNAME
env.password = PASSWORD

status_buffer = StringIO.StringIO()

def doPreverify():
	status_list = []
	status = sudo('/opt/lampp/xampp status', shell=False,
		stdout=status_buffer)

	for line in status.split('\n'):
		if "Apache_is_running." == line.strip().replace(' ', '_'):
			print green("passed!")
			return True
	return False

def go():

	if not doPreverify():
		sudo("/opt/lampp/xampp startapache")

	sudo('createrepo /opt/lampp/htdocs/rpms --update')


