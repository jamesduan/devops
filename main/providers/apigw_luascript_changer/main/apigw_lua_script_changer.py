
from fabric.api import *

from common import apigw_host_public

from settings import USERNAME, PASSWORD, APIGW_BASEDIR

env.hosts = apigw_host_public
env.user = USERNAME
env.password = PASSWORD

#/opt/magima/apigw/scripts/lua/apigw.lua
def go():
	sudo('sed -i -e "195s/setResponsesByProfile()/--setResponsesByProfile()/g" ' + APIGW_BASEDIR + '/scripts/lua/apigw.lua')
	sudo('sed -i -e "4s/setrequestsByProfile()/--setrequestsByProfile()/g" ' + APIGW_BASEDIR + '/scripts/lua/apimapping.lua')

	for i in range(94, 99):
		sudo('sed -i -e "'+str(i)+'s/^/--/g" ' + APIGW_BASEDIR + '/scripts/lua/apimapping.lua')


