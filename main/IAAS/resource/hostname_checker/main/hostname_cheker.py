# encoding:utf8

import json, StringIO, os

from fabric.api import *
from fabric.colors import *

from settings import *
from host import Host

''' init fabric env variables '''
# define user and password for host list
env.user = DEFAULT_USER
env.password = DEFAULT_PASSWD

# read config file for host list
with open(CONF_FILE, 'r') as f:
	jsondata =  json.loads(f.read())

ip_list = []
hosts = []

for key, val in jsondata.items():
	host = Host()
	ips = [ str(ip) for ip in val if str(ip) != '' ]
	ip_list += ips
	host.ipaddress = ips
	host.hostname = key
	hosts.append(host)

env.hosts = ip_list
#############################
# action task
hostname_stdout = StringIO.StringIO()
hosts_file_stdout = StringIO.StringIO()
ipaddr = StringIO.StringIO()

#for host in hosts:
#	print host.hostname, host.ipaddress
# report 
if os.path.exists(REPORT_FILE_NAME):
	os.system('cat "" > ' + REPORT_FILE_NAME)
f = open(REPORT_FILE_NAME, 'a+')

@task
def check():
	hostname_check()

def hostname_check():
	hostname_output_infos = run('grep "HOSTNAME" /etc/sysconfig/network',
								shell=False,stdout=hostname_stdout)
	
	tmp_hostname = hostname_output_infos.split('=')[1]
	ipaddr_infos = run("PATH=$PATH:/sbin/;ifconfig | grep 'inet addr' | grep -v '127.0.0.1' | awk -F ':' '{print $2}' | awk -F ' ' '{print $1}'", shell=False, stdout=ipaddr)
	tmp_ip = ipaddr_infos.split('\n')[0]
	host = Host()
	tmp_host = host.queryHostByHostname(hosts, hostname = tmp_hostname)
	f.write("find hostname and ipaddr is :" + tmp_hostname + ',' + tmp_ip + "\n")
	print yellow(tmp_hostname + ' ' + tmp_ip + '\n')

	if tmp_host:
		if tmp_ip not in tmp_host.ipaddress:
			print red("check not passed!\n")
			f.write("check not passed!\n")
		else:
			print green("check passed!\n")
			f.write('check passed!\n')
	else:
		print red("unkown host! please check your hostname macthed with CMBD metadata!")
		f.write('not metched hostname!\n')

