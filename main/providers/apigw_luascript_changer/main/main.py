#!/usr/bin/env python

import os, sys

# change apigw config 

def main():

	if os.system("fab -f apigw_lua_script_changer.py go") != 0:
		print "excute fabfile error.exit"
		sys.exit(1)

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

