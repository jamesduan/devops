# encoding:utf8

import subprocess, os, time, ConfigParser, re, sys

from OrchestratorConfig import PROVIDER_PATH, TOPLEVEL_PROVIDER_NAME, \
	PROVISION_PROVIDER_NAME

class DeployHandler(object):

	deployPhase = None

	def __init__(self):
		self.deployPhase = ""

	def parseConfig(self, filepath):
		configParser = ConfigParser.RawConfigParser()
		configParser.read(filepath)
		sections = configParser.sections()
		data = {}
		for section in sections:
			kvs = configParser.items(section)
			data[section] = dict(kvs)
		return data

	#def search(self, pattern , content):
	#	match = re.search(pattern, content)
	#	match.start()
	#	match.end()
	#	return match.string
	def runProviderByUID(self, UID):
		for provider_dir in os.listdir("./"):
			property_content = self.parseConfig(provider_dir + '/provider.properties')

			if UID == property_content['Main']['uuid']:
				if property_content['Main']['language'] == 'python':
					if property_content['Main']['dsltype'] == 'fabric':
						os.chdir(provider_dir + '/main')
						os.popen("fab -f " + property_content['Runtime']['doentry']).readlines()
					else:
						os.chdir(provider_dir + '/main')
						if os.system("python " + property_content['Runtime']['doentry']) != 0:
							print "exit error!"
							sys.exit(1)
						os.chdir('../../')

				elif property_content['Main']['language'] == 'bash':
					os.chdir(provider_dir + '/main')
					print os.popen("bash " + property_content['Runtime']['doentry']).readlines()

	def execProvider(self):

		print "begin execute provider..."
		# prepare toplevel provider
		print "prepare toplevel privider..."
		time.sleep(1)
		# exec provider
		os.chdir(PROVIDER_PATH)
		# read provider.properties
		provider_properties = self.parseConfig(TOPLEVEL_PROVIDER_NAME + '/provider.properties')

		# read toplevel provider's dependency.desc
		# and execute provider.
		contents = ''
		with open(TOPLEVEL_PROVIDER_NAME + '/dependency.desc', 'r') as f:
			contents = f.read()
		#os.popen()

		# parse provider properties file
		#provider_uuids = []
		try:
			for line in contents.split('\n'):
				#print line
				if 'id:' in line:
					self.runProviderByUID(line.split(":")[1].strip())
			# excute toplevel provider complete
			print "\n===============>>deploy complete!<<===================\n"	
		except KeyboardInterrupt, e:
			print >> sys.stderr, "\n\n Exiting on user cancel."
			sys.exit(1)
		except OSError, e:
			print >> sys.stderr, "\n\nexec provider: exec os command error."
			sys.exit(1)

		# excute provision provider. before developer can use system themself.
		# this function to change configs , service lifecycle setting, data store 

		provision_denpendency_contents = ""
		with open(PROVISION_PROVIDER_NAME+'/dependency.desc', 'r') as f:
			provision_denpendency_contents = f.read()
		try:
			for line in provision_denpendency_contents.split('\n'):
				#print line
				if 'id:' in line:
					self.runProviderByUID(line.split(":")[1].strip())
			# excute toplevel provider complete
			print "\n===============>>provision operation complete!<<===================\n"	

		except KeyboardInterrupt, e:
			print >> sys.stderr, "\n\n Exiting on user cancel."
			sys.exit(1)
		except OSError, e:
			print >> sys.stderr, "\n\nexec provider: exec os command error."
			sys.exit(1)

		# the next...
		print "\n================>>init robotframework env vars...<<===================\n"
		
		
	def prepareDeployProvider():
		pass

	def install(self):
		pass
	
	def uninstall(self):
		pass

	def setAttributes(self):
		# this function is to set attributes to config file of chef.
		pass
	
	def verify(self):
		pass
	
	def start(self):
		pass

	def stop(self):
		pass
	
	def enable(self):
		pass
	
	def disable():
		pass

