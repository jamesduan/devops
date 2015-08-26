#!/usr/bin/env python

import os
import time
import sys
import scanner

from settings import *
from mako.template import Template

def getDomainNameByHostName(hostname):

	for key, val in DOMAINS.items():
		if hostname in key:
			return val

def prepareHostName():
	
	print "prepare hostname..."
	n = 1
	hosts_contents = ''
	hosts_contents_publicIP = ''

	for key, val in HOST_IPS.items():

		if 'opsserver' not in key:

			hosts_contents += '\n' + val['bindPrivateIP'][0] + '\t' + key + ' chef-client' + str(n)
		else:
			hosts_contents += '\n' + val['bindPrivateIP'][0] + '\t' + key + ' chef-server repo-server dns-server'

		if 'opsserver' not in key:

			hosts_contents_publicIP += '\n' + val['bindPublicIP'] + '\t' + key + ' chef-client' + str(n)
		else:
			hosts_contents_publicIP += '\n' + val['bindPublicIP'] + '\t' + key + ' chef-server repo-server dns-server'

		print "change " + val['bindPublicIP'] + ' hostname.'
		os.system('sshpass -p '+PASSWORD+' ssh '+USERNAME+'@' + val['bindPublicIP'] + ' sudo hostname ' + key)
		os.system('sshpass -p '+PASSWORD+' ssh '+USERNAME+'@' + val['bindPublicIP'] + ' sudo sed -i -e s/HOSTNAME=.*/HOSTNAME='+key+'/g /etc/sysconfig/network')
		n+=1

	#print hosts_contents

	with open(TEMPLATE_FILE, 'w+') as f:
		f.write('127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4' \
			+ hosts_contents)

	with open(TEMPLATE_FILE_P, 'w+') as f:
		f.write('127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4' \
			+ hosts_contents_publicIP)

	os.system('cp ' + TEMPLATE_FILE_P + ' hosts')
	os.system('sudo cp hosts ' + RFILEPATH)
	os.system('fab -f fabfile.py go')
	print "\nhost rebooting...please wait for 1 minute..."
	time.sleep(70)
	## check connect
    # scanner.getScanState(ip='127.0.0.1', port='22')

	print "\ncheck connect..\n"
	for key,val in HOST_IPS.items():
		state = ()

		try:
			state = scanner.getScanState(ip=val['bindPublicIP'].encode('utf-8'), port='22')
		except Exception,e :
			print e

		try:
			if not state:
				print "Scan {host} Failure".format(host=val['bindPublicIP'].encode('utf-8'))
				print "continue scan port!"
				while(1):
					state = scanner.getScanState(ip=val['bindPublicIP'].encode('utf-8'), port='22')
					if state:
						break

			if state[0] is "down" or state[0] is "unkown" or state[0] is "skipped":
				print "can not access host".join([val['bindPublicIP']])
				sys.exit(1)

			if state[1] is "closed":
				print "host {host} 22 port is not open.".format(host = val['bindPublicIP'])
				sys.exit(1)

			print "check {host} passed!".format(host=val['bindPublicIP'].encode('utf-8'))

		except KeyError, err:
			print "check network unkown host:", err
			sys.exit(1)

	if os.system('fab -f fabfile2.py go') is 1:
		print "already done."
	elif os.system('fab -f fabfile2.py go') != 1 and os.system('fab -f fabfile2.py go') != 0:
		print "error occurred."

try:
	prepareHostName()
except KeyboardInterrupt, e:
	print "Exit by user cancel.", e
	sys.exit(1)
except Exception, e:
	print "Abort with a error occurred.", e
	sys.exit(1)

