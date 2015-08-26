
import json

HOST_IP_CONFIG_PATH = '../../../configs/host_ip.json'
ORC_PAAS_CONFIG_PATH = '../../../juarez/scripts/role/orc_paas.json'

with open(HOST_IP_CONFIG_PATH, 'r') as f:
	json_contents = f.read()

HOST_IPS = json.loads(json_contents)
#print HOST_IPS

with open(ORC_PAAS_CONFIG_PATH, 'r') as f:
	jj2 = f.read()

with open('../../../configs/.secret', 'r') as f:
	secret_d = f.read()

IP_ROLES = json.loads(jj2)
#print IP_ROLES

MYSQL_PORT = '3306'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'magima.1'

USERNAME = secret_d.split(':')[0]
PASSWORD = secret_d.split(':')[1]

INIT_PROVIDER_NAME = 'initdbdata-v2.0-201507101035.zip'
INIT_PROVIDER_DIR = 'initdbdata-v2.0'

REGISTER_TFS_APP_PROVIDER= 'registerTfsApp-v1.0-201411242009.zip'
REGISTER_TFS_APP_DIR = 'registerTfsApp-v1.0'
TFS_DB = 'tfs_name_db'

MYSQL_BIN='/opt/magima/mysql/bin/mysql'

# register pvo_clients
PVO_INSERT_PROVIDER_ZIP = 'register_pvo_client-v1.0-201411061642.zip'
PVO_INSERT_PROVIDER_DIR = 'register_pvo_client-v1.0'

