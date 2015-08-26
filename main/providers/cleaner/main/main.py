#!/usr/bin/env python

import StringIO, sys, os
from settings import *

# paas installer

try:
	from fabric.api import *
except ImportError, e:
	print "\n\nPlease install fabric first ."
	sys.exit(1)

env.user = OPENSTACK_ADMIN_AUTH['user']
env.password = OPENSTACK_ADMIN_AUTH['password']
env.hosts = [OPENSTACK_ADMIN_AUTH['host']]

hostuidBuffer = StringIO.StringIO()
current_dir = os.getcwd()

def queryHostUUIDByHostIP(ipaddr):
	hostUID = run('source keystonerc_admin;nova list | grep \
		"'+ipaddr+'" | awk -F "|" "{print $2}"', shell=False,
												stdout=hostuidBuffer)
	return hostUID

def go():
	run('source keystonerc_admin;nova rebuild ' + NODE1 +' '+ CC_IMAGEUID + ' --poll')
	run('source keystonerc_admin;nova rebuild ' + NODE2 +' '+ CC_IMAGEUID + ' --poll')
	run('source keystonerc_admin;nova rebuild ' + NODE3 +' '+ CC_IMAGEUID + ' --poll')
	run('source keystonerc_admin;nova rebuild ' + NODE4 +' '+ CC_IMAGEUID + ' --poll')
	run('source keystonerc_admin;nova rebuild ' + NODE5 +' '+ CC_IMAGEUID + ' --poll')
	run('source keystonerc_admin;nova rebuild ' + BOC +' '+ CC_IMAGEUID + ' --poll')
	os.system('fab -f f2cs_reconfig.py go')

