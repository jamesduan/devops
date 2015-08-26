#!/usr/bin/env python

import os, sys

from settings import *

# paas installer
description = "\nexecute paas installer provider...\n"
print "\nPrepareing runlist"

try:
	current_dir = os.getcwd()
	os.chdir('../../../juarez/scripts/')
	# remove all role from runlist first
	os.system('./addrole2runlist role/orc_paas.json')
	print "\nExecute chef-client\n"
	os.chdir(current_dir)
	print "\nFirst to setup.\n"
	os.system('fab -f fabfile.py go')
	#print "\nSecond setup.\n"
	#os.system('fab -f fabfile.py go')

except OSError, e:
	print >> sys.stderr, "\n\n" + description
	sys.exit(1)

except KeyboardInterrupt, e:
	print >> sys.stderr, "\n\n" + description
	sys.exit(1)

