
from settings import HOST_IPS, IP_ROLES

def getPublicIpByPrivateIp(privateIp=None):
	if privateIp == None:
		return None
	else:
		for host, ips in HOST_IPS.items():
			if 'opsserver' not in host and privateIp in ips['bindPrivateIP']:
				return ips['bindPublicIP']

apigw_host_public = []

for ip,roles in IP_ROLES.items():
	if "Production_Access_Normal_APIGW" in roles:
		apigw_host_public.append(getPublicIpByPrivateIp(ip))

print apigw_host_public

