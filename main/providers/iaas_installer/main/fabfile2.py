# encoding:utf8

import sys
from fabric.api import *
from settings import *

import StringIO

for key, val in HOST_IPS.items():
	if 'opsserver' not in key:
		env.hosts.append(val['bindPublicIP'])

env.user = USERNAME
env.password = PASSWORD

df_buffer = StringIO.StringIO()

def preVerify():

	result = sudo('df | grep ' + ADDITIONAL_DISK, shell=False,
		stdout=df_buffer)
	if result:
		print "{disk} already mounted.".format(disk=ADDITIONAL_DISK)
		sys.exit(1)
	else:
		print "check {disk} not found , begin mount additional disk.".format(disk=ADDITIONAL_DISK)

def postVerify():

	result = sudo('df | grep ' + ADDITIONAL_DISK, shell=False,
		stdout=df_buffer)
	if result:
		print "do post verify is passed."
	else:
		print "error: not mount complte. please check.exit"
		sys.exit(1)

def go():

	preVerify()
	sudo('mkdir -p ' + DATA_DIRECTORY)
	sudo('mkdir -p ' + ZABBIX_LOG)
	#sudo('mkfs.ext4 ' + ADDITIONAL_DISK)
	#sudo('mount ' + ADDITIONAL_DISK + ' ' + DATA_DIRECTORY)
	#sudo('echo "'+ADDITIONAL_DISK+'\t/var/magima\text4\tdefaults\t0\t0" >> /etc/fstab')

	postVerify()

