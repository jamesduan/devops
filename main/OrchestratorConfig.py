# encoding:utf8

DEPLOY_DESIGN_FILE_URL = {
	'EnvResource':'../conf/EnvResource.xml',
	'Role':'../conf/RoleDefine.xml',
	'Target':'../conf/Target.xml',
	'DeploySchema':'../conf/DeploySchema.xml',
	'TargetRoleMapping': '../conf/TargetRoleMapping.xml',
	'Role2DeviceMapping': '../conf/Role2DeviceMapping.xml',
}

# provider repository url
PROVIDER_REPO_URL = '/opt/lampp/htdocs/providers/'
TARGET_REPO_URL = 'http://repo-server:1670/generics'
RPM_REPO_URL = 'http://repo-server:1670/rpms'

LOGLEVEL = (
     'DEBUG',
     'INFO',
     'WARN' ,
     'ERROR' 
)

# iaas provider input config file 
IAAS_NETWORK_CHECK_CONFIG_FILE='./IAAS/resource/network_chcker/conf/iaas_check_host_list.json'
IAAS_HOSTNAME_CHECK_CONFIG_FILE='./IAAS/resource/hostname_checker/conf/iaas_check_host_list.json'

TESTENV_REPO_SERVER = {
	'ip' : '10.0.0.126', 
	'user' : 'mtagent', 
	'password' : 'magima.1',
}

UPDATE_WAR_PATH = '/opt/upgrade/wars/' 

UPDATE_REPO_PATH = '/opt/lampp/htdocs/upgrade/testenv/jetty/'

PROVIDER_TYPE =(
	'robotframework',
	'chef',
	'ssh',
	'fabric',
	'python',
)

PAAS_ROLE = ['', '', '']

EXEC_HOME='~/orchestrator/main'

CHEF_ROLE_CONFIG_FILE_PATH='./juarez/roles/'

PROVIDER_PATH='./providers/'
TOPLEVEL_PROVIDER_NAME='toplevel'
PROVISION_PROVIDER_NAME='toplevel4provision'

CLEANER_PROVIDER_PATH = './providers/cleaner/main'
DOMAIN_FILE = 'configs/domain.json'

ORC_PAAS_FILE='juarez/scripts/role/orc_paas.json'
ORC_SAAS_FILE='juarez/scripts/role/orc_saas.json'
ORC_ZOO_FILE='juarez/scripts/role/orc_null.json'

HOST_IP_FILE = 'configs/host_ip.json'

ROBOTFRAMEWORK_DIR = 'robotframework_PQA/'

ENV_VARS_TEMPLATE_FILE='configs/env_vars.py.tpl'
PYTHON_DEVEL_PATH='../lib/python-devel-2.6.6-52.el6.x86_64.rpm'
