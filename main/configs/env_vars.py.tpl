TARGET_NAME='${target_name}'
REMOTE='${remote}'
PRIMARY_DOMAIN='${primary_domain}'
#BOC_DOMAIN = ''

HOSTS_OUTER = [
    ${outer_hosts_ip_str}
]

HOSTS_INNER = [
	${inner_hosts_ip_str}
]

HOST_BOC = '${boc_host_ip}'

HOST_IMPORT = ''

#roles:Production_Persistence_Normal
MEMCACHED_SERVERS = [${memcached_hosts}]
REDIS_SERVERS = [${redis_hosts}]
RABBITMQ_SERVERS = [${rabbitmq_hosts}]

ZOOKEEPER_SERVERS = [${zookeeper_hosts}]

MYSQL_SERVERS = [${mysql_hosts}]
MONGO_SERVERS = [${mongo_hosts}]  # mongo master is before than mongo slave
TOMCAT_SERVERS = [${tomcat_hosts}]

IOBALANCER_SERVERS = [${iobalancer_hosts}]
IOBALANCER_SITES = [
	'${iobalancer_hostname}:www.${primary_domain}.com',
]

#IOBALANCER_SERVERS = ['node1001', 'node1004', 'node1005']

IMAGE_SERVERS = [${image_hosts}]
DOC_SERVERS = [${doc_hosts}]
TFS_SERVERS = [${tfs_hosts}]
SLBGATEWAY_SERVERS = [${slbgateway_hosts}]
SLBMETASERVER_SERVERS = [${slbmetaserver_hosts}]

APIGW_SERVERS = [${apigw_hosts}]
BOCGW_SERVERS = [${bocgw_hosts}]

ACTIVITYSTREAM_SERVERS = [${activitystream_hosts}]
INVITATION_SERVERS = [${invitation_hosts}]
CONTACT_SERVERS = [${contact_hosts}]

OAS_SERVERS = [${oas_hosts}]
COMMONLIB_SERVERS = [${commonlib_hosts}]
JETTY_SERVERS = [${jetty_hosts}]

APPCENTER_SERVERS = [${appcenter_hosts}]

APPCENTER_SITES = [
	'${appcenter_hostname}:www.${primary_domain}.com',
]

DOWNLOAD_APP = [
	'${appcenter_hostname}:/mobile/download_beta/mybibo.apk',
]

DOWNLOAD_APP_UNSIGNED = [
	'${appcenter_hostname}:/mobile/download_beta/startActivity-beta-unsigned.apk',
]

OPEN_APP = [
	'${appcenter_hostname}:hibiscus.magima.com',
]

BOC_DBNAME = '${bocdb_name}'
BOCWEBAPP = '${bocname}'

DNS_SERVER = '${dnsserver_name}'
REPO_SERVER = '${reposerver_name}'
PRIMARY_IOBALANCER_SERVER = '${primary_iobalancer_hostname}'

SEARCH_SERVER_IP = '${search_server_ip}'
FLUENTD_AGENTS = [${fluentd_agents}]

CHEF_CLIENTS = [${chef_client_hosts}]
PSACCT_NODES = [${acct_hosts}]

GRAYLOG_CLIENTS = [${graylog_client_hosts}]

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


