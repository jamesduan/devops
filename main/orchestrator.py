# encoding:utf8

from deployresource import DeployResourceManager
from role import RoleManager
from target import DeployTargetManager
from deployschema import DeploySchemaManager
from role2deviceMapping import Role2DeviceManager
from xmlcmdb_observer import XMLCMDBObserver
from DeployExecutionManager import DeployExcutionManager
from deployresource import DeployResourceManager

class Orchestrator(object):
	
	def __init__(self):

		self.deployResourceManager = DeployResourceManager()
		# role
		self.roleManager = RoleManager()

		# xmlcmb observer
		self.xmlcmdbobserver = XMLCMDBObserver()

		#target manager
		self.deployTargetManager = DeployTargetManager()
		self.deployTargetManager.importTargetList()
		
		#self.deployExecutionM = DeployExecManager()
		# role2deviceMappings
		self.role2deviceMappingManager = Role2DeviceManager()
		role2deviceMappingList = self.role2deviceMappingManager.mappings

		# deployschemaManager
		self.deploySchemaManager = DeploySchemaManager()
		self.deploySchemaManager.loadDeploySchema()

		self.deploySchemaList = self.deploySchemaManager.listDeploySchema()
		
		self.deploySchema = self.deploySchemaList[0]
		self.deploySchema.role2DeviceMappingList = role2deviceMappingList
		#self.role2deviceMappings = role2deviceMappingManager.getRole2Devices()

		# execution manager 
		self.executionManager = DeployExcutionManager()

		# resources manager
		self.resourceManager = DeployResourceManager()

