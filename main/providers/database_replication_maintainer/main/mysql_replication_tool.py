
from fabric.api import *

from common import mysql_master_host,  private_ips
from settings import USERNAME, PASSWORD, REPLI_PROVIDER_BASEDIR, REPLI_PROVIDER_NAME

env.hosts = mysql_master_host
mysql_serversip = ','.join(private_ips)

env.user = USERNAME
env.password = PASSWORD

def go():

	run('if [ -f "'+REPLI_PROVIDER_NAME+'" ];then rm -rf '+REPLI_PROVIDER_NAME+' ; fi')
	run('if [ -d "'+REPLI_PROVIDER_BASEDIR+'" ];then rm -rf '+REPLI_PROVIDER_BASEDIR+' ; fi')

	put('packages/' + REPLI_PROVIDER_NAME, '~/' + REPLI_PROVIDER_NAME)
	run('unzip ' + REPLI_PROVIDER_NAME)

	with cd(REPLI_PROVIDER_BASEDIR+'/main'):
		sudo('sed -i -e s/ip=.*/ip=' + mysql_serversip+ '/g properties.ini')
		sudo('sed -i -e s/sudouser=.*/sudouser=' + USERNAME+ '/g properties.ini')
		sudo('bash main.sh')

