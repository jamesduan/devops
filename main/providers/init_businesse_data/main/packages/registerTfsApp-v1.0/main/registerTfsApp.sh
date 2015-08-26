#!/bin/bash

export PATH=/opt/magima/mysql/bin:$PATH

scriptdir=$(cd $(dirname $0);pwd)

if [ $# != 9 ]; then
    echo "Usage: $0 tfs_mysql_host tfs_mysql_port tfs_mysql_user tfs_mysql_password tfs_mysql_dbname tfs_ipAddr tfs_rcPort tfs_nsPort"
    echo "Usage:  default port(ns:8108, rc:5100)"
    exit 99
fi

tfs_mysql_host=$1
tfs_mysql_port=$2
tfs_mysql_user=$3
tfs_mysql_password=$4
tfs_mysql_dbname=$5
tfs_ipAddr=$6

cd $scriptdir
for script in `ls tfs_*.sh`;do
    ./$script  $*
done
exit 0

#TODO:  must set the tfs.conf(rc.conf,ds.conf) for mysql.passwd
sshpass $tfs_ipAddr "sed -i -e \"s|^meta_db_infos.*|meta_db_infos = $tfs_mysql_host:$tfs_mysql_port:$tfs_mysql_dbname,$tfs_mysql_user,$tfs_mysql_password|g\" /opt/magima/tfs/conf/ns.conf"
sshpass $tfs_ipAddr "sed -i -e 's|mount_maxsize.*|mount_maxsize = 16777216|g'" /opt/magima/tfs/conf/ds.conf
#rc.server
#rc_db_info = 10.0.107.20:3306:tfs_name_db
#rc_db_user = root
#rc_db_pwd = boss.magima
su mtagent -c "shpass -p magima.1 ssh $tfs_ipAddr sudo sed -i -e 's|rc_db_info.*|rc_db_info = $tfs_mysql_host:$tfs_mysql_port:$tfs_mysql_dbname |g' /opt/magima/tfs/conf/rc.conf"
su mtagent -c "sshpass -p maigma.1 ssh $tfs_ipAddr sudo sed -i -e 's|rc_db_user.*|rc_db_user = $tfs_mysql_user|g' /opt/magima/tfs/conf/rc.conf"

su mtagent -c "sshpass -p magima.1 ssh $tfs_ipAddr sed -i -e 's|rc_db_pwd.*|rc_db_pwd = $tfs_mysql_password|g' /opt/magima/tfs/conf/rc.conf"

#TODO:  must set the imageservice/docservice tfs.xml for rcserver ip

# create /img ""
# create /img/bucket ""
# create /img/bucket/avt {"logicalServers":["img"],"physicalServers":{"img":"img.biboboss.com"},"thumbnailPolicy":{"L":"500x500","M":"300x300","S":"100x100","T":"50x50","lastModified":"2014-07-30"}}
# create /img/bucket/qrc {"logicalServers":["img"],"physicalServers":{"img":"img.biboboss.com"},"thumbnailPolicy":{"L":"200x140","lastModified":"2014-07-30"}}
# create /img/bucket/wpr-uploaded {"logicalServers":["img"],"physicalServers":{"img":"img.biboboss.com"},"thumbnailPolicy":{"IC":"38x38","lastModified":"2014-07-30"}}
# create /img/bucket/usr-uploaded  {"logicalServers":["img"],"physicalServers":{"img":"img.biboboss.com"},"thumbnailPolicy":{"T":"80x80","lastModified":"2014-07-30"}}
#create /img/bucket/gar {"logicalServers":["img"],"physicalServers":{"img":"img.biboboss.com"},"thumbnailPolicy":{"L":"208x208","S":"122x122","lastModified":"2014-07-30"}}

