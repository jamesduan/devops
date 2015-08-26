
import os, StringIO

from fabric.api import *
from fabric.colors import red

from settings import HOST_IP_CONFIG_PATH, ORC_PAAS_CONFIG_PATH, USERNAME, PASSWORD, MYSQL_BASEDIR
from common import hosts

# check config files 

if not os.path.exists(HOST_IP_CONFIG_PATH):
	print "PLEASE CHECK YOUR CONFIGURATION FILE:{host_ip_json} AND DO AGAIN."\
		.format(host_ip_json = HOST_IP_CONFIG_PATH)
	sys.exit(1)
else:
	print "CHECK CONFIGURATION FILE:{host_ip_json} PASSED".format(host_ip_json = HOST_IP_CONFIG_PATH)

if not os.path.exists(ORC_PAAS_CONFIG_PATH):
	print "PLEASE CHECK YOUR CONFIGURATION FILE:{orc_paas_json} CAN BE FOUND IN PATH."\
		.format(orc_paas_json = ORC_PAAS_CONFIG_PATH)
	sys.exit(1)
else:
	print "CHECK CONFIGURATION FILE:{orc_paas_json} PASSED.".format(orc_paas_json=ORC_PAAS_CONFIG_PATH)

print "\ndone.\n"

print hosts
env.hosts = hosts
env.user = USERNAME
env.password = PASSWORD

check_buffer = StringIO.StringIO()

def check_mysql_files():
	# check basedir
	status_code = run('if [ -d "'+MYSQL_BASEDIR+'" ];then echo "1" ; else echo "2"; fi',
		shell=False, stdout=check_buffer)
	if status_code == "1":
		with cd(MYSQL_BASEDIR):
			run('ls -lrt ./data')
			run('ls -lrt ./bin')
			run('ls -lrt ./bin/mysql')
			run('ls -lrt ./bin/mysqld')
	if status_code =="2" :
		print red('mysql basedir is not exists!')
		sys.exit(1)

def go():
	check_mysql_files()

