# encoding:utf8

class Host(object):

	def __init__(self, hostname = None, ipaddress=None, dns_name = None):
		self.hostname = hostname
		self.ipaddress = ipaddress
		self.dns_name = dns_name

	def queryHostByIp(self, hosts = [], ipaddr=""):
		for host in hosts:
			if host.ipaddress == ipaddr:
				return host
			else:
				return None
	
	def queryHostByHostname(self, hosts = [], hostname=""):
		for host in hosts:
			if host.hostname == hostname:
				return host
