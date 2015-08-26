
from fabric.api import *

from common import hosts
from settings import USERNAME, PASSWORD, MYSQL_MVDATA_PROVIDER_NAME, \
		MYSQL_MVDATA_PROVIDER_BASEDIR

env.hosts = hosts
env.user = USERNAME
env.password = PASSWORD

def go():
	print "1"
	run('if [ -f "'+MYSQL_MVDATA_PROVIDER_NAME+'" ];then rm -rf '+MYSQL_MVDATA_PROVIDER_NAME+' ; fi')
	print "2"
	run('if [ -d "'+MYSQL_MVDATA_PROVIDER_BASEDIR +'" ];then rm -rf '+MYSQL_MVDATA_PROVIDER_BASEDIR+' ; fi')
	print "3"
	put('packages/'+ MYSQL_MVDATA_PROVIDER_NAME, '~/' + MYSQL_MVDATA_PROVIDER_NAME)
	print "4"
	run('unzip ' + MYSQL_MVDATA_PROVIDER_NAME)
	print "5"
	with cd(MYSQL_MVDATA_PROVIDER_BASEDIR+'/main'):
		print "6"
		sudo('bash main.sh')

