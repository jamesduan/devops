
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
mongodb_master_host = []
tfs_host = []

for ip,roles in IP_ROLES.items():

		if "Production_Persistence_Normal_Mysql_Master" in roles \
			or "Production_Persistence_Normal_Mysql_Slave" in roles:
			hosts.append(getPublicIpByPrivateIp(ip))

		if "Production_Persistence_Normal_Mysql_Master" in roles:
			mysql_master_host.append(getPublicIpByPrivateIp(ip))
		
		if "Production_Persistence_Normal_Mysql_Master" in roles \
			or "Production_Persistence_Normal_Mysql_Slave" in roles:
			private_ips.append(ip)

		if "Production_Persistence_Normal_MongoDB_Master" in roles:
			mongodb_master_host.append(getPublicIpByPrivateIp(ip))

		if "Production_Persistence_Normal_TFS" in roles:
			tfs_host.append(ip)

