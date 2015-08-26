
from fabric.api import *

from common import mongodb_master_host
from settings import USERNAME, PASSWORD, \
	INIT_PROVIDER_NAME, INIT_PROVIDER_DIR

env.hosts = mongodb_master_host
env.user = USERNAME
env.password = PASSWORD

def go():

	put('packages/' + INIT_PROVIDER_NAME, '~/' + INIT_PROVIDER_NAME)
	
	run('unzip ' + INIT_PROVIDER_NAME)
	with cd(INIT_PROVIDER_DIR + '/main'):
		run('sed -i -e s/initmongo=.*/initmongo=1/g properties.ini')
		run('sed -i -e s/initproduce=.*/initproduce=0/g properties.ini')
		run('sed -i -e s/initboc=.*/initboc=0/g properties.ini')
		sudo('bash initdbdata.sh')

