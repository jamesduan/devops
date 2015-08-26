#!/usr/bin/env python

import os, sys
from fabric.colors import red
# prepare baseline warehouse

print "update rpm database."

try:
	
	print "EXECUTE fabfile."
	if os.system('fab -f fabfile.py go') !=0 :
		print red("execute prepare rpmrepo server error!")
		sys.exit(1)

	if os.system('fab -f makecache.py go') != 0:
		print red('execute yum makecache error.')
		sys.exit(1)

except OSError, e:
	print "execute os command error.", e
	sys.exit(1)

except KeyboardInterrupt, e:
	print >> stderr , "Exit by user cancel."
	sys.exit(1)

except Exception , e:
	print "Abort with a error occurred."
	sys.exit(1)

