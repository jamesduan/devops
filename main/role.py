
from OrchestratorConfig import DEPLOY_DESIGN_FILE_URL
from xmlparse import XMLParse

class Role(object):
	
	def __init__(self, roleName="", provider=""):
		self.rolename = roleName
		self.providerName = provider

class RoleManager(object):
	
	roles = []

	def __init__(self):

		for role in self.load_roles():
			if len(role._children) > 1:
				self.roles.append( Role(roleName=role.attrib['Name'],
									provider=role._children[1].attrib['SpecName']))
			else:
				self.roles.append( Role(roleName=role.attrib['Name']))

	def load_roles(self):
		xmlparse = XMLParse(xml_file_path=DEPLOY_DESIGN_FILE_URL['Role'])
		return xmlparse.query('Role')

	def queryRoleByUID(self, roleUID):
		for role in self.load_roles():
			if role.attrib['RoleUID'] == roleUID:
				return role.attrib['Name']

	def getPaasRoles(self):

		paas_roles = []

		for role in self.load_roles():
			if role.attrib['CloudLayer'] == "PAAS":
				paas_roles.append(role.attrib['Name'])

		return paas_roles

#print RoleManager().queryRoleByUID("35bd2a8e-0786-4d3c-b3ee-15e54505b26a")

