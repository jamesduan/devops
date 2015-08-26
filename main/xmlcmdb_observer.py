# encoding:utf8

from envresource_observer import EnvResouceObserver
from xmlparse import XMLParse
from OrchestratorConfig import DEPLOY_DESIGN_FILE_URL
from util import getoutCurlyBraces

class XMLCMDBObserver(EnvResouceObserver):
	
	def __init__(self):
		self.xmlparse = XMLParse(
			xml_file_path=DEPLOY_DESIGN_FILE_URL['EnvResource'])
		
	def getResource(self, tagname):
		return [element for element in self.xmlparse.query(tagname)]

	def getDataCenter(self):
		return self.getResource('DataCenter')

	def getNetwork(self):
		return self.getResource('Network')
	

	def getHostlist(self):
		return self.getResource('Host')

	def getHostByContainerUID(self, containerUID):

		for host in self.getHostlist():

			containers = host.findall("./Software/Containers")

			for container in containers:

				for ref in container._children:

					if ref.text != None and containerUID == getoutCurlyBraces(ref.text):

						return host
	
	def getHostByUID(self, UID):
		hosts = self.getHostlist()
		#print hosts
		for host in hosts:
			#print host
			if host.attrib['ResourceUID'] == UID:
				return host

	def getContainerlist(self):
		return self.getResource('Container')

	#def getIPList(self):
	#	hosts = self.getHostlist()
	#	
	#	for host in hosts:
	#		
	#		for ethernet in host.findall('./Hardware/EthernetIF'):
				

#XMLCMDBObserver().getHostByContainerUID('9b553d55-8f24-4cd0-86d2-00a15cb4d693')

