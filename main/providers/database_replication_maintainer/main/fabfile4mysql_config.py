
from fabric.api import *

from common import hosts
from settings import USERNAME, PASSWORD

env.hosts = hosts
print env.hosts
env.user = USERNAME
env.password = PASSWORD

def go():

	#put('templates/mysql.server', '/etc/init.d/mysql.server')
	put('templates/mysql.server', '/tmp/mysql.server')
	sudo('cp -v /tmp/mysql.server /etc/init.d/mysql.server')

	#put('templates/my.cnf', '/opt/magima/mysql/my.cnf')
	put('templates/my.cnf', '/tmp/my.cnf')
	sudo('cp -v /tmp/my.cnf /opt/magima/mysql/my.cnf')

	#put('templates/etc.my.cnf', '/etc/my.cnf')
	put('templates/etc.my.cnf', '/tmp/my.cnf')
	sudo('cp -v /tmp/my.cnf /etc/my.cnf')
	sudo('/etc/init.d/mysql.server restart')

