
from fabric.api import *

from common import mongo_hosts_public

from settings import USERNAME, PASSWORD, MONGO_MVDATA_PROVIDER_NAME, \
	MONGO_MVDATA_PROVIDER_BASEDIR

env.hosts = mongo_hosts_public
env.user = USERNAME
env.password = PASSWORD

def go():
	# mongodb mvdata
	
	run('if [ -f "'+MONGO_MVDATA_PROVIDER_NAME+'" ];then rm -rf '+MONGO_MVDATA_PROVIDER_NAME+' ; fi')
	run('if [ -d "'+MONGO_MVDATA_PROVIDER_BASEDIR +'" ];then rm -rf '+MONGO_MVDATA_PROVIDER_BASEDIR+' ; fi')

	put('packages/' + MONGO_MVDATA_PROVIDER_NAME, '~/' + MONGO_MVDATA_PROVIDER_NAME)
	run('unzip ' + MONGO_MVDATA_PROVIDER_NAME)
	with cd(MONGO_MVDATA_PROVIDER_BASEDIR + '/main'):
		sudo('bash main.sh')

