
from fabric.api import *

from common import mysql_master_host, tfs_host
from settings import USERNAME, PASSWORD, \
	INIT_PROVIDER_NAME, INIT_PROVIDER_DIR, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWD, TFS_DB,\
	REGISTER_TFS_APP_PROVIDER, REGISTER_TFS_APP_DIR, MYSQL_BIN

env.hosts = mysql_master_host
env.user = USERNAME
env.password = PASSWORD

def go():

	run('if [ -f "' + REGISTER_TFS_APP_PROVIDER + '" ];then rm -rf '+ REGISTER_TFS_APP_PROVIDER +' ; fi')
	run('if [ -d "'+ REGISTER_TFS_APP_DIR +'" ];then rm -rf '+ REGISTER_TFS_APP_DIR +' ; fi')

	put('packages/' + REGISTER_TFS_APP_PROVIDER,
		'~/' + REGISTER_TFS_APP_PROVIDER)
	run('unzip ' + REGISTER_TFS_APP_PROVIDER)

	with cd(REGISTER_TFS_APP_DIR  + '/main'):
		sudo('./registerTfsApp.sh {tfs_mysql_host} {tfs_mysql_port} {tfs_mysql_user} {tfs_mysql_password} {tfs_mysql_db} {tfs_ipaddr} {tfs_rcport} {tfs_nsport} {mysql_bin}'.\
			format(tfs_mysql_host = mysql_master_host[0].encode('utf-8'),
					tfs_mysql_port = MYSQL_PORT,
					tfs_mysql_user = MYSQL_USER,
					tfs_mysql_password = MYSQL_PASSWD,
					tfs_mysql_db = TFS_DB,
					tfs_ipaddr = tfs_host[0],
					tfs_rcport = '5100', tfs_nsport = '8108',
					mysql_bin = MYSQL_BIN))

		#run('./tfs_doc.sh {tfs_mysql_host} {tfs_mysql_port} {tfs_mysql_user} {tfs_mysql_password} {tfs_mysql_db} {tfs_ipaddr} {tfs_rcport} {tfs_nsport} {mysql_bin}'.format(tfs_mysql_host = mysql_master_host[0].encode('utf-8'),
		#											tfs_mysql_port = MYSQL_PORT,
		#											tfs_mysql_user = MYSQL_USER,
		#											tfs_mysql_password = MYSQL_PASSWD,
		#											tfs_mysql_db = TFS_DB,
		#											tfs_ipaddr = tfs_host[0],
		#											tfs_rcport = "5100", tfs_nsport = "8108",
		#											mysql_bin = MYSQL_BIN))
	
		## ns:8108, rc:5100
		#run('./tfs_image.sh {tfs_mysql_host} {tfs_mysql_port} {tfs_mysql_user} {tfs_mysql_password} {tfs_mysql_db} {tfs_ipaddr} {tfs_rcport} {tfs_nsport} {mysql_bin}'.format(tfs_mysql_host = mysql_master_host[0].encode('utf-8'),
		#									tfs_mysql_port = MYSQL_PORT,
		#									tfs_mysql_user = MYSQL_USER,
		#									tfs_mysql_password = MYSQL_PASSWD,
		#									tfs_mysql_db = TFS_DB,
		#									tfs_ipaddr = tfs_host[0],
		#									tfs_rcport = "5100", tfs_nsport = "8108",
		#									mysql_bin = MYSQL_BIN))


