#!/usr/bin/env python

import os, sys
from settings import *

print "\nPrepareing metadata...\n"
print "\ngenerate metadata xml files.\n"

current_dir = os.getcwd()

try:
	print "\n Preparing zookeeper service ..."
	os.chdir(current_dir)
	os.system('fab -f fabfile.py go')
	print "\nZookeeper setup ok!\n"

	import_nodes = []

	for key, val in HOST_IPS.items():

		if 'opsserver' not in key and key is not "boc":

			import_nodes.append(key)

	os.chdir('./centralmeta')
	print "exec do generate_instance."
	os.system('./do_generate_instance.sh -m idc -c idc')

	os.chdir('./install_xml_files')
	os.system('sudo yum -y install java-1.7.0-openjdk.x86_64')
	os.system('./do_import_zkinfo.sh {node} 2181 origin'.format(node=import_nodes[0]))

except KeyboardInterrupt, e:
	print "EXIT by user cancel." , e
	sys.exit(1)


