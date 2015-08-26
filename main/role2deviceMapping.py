from xmlparse import XMLParse
from OrchestratorConfig import DEPLOY_DESIGN_FILE_URL


class Role2DeviceMapping(object):

	def __init__(self, roleUID, hostUID):
		self.roleUID = roleUID
		self.hostUID = hostUID

class Role2DeviceManager(object):
	
	mappings = []

	def __init__(self):

		mappingItems = self.loadRole2Devices()

		for item in mappingItems:
			roleUID = item.text.split(':')[0].lstrip('{').rstrip('}')
			hostUID = item.text.split(':')[1].lstrip('{').rstrip('}')
			self.mappings.append(Role2DeviceMapping(roleUID, hostUID))

	def loadRole2Devices(self):
		xmlparse = XMLParse(xml_file_path=DEPLOY_DESIGN_FILE_URL['Role2DeviceMapping'])
		return xmlparse.query('MappingItem')

	def getRole2Devices(self):
		return self.mappings
	
	def queryRoleByHostUID(self, hostUID):

		roleUIDs = []
		
		for mapper in self.mappings:
			if hostUID == mapper.hostUID:
				roleUIDs.append(mapper.roleUID)

		return list(set(roleUIDs))

#print Role2DeviceManager().queryRoleByHostUID('2c7eb9c4-3927-47ed-8b99-476747e01454')
#print Role2DeviceManager().queryRoleByHostUID('46298d9b-b02f-4766-a069-3c236a3bb208')
#print Role2DeviceManager().queryRoleByHostUID('9ed71aa9-7f34-4c9f-a1ec-8d110c740253')
#
