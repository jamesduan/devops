import StringIO

from fabric.api import *
from fabric.colors import green, red

from settings import USERNAME, PASSWORD, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_BASEDIR
from common import hosts

env.hosts = hosts
env.user = USERNAME
env.password = PASSWORD
slave_status_buffer = StringIO.StringIO()

def go():

	slave_status = run(MYSQL_BASEDIR + '/bin/mysql -u' + MYSQL_USERNAME + ' -p' + \
		MYSQL_PASSWORD + ' -e "show slave status\G"', shell=False,
		stdout=slave_status_buffer)

	for line in slave_status.split('\n'):
		if "Slave_IO_Running" in line or "Slave_SQL_Running" in line and "Slave_SQL_Running_State" not in line:
			
			if "Yes" in line.split(':')[1]:
				print green("Slave_IO_Running; Slave_SQL_Running_State; passed!")
				
			else:
				print red("slave replication is not create compelte ok! please check and try agian!")

