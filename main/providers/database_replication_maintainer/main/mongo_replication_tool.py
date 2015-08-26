
from fabric.api import *

from common import mongo_master_host_public, mongo_hosts_private

from settings import USERNAME, PASSWORD, MONGO_REPLI_PROVIDER_BASEDIR, MONGO_REPLI_PROVIDER_NAME

env.hosts = mongo_master_host_public
print env.hosts

#mongo_hosts_private.reverse()

mongo_serversip = ','.join(mongo_hosts_private)

print mongo_serversip

env.user = USERNAME
env.password = PASSWORD

def go():

	run('if [ -f "'+MONGO_REPLI_PROVIDER_NAME+'" ];then rm -rf '+MONGO_REPLI_PROVIDER_NAME+' ; fi')
	run('if [ -d "'+MONGO_REPLI_PROVIDER_BASEDIR+'" ];then rm -rf '+MONGO_REPLI_PROVIDER_BASEDIR+' ; fi')

	put('packages/' + MONGO_REPLI_PROVIDER_NAME, '~/' + MONGO_REPLI_PROVIDER_NAME)
	run('unzip ' + MONGO_REPLI_PROVIDER_NAME)

	with cd(MONGO_REPLI_PROVIDER_BASEDIR+'/main'):

		sudo('sed -i -e s/ip=.*/ip=' + mongo_serversip+ '/g properties.ini')
		sudo('sed -i -e s/sudouser=.*/sudouser=' + USERNAME+ '/g properties.ini')
		sudo('bash main.sh')

