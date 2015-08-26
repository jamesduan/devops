
import json

HOST_IP_CONFIG_PATH = '../../../configs/host_ip.json'
ORC_PAAS_CONFIG_PATH = '../../../juarez/scripts/role/orc_paas.json'

with open(HOST_IP_CONFIG_PATH, 'r') as f:
	json_contents = f.read()

HOST_IPS = json.loads(json_contents)
#print HOST_IPS

with open(ORC_PAAS_CONFIG_PATH, 'r') as f:
	jj2 = f.read()

IP_ROLES = json.loads(jj2)
#print IP_ROLES

with open('../../../configs/.secret', 'r') as f:
	s_d = f.read()

USERNAME=s_d.split(':')[0]
PASSWORD=s_d.split(':')[1]

MYSQL_BASEDIR='/opt/magima/mysql'
MYSQL_USERNAME='root'
MYSQL_PASSWORD='magima.1'

REPLI_PROVIDER_NAME = 'mysql_start_rep-mm-v1.1-201412040942.zip'

REPLI_PROVIDER_BASEDIR = 'mysql_start_rep-mm-v1.1'

MYSQL_MVDATA_PROVIDER_NAME = 'mysql_mvdata-v1.0-201412041508.zip'
MYSQL_MVDATA_PROVIDER_BASEDIR = 'mysql_mvdata-v1.0'

MONGO_MVDATA_PROVIDER_NAME = 'mongodb_mvdata-v1.0-201412041508.zip'
MONGO_MVDATA_PROVIDER_BASEDIR = 'mongodb_mvdata-v1.0'

MONGO_REPLI_PROVIDER_NAME = 'mongodb_start_ms-v1.1-201412041952.zip'
MONGO_REPLI_PROVIDER_BASEDIR = 'mongodb_start_ms-v1.1'

MONGO_BASE = '/opt/magima/mongodb'

