# encoding:utf8

from xmlcmdb_observer import XMLCMDBObserver

class DeployResource(object):
	
	def __init__(self, resourceUID="", resourceLimit=None,
				availableTimeWindowForDeploy=None):
		self.resourceUID = resourceUID
		self.resourceLimit = resourceLimit
		self.availableTimeWindowForDeploy = availableTimeWindowForDeploy

class DeployResourceManager(object):
	
	resources = []

	def __init__(self):
		xcbo = XMLCMDBObserver()
		self._manageResource(xcbo.getDataCenter())
		self._manageResource(xcbo.getNetwork())
		self._manageResource(xcbo.getHostlist())
		self._manageResource(xcbo.getContainerlist())
		
	def _manageResource(self, resource=None):
		try:
			for tmp_resource in resource:
				if not tmp_resource.attrib:
					return
				resourceUID = tmp_resource.attrib['ResourceUID']
				if not resourceUID:
					continue
				self.resources.append(DeployResource(resourceUID=resourceUID))
		except KeyError, msg:
			print "Key error:", msg
	
	def getResourceByUID(self, UID=None):
		for resource in self.resources:
			if resource.resourceUID == UID:
				return resource

#drM = DeployResourceManager()
#for root in drM.resources:
#	print root.resourceUID

