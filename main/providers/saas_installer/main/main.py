#!/usr/bin/env python

import os

# paas installer
print "execute saas installer..."
current_dir = os.getcwd()
print "prepareing runlist..."
os.chdir('../../../juarez/scripts/')

try:
	os.system('./addrole2runlist role/orc_saas.json')
	
	print "exec chef-client"
	os.chdir(current_dir)
	print "First setting up saas."
	os.system('fab -f fabfile.py go')

except KeyboardInterrupt, e:
	print "Exit by user cancel.", e
	sys.exit(1)

