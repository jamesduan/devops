#!/usr/bin/env python

import os

# init businesse data

def main():

	#os.system('fab -f doPreVerify.py go 2>&1 | tee ~/init_database_preVerify.log')

	os.system('fab -f mysql_initialize.py go 2>&1 | tee ~/init_mysql_database_go.log')
	os.system('fab -f mongodb_initialize.py go 2>&1 | tee ~/init_mongo_database_go.log')
	os.system('fab -f register_tfs_app.py go 2>&1 | tee ~/init_tfs_app.log')

	#os.system('fab -f doPostVerify.py go 2>&1 | tee ~/init_database_postVerify.log')

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

