import StringIO

from fabric.api import *

from common import  mongo_hosts_public
from settings import USERNAME, PASSWORD, MONGO_BASE


env.hosts = mongo_hosts_public
env.user=USERNAME
env.password=PASSWORD

mongo_statu_buffer = StringIO.StringIO()

def go():
	mongo_status = sudo(MONGO_BASE + '/bin/mongo; exit',
						shell=False, stdout=mongo_statu_buffer)
	print mongo
