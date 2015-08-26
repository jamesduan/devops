import os, subprocess, datetime, sys, json
import getpass

from orchestrator import Orchestrator
from colors import green, red
from OrchestratorConfig import IAAS_HOSTNAME_CHECK_CONFIG_FILE, \
								IAAS_NETWORK_CHECK_CONFIG_FILE,\
								UPDATE_WAR_PATH, UPDATE_REPO_PATH, \
								TESTENV_REPO_SERVER, EXEC_HOME, \
								CLEANER_PROVIDER_PATH
from target import DeployTargetManager
from role import RoleManager

class OrchestratorConsole(object):

	def __init__(self):
		self.orc = Orchestrator()

	#def iaasResourceCheck(self):

	#	iaas_resource_check_infos = "execute iaas resource check ."
	#	self.deployeWorker.logger.addLog(iaas_resource_check_infos, 'INFO')
	#	print green(iaas_resource_check_infos)
	#	self.deployeWorker.start_time = datetime.datetime.now()
	#	print red("start time:" + str(self.deployeWorker.start_time))
	#	self.deployeWorker.logger.addLog("start time:" + str(self.deployeWorker.start_time),
	#									'INFO')

	#	hosts = {}

	#	for hostUID in self.getUniqHost():

	#		host = self.orc.xmlcmdbobserver.getHostByUID(hostUID)
	#		host_pri_ipaddr1 = host.findall('./Hardware/EthernetIF')[0].attrib['bindPrivateIP']
	#		host_pri_ipaddr2 = host.findall('./Hardware/EthernetIF')[1].attrib['bindPrivateIP']
	#		hostname = host.attrib['name']
	#		hosts[hostname] = [host_pri_ipaddr1, host_pri_ipaddr2]

	#	#print hosts
	#	jsondata = json.dumps(hosts)
	#	with open(IAAS_NETWORK_CHECK_CONFIG_FILE, 'w+') as networkf:
	#		networkf.write(jsondata)

	#	with open(IAAS_HOSTNAME_CHECK_CONFIG_FILE, 'w+') as hostnamef:
	#		hostnamef.write(jsondata)
	#def resourceSetup(self):

	def doDeploy(self, schema_name):

		print "\ndo deploy: %s\n" % green(schema_name)
		deploySchema = self.orc.deploySchemaManager.querySchemaBySchemaName(schema_name)

		if not deploySchema:
			print red("schema name is not valid please try again!")
			return

		deployeWorker = self.orc.executionManager.newDeployWorker(
									deployeSchema=deploySchema,
									resources=self.orc.resourceManager.resources
									)
		try:
			deployeWorker.doWork()
		except KeyboardInterrupt, e:
			print >> sys.stderr, "\n\nExiting on user cancel."
			sys.exit(1)
		except OSError, e:
			print >> sys.stderr, "\n\nExiting on execute os command error."
			sys.exit(1)

	def execChefProvider(self):
		pass

	def execChefInit(self):
		pass
	
	def upload_jetty_war(self, war_name):
		try:
			proc = subprocess.Popen(['scp', UPDATE_WAR_PATH + war_name + '.war',
							TESTENV_REPO_SERVER['user'] + '@' + TESTENV_REPO_SERVER['ip']\
							+ ":" + UPDATE_REPO_PATH + war_name ],
							stdout=subprocess.PIPE,
							stderr=subprocess.PIPE
							)
			output = proc.communicate()
			print output

		except OSError, e:
			print >> stderr, "\n\n upload jetty war: exe os command error!"
			sys.exit(1)

		except ValueError, e:
			print >> stderr, "\n\n upload jetty war: Popen have invalid arguments."

	def update_jetty_war(self, war_name):
		# init robotframework env vars file
		self.upload_jetty_war(war_name)
		# execute provider todo 
		os.system('bash ./providers/robotframework_PQA/upload-jetty-war.sh')
		print war_name

	def listDeploySchema(self):
		# list deploySchemas
		print red("\n list deploy schemas:\n")
		for schema in self.orc.deploySchemaList:
			print green(schema.schema_name)

		# list Target Role Mappings
		print red("\nTargetRoleMapping: \n")
		dtm = DeployTargetManager()
		rm = RoleManager()
		for item in self.orc.deploySchema.targetRoleMapping:
			targetUID = item.text.split(':')[0].lstrip('{').rstrip('}')
			roleUID = item.text.split(':')[1].lstrip('{').rstrip('}')
			if dtm.getTargetNameByUID(targetUID):
				targetName = dtm.getTargetNameByUID(targetUID)
			if rm.queryRoleByUID(roleUID):
				roleName = rm.queryRoleByUID(roleUID)
			print green(targetName) + ' ===> ' + green(roleName)
		print "count: " + str(len(self.orc.deploySchema.targetRoleMapping))

		print "\n"
		# list targetinstance target mappings
		print red("TargetInstancesTargetMapping:\n")
		for targetInstance in self.orc.deploySchema.targetInstList:
			targetUID = targetInstance.attrib['TargetUID'].lstrip('{').rstrip('}')
			targetInstanceUID = targetInstance.attrib['InstanceUID']

			if dtm.getTargetNameByUID(targetUID):
				targetName = dtm.getTargetNameByUID(targetUID)
			print green(targetInstanceUID) + ' ===> ' + green(targetName)
		print "count: " + str(len(self.orc.deploySchema.targetInstList))

		self.listContainers()

	def	listTargets(self):
		for target in self.orc.deployTargetManager.targetList:
			print "Target Component name: %s " % (green(target.componentName))
		print "\n\n"

	def listRoles(self):
		for role in self.orc.roleManager.roles:
			print "rolename: %s " % (green(role.rolename))
		print "count: %s " % (len(self.orc.roleManager.roles))
		print "\n\n"

	def listEnvResources(self):
		for resource in self.orc.deployResourceManager.resources:
			print resource.resourceUID

	def listContainers(self):
		print "\n Containers:\n"
		for container in self.orc.xmlcmdbobserver.getContainerlist():
			container_type_name = container.attrib['type']
			container_version = container.attrib['version']
			container_UID = container.attrib['ResourceUID']
			print "typename: " + green(container_type_name) + "  version: " + green(container_version) + "  UID: " + green(container_UID)
		print "count: " + str(len(self.orc.xmlcmdbobserver.getContainerlist()))

	def setPassword(self):
		username = raw_input("please input your global user:")
		password = getpass.getpass('password:')
		with open('./configs/.secret', 'w+') as f:
			f.write(username+':'+password)

	def clean(self):

		current_dir = os.getcwd()
		os.chdir(CLEANER_PROVIDER_PATH)
		os.system('fab -f main.py go')
		os.chdir(current_dir)

	def install(self, cloud_layer):

		if cloud_layer == "paas":
			print "install paas"
		if cloud_layer == "saas":
			print "install saas"

	def showContainerStatus(self):
		pass
	
	def listWorkers(self):
		pass
	
	def showWorkerstatus(self):
		pass

