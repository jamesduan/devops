
from settings import HOST_IPS, IP_ROLES

def getPublicIpByPrivateIp(privateIp=None):
	if privateIp == None:
		return None
	else:
		for host, ips in HOST_IPS.items():
			if 'opsserver' not in host and privateIp in ips['bindPrivateIP']:
				return ips['bindPublicIP']

hosts = []
mysql_master_host = []
private_ips = []

mongo_hosts_public = []
mongo_master_host_public = []

mongo_hosts_private = []

for ip,roles in IP_ROLES.items():

		if "Production_Persistence_Normal_Mysql_Master" in roles \
			or "Production_Persistence_Normal_Mysql_Slave" in roles:
			hosts.append(getPublicIpByPrivateIp(ip))

		if "Production_Persistence_Normal_Mysql_Master" in roles:
			mysql_master_host.append(getPublicIpByPrivateIp(ip))
		
		if "Production_Persistence_Normal_Mysql_Master" in roles \
			or "Production_Persistence_Normal_Mysql_Slave" in roles:
			private_ips.append(ip)

		if "Production_Persistence_Normal_MongoDB_Master" in roles \
			or "Production_Persistence_Normal_MongoDB_Slave" in roles:
			mongo_hosts_public.append(getPublicIpByPrivateIp(ip))

		if "Production_Persistence_Normal_MongoDB_Master" in roles:
			mongo_master_host_public.append(getPublicIpByPrivateIp(ip))

		if "Production_Persistence_Normal_MongoDB_Master" in roles \
			or "Production_Persistence_Normal_MongoDB_Slave" in roles:
			mongo_hosts_private.append(ip)

