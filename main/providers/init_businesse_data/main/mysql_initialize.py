# encoding:utf8

from fabric.api import *

from common import mysql_master_host
from settings import USERNAME, PASSWORD, \
	INIT_PROVIDER_NAME, INIT_PROVIDER_DIR

env.hosts = mysql_master_host
env.user = USERNAME
env.password = PASSWORD

def go():
	put('packages/' + INIT_PROVIDER_NAME, '~/' + INIT_PROVIDER_NAME)
	
	run('unzip ' + INIT_PROVIDER_NAME)
	# initproduce=0
	#是否初始化boc：1＝是 0＝否
	#initboc=0
	#是否保留组件安装信息：1＝是 0＝否
	#initcom=0

	with cd(INIT_PROVIDER_DIR + '/main'):
		run('sed -i -e s/initmongo=.*/initmongo=0/g properties.ini')
		run('sed -i -e s/initproduce=.*/initproduce=1/g properties.ini')
		run('sed -i -e s/initboc=.*/initboc=1/g properties.ini')
		run('sed -i -e s/initcom=.*/initcom=1/g properties.ini')
		run('bash initdbdata.sh')

