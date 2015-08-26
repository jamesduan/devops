# encoding:utf8

import os, sys

from settings import *
from fabric.colors import red

def main():

	# mysql replication
	print red("MYSQL: ===> DO PRE VERIFY.")
	if os.system('fab -f doPreVerify.py go 2>&1 | tee ~/replication_doPreVerify.log') != 0:
		print "excute doPreVerify.py error!exit."
		sys.exit(1)
	
	print red('MYSQL: ===> MV CONFIG FILES.')
	os.system('fab -f fabfile4mysql_config.py go 2>&1 | tee ~/replication_mysql_config.log')
	print red("MYSQL: ===> EXEC MV DATA DIRECTORY PROVIDER.")
	os.system('fab -f mysql_mvdata_tool.py go 2>&1 | tee ~/replication_mvdata.log')
	print red('MYSQL: ===> EXEC REPLICATION PROVIDER.')
	os.system('fab -f mysql_replication_tool.py go 2>&1 | tee ~/replication_do.log')
	print red("MYSQL: ===> DO POST VERIFY.")
	os.system('fab -f doPostVerify.py go 2>&1 | tee ~/replication_doPostVerify.log')

	## mongodb replication
	print red("MONGODB: ===> DO PRE VERIFY.")
	## exec 
	#
	print red("MONGODB: ===> MV DATA.")
	os.system('fab -f mongo_mvdata_tool.py go 2>&1 | tee ~/mongo_mvdata.log')
	#
	print red("MONGODB: ===> EXEC REPLICATION PROVIDER.")
	os.system('fab -f mongo_replication_tool.py go 2>&1 | tee ~/mongo_replication.log')

	# first configuring my.cnf and boot script

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt, e:
		print >> sys.stderr, "\nExiting on user cancel.\n"
		sys.exit(1)
	except OSError, e:
		print >> sys.stderr, "\n excute os command error\n"
		sys.exit(1)
	except Exception, e:
		print "A error occurred, exit."
		sys.exit(1)

