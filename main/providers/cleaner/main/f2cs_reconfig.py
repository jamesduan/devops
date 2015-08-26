#!/usr/bin/env python

import StringIO, sys, os
from settings import *

# paas installer
try:
	from fabric.api import *
except ImportError, e:
	print "\n\nPlease install fabric first ."
	sys.exit(1)

env.user = OPSSERVER['user']
env.password = OPSSERVER['password']
env.hosts = [OPSSERVER['host']]

def go():
	sudo("chef-server-ctl cleanse")


