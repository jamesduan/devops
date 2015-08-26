TARGET_NAME='testenv'
REMOTE='Y'
PRIMARY_DOMAIN = 'testenv'
BOC_DOMAIN = 'testenv'

HOSTS_OUTER = [
    'node01:10.0.0.123',
    'node02:10.0.0.124',
    'node03:10.0.0.125',
    'chef-server:10.0.0.126'
]

HOSTS_INNER = [
	'node01:10.0.107.13',
	'node02:10.0.107.14',
	'node03:10.0.107.15',
	'chef-server:10.0.107.17',
]

HOST_BOC = 'node1000boc:10.0.6.168'
HOST_IMPORT = 'import1000:10.0.6.152'

#roles:Production_Persistence_Normal
MEMCACHED_SERVERS = ['node02']
REDIS_SERVERS = ['node02']
RABBITMQ_SERVERS = ['node02']

ZOOKEEPER_SERVERS = ['node01', 'node02', 'node03']

MYSQL_SERVERS = ['node01', 'node02']
MONGO_SERVERS = ['node03', 'node01']
TOMCAT_SERVERS = ['node01', 'node02', 'node03']
IOBALANCER_SERVERS = ['node01']
IOBALANCER_SITES = [
	'node01:www.testenv.com',
]

#IOBALANCER_SERVERS = ['node1001', 'node1004', 'node1005']
IMAGE_SERVERS = ['node02', 'node03']
DOC_SERVERS = ['node02', 'node03']
TFS_SERVERS = ['node03']
SLBGATEWAY_SERVERS = ['node01', 'node02']
SLBMETASERVER_SERVERS = ['node01', 'node02']
APIGW_SERVERS = ['node02', 'node03']
BOCGW_SERVERS = ['node01']

ACTIVITYSTREAM_SERVERS = ['node01', 'node02']
INVITATION_SERVERS = ['node01', 'node02']
CONTACT_SERVERS = ['node02', 'node03']
OAS_SERVERS = ['node01', 'node02']
COMMONLIB_SERVERS = ['node01', 'node02', 'node03']
JETTY_SERVERS = ['node01', 'node02', 'node03']

APPCENTER_SERVERS = ['node02']

APPCENTER_SITES = [
	'node02:www.testenv.com',
]

DOWNLOAD_APP = [
	'node02:/mobile/download_beta/mybibo.apk',
]

DOWNLOAD_APP_UNSIGNED = [
	'node02:/mobile/download_beta/startActivity-beta-unsigned.apk',
]
OPEN_APP = [
	'node01:hibiscus.magima.com',
]

BOC_DBNAME = 'bocdb'
BOCWEBAPP = 'bocwebapp'

DNS_SERVER = 'chef-server'
REPO_SERVER = 'chef-server'
PRIMARY_IOBALANCER_SERVER = 'node01'

SEARCH_SERVER_IP = '10.160.14.232'
FLUENTD_AGENTS = ['node01', 'node02', 'node03']

CHEF_CLIENTS = ['node01', 'node02', 'node03']
PSACCT_NODES = ['node01', 'node02', 'node03', 'chef-server']

GRAYLOG_CLIENTS = ['node01', 'node02', 'node03']
LOG_PATHS = {
	'iobalancer_access': '/opt/magima/openresty/nginx/logs/proxy.access.log',
	'iobalancer_error': '/opt/magima/openresty/nginx/logs/proxy.error.log',
	'apigw_access': '/opt/magima/openresty/nginx/logs/apigw_access.log',
	'apigw_error': '/opt/magima/openresty/nginx/logs/apigw_error.log',
	'boss4_access': '/opt/magima/openresty/nginx/logs/boss4_access.log',
	'boss4_error': '/opt/magima/openresty/nginx/logs/boss4.error.log',

	'servshell': '/opt/magima/saas_bibo123/cloud_components/servshell/log/_output.log',
	'useraccount': '/opt/magima/saas_bibo123/cloud_components/useraccount/log/_output.log',
	'asset': '/opt/magima/saas_bibo123/cloud_components/asset/log/_output.log',
	'invitation': '/opt/magima/saas_bibo123/cloud_components/invitation/log/_output.log',
	'notifyservice': '/opt/magima/saas_bibo123/cloud_components/notifyservice/log/_output.log',
	'contact': '/opt/magima/saas_bibo123/cloud_components/contact/log/_output.log',
	'topic': '/opt/magima/saas_bibo123/cloud_components/topic/log/_output.log',
	'party': '/opt/magima/saas_bibo123/cloud_components/party/log/_output.log',
	'privchat': '/opt/magima/saas_bibo123/cloud_components/privchat/log/_output.log',
	'sysadmin': '/opt/magima/saas_bibo123/cloud_components/sysadmin/log/_output.log',
	'oas': '/opt/magima/saas_bibo123/cloud_components/oas/log/_output.log',
	'saassettingservice': '/opt/magima/saas_bibo123/cloud_components/saassettingservice/log/_output.log',
	'imageservice': '/opt/magima/saas_bibo123/cloud_components/imageservice/log/_output.log',
	'slbmetaserver': '/opt/magima/saas_bibo123/cloud_components/slbmetaserver/log/_output.log',
	'docservice': '/opt/magima/log/docservice_log.log',
	'activitystream': '/opt/magima/log/activitystream_log.log',
	'adpservice': '/opt/magima/log/adpservice_log.log',
	'appcenterservice': '/opt/magima/log/appcenterservice_log.log',
	'userfeedbackservice': '/opt/magima/log/userfeedbackservice_log.log',
	'webcontentservice': '/opt/magima/log/webcontentservice_log.log',
	'tomcat': '/opt/magima/tomcat6/logs/catalina.out',
	'mysql': '/var/magima/log/paas/mysql/slow.log',
	'mongo': '/var/magima/log/paas/mongodb/logs/mongo.log',
	'tfs_nameserver': '/opt/magima/tfs-data/tfs-data/tfs-ns/logs/nameserver.log',
	'tfs_rcserver': '/opt/magima/tfs-data/rcserver/work_dir/logs/rcserver.log',
	'tfs_dataserver': '/opt/magima/tfs-data/tfs-ds/logs/dataserver_2.log',
	'slbgateway': '/opt/magima/slbgateway/logs/slbgateway-*.log',
	'php_web': '/var/log/php-fpm/boss4-error.log',
	'bocgw_access': '/opt/lampp/logs/access_log',
	'bocgw_error': '/opt/lampp/logs/error_log',
        'redis': '/var/log/redis/redis.log',
        'rabbitmq': '/var/log/rabbitmq/rabbit@node*.log',
	'zookeeper': '/var/log/zookeeper.log',
}
