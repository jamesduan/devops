# encoding:utf8

from DeployWorker import DeployWorker
from logger import Logger

class DeployExcutionManager(object):

	deployWorker = []
	usedProvider = []

	def __init__(self):
		pass

	def newDeployWorker(self, deployeSchema=None, resources=[]):
		logger = Logger('deploy worker', '/tmp/deploy.log', 'DEBUG')
		deployWorker = DeployWorker(logger=logger,
									bindDeploySchema=deployeSchema,
									bindResources=resources)
		return deployWorker

	def findProvider(self):
		
		pass

	def downloadProvider(self):

		pass

