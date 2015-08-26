import uuid

from fabric.api import *

from common import mysql_master_host
from settings import MYSQL_USER, MYSQL_PASSWD, MYSQL_PORT, PVO_INSERT_PROVIDER_ZIP, PVO_INSERT_PROVIDER_DIR, USERNAME, PASSWORD

env.hosts = mysql_master_host
env.user = USERNAME
env.password = PASSWORD

def go():
	
	sudo('if [ -f "' + PVO_INSERT_PROVIDER_ZIP + '" ];then rm -rf '+ PVO_INSERT_PROVIDER_ZIP +' ; fi')
	sudo('if [ -d "'+ PVO_INSERT_PROVIDER_DIR +'" ];then rm -rf '+ PVO_INSERT_PROVIDER_DIR +' ; fi')

	put('packages/' + PVO_INSERT_PROVIDER_ZIP, '~/' + PVO_INSERT_PROVIDER_ZIP)
	run('unzip ' + PVO_INSERT_PROVIDER_ZIP)
	# /opt/chef/embedded/bin/ruby register_pvo.rb --host node1001 --username root --pwd magima.1 --name newpqa --type web --url http://localhost
	with cd('~/' + PVO_INSERT_PROVIDER_DIR + '/main/'):
		sudo('/opt/chef/embedded/bin/ruby register_pvo.rb --host ' + mysql_master_host[0] + ' --username ' + MYSQL_USER + ' --pwd '+ MYSQL_PASSWD+' --name ' +str(uuid.uuid4())+ ' --type web ' + '--url http://localhost')

		with cd('~'):
			
			run('if [ -f "' + PVO_INSERT_PROVIDER_ZIP + '" ];then rm -rf '+ PVO_INSERT_PROVIDER_ZIP +' ; fi')
			run('if [ -d "'+ PVO_INSERT_PROVIDER_DIR +'" ];then rm -rf '+ PVO_INSERT_PROVIDER_DIR +' ; fi')

