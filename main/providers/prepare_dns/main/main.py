#!/usr/bin/env python

import time, os

from mako.template import Template

from settings import *

# prepare DNS server

def prepareNamedConfFile():
	
	print "Prepare Dns..\n"
	
	t = Template(filename=CONF_TEMPLATE_PATH)
	template_buffer = t.render(listen_ip = NAMED_CONF['listen_ip'],
								allow_query_ip = NAMED_CONF['allow_query_ip'],
								forwarders_ip = NAMED_CONF['forwarders_ip'])
	
	print template_buffer
	
	with open(CONF_FILE_PATH, 'w+') as f:
		f.write(template_buffer)
	
	time.sleep(1)
	print "\ndns named.conf file generate ok!\n"


def prepareNamedRFCFile():

	print "init named.rfc1912.zones"

	t = Template(filename=RFC1912_TEMP_PATH)
	template_buffer = t.render()
	#print template_buffer

	rfccontents = template_buffer
	for key, val in HOST_IPS.items():
		rfccontents += 'zone "'+key+'" IN {\n' + '\ttype master;\n' + '\tfile '+'"'+key+'.zone";\n' + '\tallow-update { none; };\n' + '};\n'

	print rfccontents
	with open(RFC1912_PATH, 'w+') as f:
		f.write(rfccontents)

	time.sleep(1)
	print "Prepared named.rfc1912.zones ok!"

def prepareZonesFile():
	print "init zones files"
	master_ip = ''
	for key,val in HOST_IPS.items():
		master_ip = val['bindPrivateIP'][0]

		t = Template(filename=ZONES_FILE_TEMP_PATH)
		template_buffer = t.render(domain_name = key, master_ip = master_ip)
		print template_buffer

		with open("generate_files/" + key + '.zone', 'w+') as f:
			f.write(template_buffer)


	#for key,val in HOST_IPS.items():
	#	with open(ZONES_FILE_PATH, 'a+') as f:
	#		if key == 'opsserver':
	#			f.write('\ndns-server\tA\t' + val['bindPrivateIP'][0])
	#			f.write('\nchef-server\tA\t' + val['bindPrivateIP'][0])
	#		else:
	#			f.write('\n' + key + '\tA\t' + val['bindPrivateIP'][0])
	time.sleep(1)
	print "ok!"

	print "init resolv.conf"
	for key,val in HOST_IPS.items():

		if 'opsserver' in key:
			master_ip = val['bindPrivateIP'][0]

	t = Template(filename=RESOLV_CONF_TEMP)
	template_buffer = t.render(nameserver_ip = master_ip)
	print template_buffer
	with open(RESOLV_CONF, 'w+') as f:
		f.write(template_buffer)
	print "ok!"

def go():
	print "copy to dir..."
	time.sleep(1)
	os.system('fab -f fabfile.py go')
	os.system('fab -f resovfilemover.py go -P')

	#os.system('sudo cp generate_files/named.* ' + DEST_DIR)
	#os.system('sudo cp ' + RESOLV_CONF + ' ' + DEST_DIR)
	#os.system('sudo cp generate_files/*.com ' + NAMED_DIR)
	#os.system('sudo chown named:named -R ' + NAMED_DIR)
	#os.system('sudo /etc/init.d/named restart')
	print "ok!"

def check():
	print "check dns..."
	os.system('ping -c 5 dns-server.' + DOMAIN_NAME + '.com')
	os.system('nslookup dns-server.' + DOMAIN_NAME + '.com')

if __name__ == "__main__":
	try:

		prepareNamedConfFile()
		prepareNamedRFCFile()
		prepareZonesFile()
		go()

	except KeyboardInterrupt, e:
		print "Exit by user cancel.", e
		sys.exit(1)

	except Exception, msg:
		print "Abort with a Error occurred. ", msg
		sys.exit(1)

