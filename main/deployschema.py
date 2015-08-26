# encoding:utf8

import os

from OrchestratorConfig import DEPLOY_DESIGN_FILE_URL
from xmlparse import XMLParse
from xmlcmdb_observer import XMLCMDBObserver
from util import getoutCurlyBraces
from target import DeployTargetManager

class DeploySchema(object):
	
	def __init__(self, targetInstList=[], containerInstList=[],
				targetRoleMapping=[], targetInstContainerMapping=[],
				role2DeviceMappingList=[], schema_name=None):

		if not targetInstList:
			print "target list is null!"
		self.targetInstList = targetInstList
		if not containerInstList:
			print "container instance list is null!"
		self.containerInstList = containerInstList

		if not targetRoleMapping:
			print "target role mapping is None"
		self.targetRoleMapping = targetRoleMapping

		if not targetInstContainerMapping:
			print "target instance container mapping is None.!"
		self.targetInstContainerMapping = targetInstContainerMapping

		# role to device mapping list defined
		self.role2DeviceMappingList = []

		# additional attribute
		self.schema_name = schema_name

class DeploySchemaManager(object):
	
	deploySchemaList = []

	def __init__(self):
		self.xmlcmdbobserver = XMLCMDBObserver()
		pass

	def listDeploySchema(self):
		return self.deploySchemaList

	def loadDeploySchema(self):

		xmlparse = XMLParse(xml_file_path=DEPLOY_DESIGN_FILE_URL['DeploySchema'])
		deploySchema = xmlparse.query('DeploySchema')
		for schema in deploySchema:
			targetInstanceList = schema[0]._children
			containerInstanceList = schema[1]._children
			targetInstanceContainerInstanceMapping = schema[2]._children
			self.deploySchemaList.append(DeploySchema(targetInstList= targetInstanceList,
													containerInstList=containerInstanceList,
													targetRoleMapping = self.loadTargetRoleMapping(),
													targetInstContainerMapping = targetInstanceContainerInstanceMapping,
													schema_name = self.xmlcmdbobserver.getDataCenter()[0].attrib['name']))
		return

	def loadTargetRoleMapping(self):
		xmlparse = XMLParse( xml_file_path=DEPLOY_DESIGN_FILE_URL['TargetRoleMapping'] )
		targetRoleMapping = xmlparse.query('TargetToRoleMapping')
		return targetRoleMapping[0]._children

	def getTargetNamesByRoleUID(self, roleUID):
		targetNames = []
		dtm = DeployTargetManager()
		for mapping in self.loadTargetRoleMapping():
			tmp_roleUID = getoutCurlyBraces(mapping.text.split(':')[1])
			tmp_targetUID = getoutCurlyBraces(mapping.text.split(':')[0])
			if tmp_roleUID == roleUID:
				targetNames.append(dtm.getTargetNameByUID(tmp_targetUID))
		return targetNames

	def execDeploySchema(self):
		pass

	def querySchemaBySchemaName(self, schema_name):

		try:
			for schema in self.listDeploySchema():
				if schema.schema_name == schema_name:
					return schema

		except Exception,msg:
			print msg
			return

