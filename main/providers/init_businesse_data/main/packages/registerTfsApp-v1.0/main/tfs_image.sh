#!/bin/bash

if [ $# != 9 ]; then
    echo "Usage: $0 tfs_mysql_host tfs_mysql_port tfs_mysql_user tfs_mysql_password tfs_mysql_dbname tfs_ipAddr tfs_rcPort tfs_nsPort"
    exit 99
fi

tfs_mysql_host=$1
tfs_mysql_port=$2
tfs_mysql_user=$3
tfs_mysql_password=$4
tfs_mysql_dbname=$5
tfs_ipAddr=$6
tfs_rcPort=$7
tfs_nsPort=$8
mysql_bin=$9


$mysql_bin -u${tfs_mysql_user} -p${tfs_mysql_password} -h${tfs_mysql_host} -P${tfs_mysql_port} $tfs_mysql_dbname -e "select * from t_app_info where app_key='tappkey_imageservice';" > ./tmp.out
tmp_lines=$(cat ./tmp.out | wc -l)
if [ $tmp_lines -le 1 ]; then
    $mysql_bin -u${tfs_mysql_user} -p${tfs_mysql_password} -h${tfs_mysql_host} -P${tfs_mysql_port} $tfs_mysql_dbname -e "INSERT INTO t_app_info VALUES('tappkey_imageservice',1,1073741824,1,0,'picture_space','magima',5,0,'',now(),now());"
    $mysql_bin -u${tfs_mysql_user} -p${tfs_mysql_password} -h${tfs_mysql_host} -P${tfs_mysql_port} $tfs_mysql_dbname -e "INSERT INTO t_cluster_rack_group VALUES (1,1,2,'',now(),now());"
    eval "$mysql_bin -u${tfs_mysql_user} -p${tfs_mysql_password} -h${tfs_mysql_host} -P${tfs_mysql_port} $tfs_mysql_dbname -e \"INSERT INTO t_cluster_rack_info VALUES (1,'T1Mmagim','$tfs_ipAddr:$tfs_nsPort',2,'',now(),now());\""
    eval "$mysql_bin -u${tfs_mysql_user} -p${tfs_mysql_password} -h${tfs_mysql_host} -P${tfs_mysql_port} $tfs_mysql_dbname -e \"INSERT INTO t_resource_server_info VALUES ('$tfs_ipAddr:$tfs_rcPort',1,'test_first',now(),now());\""
    $mysql_bin -u${tfs_mysql_user} -p${tfs_mysql_password} -h${tfs_mysql_host} -P${tfs_mysql_port} $tfs_mysql_dbname -e "INSERT INTO t_base_info_update_time VALUES (now(),now());"
    exit 1
fi

exit 0

