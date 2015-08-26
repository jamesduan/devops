# encoding:utf8

import json, time, sys

from mako.template import Template

from DeployHandler import DeployHandler
from OrchestratorConfig import PROVIDER_TYPE, DOMAIN_FILE, HOST_IP_FILE
from role2deviceMapping import Role2DeviceManager
from role import RoleManager
from xmlcmdb_observer import XMLCMDBObserver
from colors import green, red
from util import getoutCurlyBraces
from target import DeployTargetManager
from deployschema import DeploySchemaManager
from OrchestratorConfig import CHEF_ROLE_CONFIG_FILE_PATH, ROBOTFRAMEWORK_DIR, \
	ENV_VARS_TEMPLATE_FILE, ORC_PAAS_FILE, ORC_SAAS_FILE, ORC_ZOO_FILE
from DeployHandler import DeployHandler

class DeployWorker(object):
	
	def __init__(self, startTime = None, stopTime = None,logger = None,
				bindDeploySchema = None, bindResources = []):

		self.start_time = startTime
		self.stop_time = stopTime
		self.logger = logger
		self.bind_deployschema = bindDeploySchema
		self.bind_resources = bindResources

	def verifySchemaAndResource(self):
		return None

	def getUniqHost(self):

		mappings = self.bind_deployschema.role2DeviceMappingList
		hostUIDS = [ mapping.hostUID for mapping in mappings ]
		hostUIDUniq = list(set(hostUIDS))
		return hostUIDUniq

	def gen_recipestr_4_targetnames(self, targetNames):
		recipestr = ''
		for name in targetNames:
			recipestr = recipestr + '"recipe[' + name + ']",'
		return recipestr[:-1]

	def init_config_files(self):
		print red('''
			INIT ROLE TO DEVICE MAPPING CONFIG FILE.
		''')
		# init paas
		print "Init role to device mapping file begin:"
		hostUIDUniqs = self.getUniqHost()
		r2dmM = Role2DeviceManager()
		roleM = RoleManager()
		xcobs = XMLCMDBObserver()
		# defin host role mapping dict
		host_paas_role = {}
		host_saas_role = {}
		zoo_role = {}

		for hostuid in hostUIDUniqs:
			# find role uid by host uid 
			# print hostuid
			roleUIDS = r2dmM.queryRoleByHostUID(hostuid)
			#print roleUIDS
			paas_roles = []
			saas_roles = []
			for roleuid in roleUIDS:
				role_name = roleM.queryRoleByUID(roleuid)
				if role_name in roleM.getPaasRoles():
					paas_roles.append(role_name)
				else:
					saas_roles.append(role_name)
			#print roles
			host = xcobs.getHostByUID(hostuid)
			host_ipaddr = host.findall('./Hardware/EthernetIF')[0].attrib['bindPrivateIP']
			#host_name = host.attrib['name']

			host_paas_role[host_ipaddr] = paas_roles
			host_saas_role[host_ipaddr] = saas_roles
			zoo_role[host_ipaddr] = ['Production_Persistence_Normal_Zookeeper']

		#print host_role

		pjsondata = json.dumps(host_paas_role)
		with open(ORC_PAAS_FILE, 'w+') as f:
			f.write(pjsondata)

		sjsondata = json.dumps(host_saas_role)
		with open(ORC_SAAS_FILE, 'w+') as f:
			f.write(sjsondata)

		zjsondata = json.dumps(zoo_role)
		with open(ORC_ZOO_FILE, 'w+') as f:
			f.write(zjsondata)

		print "count: %s" % len(hostUIDUniqs)
		print green("\nprepareing role<===>address json file ok!\n")

		''' 
			init chef role config file :
			include role define and target to role mapping.
			and then chef can use the config file that used ruby 
			lan written.
		'''

		print red("Init chef roles file begin:")
		dtm = DeployTargetManager()
		rm = RoleManager()
		dsmM = DeploySchemaManager()
		mappings = self.bind_deployschema.targetRoleMapping
		roleUIDs = [ getoutCurlyBraces(mapping.text.split(':')[1]) for mapping in mappings ]
		roleUIDs_uniq = list(set(roleUIDs))

		for roleUID in roleUIDs_uniq:
			roleName = rm.queryRoleByUID(roleUID)
			targetNames = dsmM.getTargetNamesByRoleUID(roleUID)
			if "openresty" in targetNames:
				targetNames.remove('openresty')
			if "rabbitmq-server" in targetNames:
				targetNames.remove('rabbitmq-server')
				targetNames.insert(0, 'rabbitmq')
			with open(CHEF_ROLE_CONFIG_FILE_PATH + roleName + '.rb' , 'w+') as f:
				f.write("name " + '"' + roleName + '"\n' \
						"description " + '"' + roleName +'"\n'\
						"run_list " + self.gen_recipestr_4_targetnames(targetNames))

		print "count: %s " % (len(roleUIDs_uniq))
		print green("preparing target===>role mapping config file ok!")

	def initdomain(self):
		print red('''
			INIT CONFIG FILES.
		''')
		domain_name = self.bind_deployschema.schema_name
		cmdbobserver = XMLCMDBObserver()
		domain_dict = {}
		host_ip_dict = {}

		for host in cmdbobserver.getHostlist():
			ipaddrs = {'bindPrivateIP' : []}
			ethernets = host.findall('./Hardware/EthernetIF')

			for ethernet in ethernets:
				if ethernet.attrib['bindPrivateIP']:
					ipaddrs['bindPrivateIP'].append(ethernet.attrib['bindPrivateIP'])
				if ethernet.attrib['bindPublicIP']:
					ipaddrs['bindPublicIP'] = ethernet.attrib['bindPublicIP']
			host_ip_dict[host.attrib['name']] = ipaddrs
			domain_dict[host.attrib['name']] = host.attrib['name'] + '.' + domain_name + '.com'

		print "init domain name and hostname config... \n"
		jsondata = json.dumps(domain_dict)
		with open(DOMAIN_FILE, 'w+') as f:
			f.write(jsondata)
		time.sleep(1)

		print "init ip node..."
		j = json.dumps(host_ip_dict)
		with open(HOST_IP_FILE, 'w+') as f:
			f.write(j)
		time.sleep(1)

	def getHostNameByPrivateIp(privateIp=None, HOST_IPS={}):
		if privateIp == None or HOST_IPS == {}:
			return None
		else:
			for host, ips in HOST_IPS.items():
				if host != 'opsserver' and privateIp in ips['bindPrivateIP']:
					return host
	
	def getHostStr(self, host_list = [], hosts_ip_dict={}):

		hosts_str = ""
		if host_list == [] or host_list == None or hosts_ip_dict =={} or hosts_ip_dict == None:
			return None
		else:
			for ip in host_list:
				hosts_str += "\t" + "'" + \
					self.getHostNameByPrivateIp(ip, hosts_ip_dict)+ "'" + ", "

		return hosts_str
	

	# robotframework_PQA/testenv_vars.py
	def generate_env_vars(self):

		# define vars for template file.
		target_name = self.bind_deployschema.schema_name
		outer_hosts_ip_str, inner_hosts_ip_str = "", ""
		persistence_normal_hosts_str = ""
		zookeeper_hosts_str, mysql_hosts_str = "", ""
		mongo_hosts_str = ""

		persistence_normal_hosts = []
		mysql_hosts = []
		mongo_hosts = []
		tomcat_hosts = []
		iobalancer_hosts = []

		with open(HOST_IP_FILE, 'r') as f:
			hosts_ip_dict = json.loads(f.read())

		with open(ORC_PAAS_FILE, 'r') as f:
			prole_ip = json.loads(f.read())

		with open(ORC_SAAS_FILE, 'r') as f:
			srole_ip = json.loads(f.read())

		for hostname, bind_addr in hosts_ip_dict.items():

			outer_hosts_ip_str += "\t" + "'" + hostname + ":" + \
				bind_addr['bindPublicIP'] + "', " + "\n"

			inner_hosts_ip_str += "\t" + "'" + hostname + ":" + \
				bind_addr['bindPrivateIP'][0] + "', " + "\n"
			
			if hostname != "opsserver":
				zookeeper_hosts_str += "\t" + "'" + hostname + "', " + "\n"

		for ipaddr, roles in prole_ip.items():

			if "Production_Persistence_Normal" in roles:
				persistence_normal_hosts.append(ipaddr)

			if "Production_Persistence_Normal_Mysql_Master" in roles \
				or "Production_Persistence_Normal_Mysql_Slave" in roles:
				mysql_hosts.append(ipaddr)

			if "Production_Persistence_Normal_MongoDB_Master" in roles \
				or "Production_Persistence_Normal_MongoDB_Slave" in roles:
				mongo_hosts.append(ipaddr)

			if "Production_Persistence_Normal_Tomcat" in roles:
				tomcat_hosts.append(ipaddr)

		for ipaddr, roles in srole_ip.items():
			if "Production_Access_Normal" in roles:
				iobalancer_hosts.append(ipaddr)
		
		mysql_hosts_str = self.getHostStr(mysql_hosts, hosts_ip_dict)
		persistence_normal_hosts_str = self.getHostStr(persistence_normal_hosts, hosts_ip_dict)
		mongo_hosts.reverse()
		mongo_hosts_str = self.getHostStr(mongo_hosts, hosts_ip_dict)
		tomcat_hosts_str = self.getHostStr(tomcat_hosts, hosts_ip_dict)
		iobalancer_hosts_str = self.getHostStr(iobalancer_hosts, hosts_ip_dict)
		
		#print outer_hosts_ip_str, inner_hosts_ip_str

		t = Template(filename=ENV_VARS_TEMPLATE_FILE)
		return t.render(target_name = target_name,
						primary_domain=target_name,remote='Y',
						outer_hosts_ip_str=outer_hosts_ip_str,
						inner_hosts_ip_str=inner_hosts_ip_str,
						boc_host_ip='', memcached_hosts=persistence_normal_hosts_str,
						redis_hosts=persistence_normal_hosts_str,
						rabbitmq_hosts=persistence_normal_hosts_str,
						mysql_hosts=mysql_hosts_str, mongo_hosts=mongo_hosts_str,
						tomcat_hosts=tomcat_hosts_str,iobalancer_hosts=iobalancer_hosts_str)

	def init_robotframework_env_vars(self):

		print "==============>>> init robotframework configs.<<<=================="
		env_vars_filename = self.bind_deployschema.schema_name + '_vars.py'
		with open(HOST_IP_FILE, 'r') as f:
			host_ip_content = f.read()

		host_ips = json.loads(host_ip_content)
		target_env_template = '\n\
		export REMOTE=${remote}\n \
		export NODE1=${ip}\n \
		export MTUSER=${mtuser}\n\
		export CKUSER=${checkuser}\n\
		export CKPASS=${checkpassword}\n\
		export BOCNODE=${bocnode_IP}\n\
		export BOCUSER=${bocuser}\n\
		export HOST_FILE=${vars_filename}\n\
		\n'

		target_temp = Template(target_env_template)
		target_env_contents = target_temp.render(remote='Y',
												ip=host_ips['node01']['bindPublicIP'],
												mtuser='mtagent',
												checkuser='mtagent',
												checkpassword='magima.1',
												bocnode_IP='',
												bocuser='',
												vars_filename=env_vars_filename)

		#print target_env_contents
		with open(ROBOTFRAMEWORK_DIR+'target.env', 'w+') as f:
			f.write(target_env_contents)

		self.generate_env_vars()
		#with open(ROBOTFRAMEWORK_DIR + env_vars_filename, 'w+') as f:
		#	f.write(self.generate_env_vars())

	def doWork(self):
		# do preverify
		print red('''
			EXECUTE DEPLOY.
		''')
		try:
			self.verifySchemaAndResource()
			self.initdomain()
			# do init 
			self.init_config_files()
			# init robotframework config files.
			#self.init_robotframework_env_vars()
			# do exec handler
			DeployHandler().execProvider()
			
		except KeyboardInterrupt, e:
			print >> sys.stderr, "\n\nExit on user cancel."

