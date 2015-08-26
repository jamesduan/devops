#!/usr/bin/env python

import os, sys, json

import time

from settings import *
from fabric.colors import *

def verifyaddedRole():
	
	node_result = os.popen('knife search "node"').read()
	boc_result = os.popen('knife search "boc"').read()
	print node_result, boc_result
	gotit = []
	nodes = []
	for key, val in HOST_IPS.items():
		if 'opsserver' not in key:

			nodes.append(key)
			if key in node_result or key in boc_result:
				gotit.append(True)
	#print nodes, gotit
	if len(nodes) == len(gotit):
		print "verify added nodes complete!"
		return True

print red("\nPrepare chef server ...")
print " waiting for 60 seconds..."
time.sleep(60)

print red("\n\nchef-server reconfigure...\n\n")

try:
	#for key,val in HOST_IPS.items():
	#	if key == 'opsserver':
			
			#os.system('sshpass -p magima.1 ssh root@'+ val['bindPublicIP'] +' chef-server-ctl reconfigure')
			#print "\ncopying pem to workstation...\n"
			#os.system('sudo sshpass -p magima.1 scp root@' + key + ':' + ADMIN_PEM + ' ' + DEST_DIR)
			#os.system('sudo sshpass -p magima.1 scp root@' + key + ':' + CHEF_VALIDATE_PEM + ' ' + DEST_DIR)
	
	# valide key for knife
	os.system('sudo fab -f fabfile.py go')
	
	#os.system('fab -f fabfile.py go')
	print "\n\n chmod to other read...\n\n"
	os.system('sudo chmod o+r -R /etc/chef-server/')
	
	os.chdir('../../../juarez/')
	print "\n\n link node to server...\n\n"
	for key,val in DOMAINS.items():
		if 'opsserver' not in key:
			#print key['bindPublicIP']
			os.system('knife bootstrap ' + key + ' -x ' + BOOTSTRAP_AUTH['user'] + ' -P ' + BOOTSTRAP_AUTH['password'])
	
	print "list nodes..."
	os.system('knife node list')
	
	print "\n\n install gem i a box \n\n"
	os.chdir('./gems')
	
	os.system('sudo /opt/chef-server/embedded/bin/gem install geminabox --local')
	
	print "\n\n deploy go...\n\n"
	os.chdir('../scripts')
	if os.system('./deploy role/orc_null.json') is not 0:
		print "exec : add role list : orc_null error."
		sys.exit(1)
	# post verify 
	while(1):
		if verifyaddedRole():
			break

except KeyboardInterrupt, e:
	print "Exit by user cancel.", e
	sys.exit(1)
except OSError, e:
	print e
	sys.exit(1)
#except Exception, e:
#	print "Abort with a error occurred."
#	sys.exit(1)

