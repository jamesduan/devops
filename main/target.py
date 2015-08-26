
from xmlparse import XMLParse
from OrchestratorConfig import DEPLOY_DESIGN_FILE_URL

class DeployTarget(object):
	
	def __init__(self, runtime_type="", componentName='',
				componentVersion='', targetProvider=[]):
		
		self.runtime_type = runtime_type
		self.componentName = componentName
		self.componentVersion = componentVersion
		self.targetProvider = targetProvider

	@property
	def getBinaryPackages(self):
		return self.componentName + "-" + self.componentVersion + '.zip'

	@property
	def getTargetProvider(self):
		return self.targetProvider

class DeployTargetManager(object):
	
	targetList = []

	def __init__(self):
		pass

	@property
	def listTargetList(self):
		return self.targetList
	
	def importTargetList(self):
		xmlparse = XMLParse(xml_file_path=DEPLOY_DESIGN_FILE_URL['Target'])
		for target in xmlparse.query('Target'):
			targetProviderList = []
			componentName = target.attrib['SpecName']
			componentVersion = target.attrib['specVersion']
			runtime_type = target._children[0]._children[0]._children[1].\
				_children[1]._children[0].attrib['Type']

			for element in target._children:
				if element.tag == 'TargetProvider':
					targetProviderList.append(element)

			targetProvider = targetProviderList
			self.targetList.append(DeployTarget(componentName = componentName,
												componentVersion = componentVersion,
												runtime_type = runtime_type,
												targetProvider = targetProvider))

	def getTargetNameByUID(self, UID):
		xmlparse = XMLParse(xml_file_path=DEPLOY_DESIGN_FILE_URL['Target'])
		for target in  xmlparse.query('Target'):
			
			if UID == target.attrib['TargetUID']:
				return target.attrib['SpecName']

#tm = DeployTargetManager()
#print tm.getTargetNameByUID('faa734d8-11a6-4b4b-b5ab-f15b07c87129')

