#!/bin/bash -x
#在主机上执行配置
#sudo sh /opt/mtprovision/daas/replicationmongo/mongodb_rep_ms/mongodb_start_ms-v1.0/main/main.sh 10.0.5.112,10.0.5.83
today=`date +%Y%m%d%H%M%S`
shpath=$(cd $(dirname $0); pwd)
    
source $shpath'/properties.ini'

if [ ! -z $1 ]; then  
  ip=$1
fi 
if [ ! -z $2 ]; then  
  port=$2
fi 
echo $port
if [ ! -z $3 ]; then  
  sudouser=$3
fi 
if [ ! -z $4 ]; then  
  sudopassword=$4
fi 
echo $ip
nodeip=(${ip//,/ })
param_index=1
for param in ${nodeip[@]}
do

  if [ -z "$masterip" ]; then
      masterip=$param
  else
    if [ -z "$slaveip" ]; then
        slaveip=$param
    else
        break
    fi
  fi
done 

echo $port
nodeport=(${port//,/ })
for param in ${nodeport[@]}
do
  if [ -z "$masterport" ]; then
      masterport=$param
  else
    if [ -z "$slaveport" ]; then
        slaveport=$param 
    else
        break
    fi
  fi
done 

echo "masterip:"$masterip
echo "masterport:"$masterport
echo "slaveip:"$slaveip
echo "slaveport:"$slaveport

if [ -z $masterip ];then
    echo "#################:masterip为空，不具备配置replication，退出本次配置！#################"
    exit 801
fi
if [ -z $slaveip ];then
    echo "#################:slaveip为空，不具备配置replication，退出本次配置！#################"
    exit 802
fi

   myhostip=` /sbin/ifconfig |grep "inet addr:$masterip"|head -n+1 |awk  '{print $2}'|sed "s/addr://g"`
   echo "myhostip:"$myhostip

   if [ -z $myhostip ]; then
     echo "#################:请在master机器上执行本次主从配置！#################"
     exit 881
   fi 

   tmpstr=$(cat $shpath/bundles/mongodrep.conf | grep "replSet=" | awk '{print $1}')
   repname=${tmpstr/"replSet="/""} 

   echo "配置 replSet:"$repname
   source $shpath/init.sh

   echo "配置 replSet:"$repname
   if [ ! 0 -eq $? ]; then
       echo "#################:replication启动失败,先关闭mongod单节点模式！#################"
       exit 883
   else
       echo "#################:replication启动！#################"
   fi 

   echo "配置 master:"$masterip   
   echo 'config = { _id:''"'$repname'"'',members:[{_id:0,host:''"'$masterip':'$masterport'"''},{_id:1,host:''"'$slaveip':'$slaveport'"''}]}' > $shpath/bundles/config.js
  echo "rs.initiate(config)"  >> $shpath/bundles/config.js
   
  cat $shpath/bundles/config.js
  echo "${mongocmd}mongo --port $masterport $shpath/bundles/config.js"
   

  ${mongocmd}mongo --host $masterip --port $masterport $shpath/bundles/config.js
  if [ ! 0 -eq $? ]; then
       echo "#################:主节点config设置失败！#################"
       exit 884
  else       
       echo "#################:主节点config设置成功！#################"
  fi 

  echo "配置 slave:"$slaveip
  echo "db.getMongo().setSlaveOk();" > $shpath/bundles/slaveok.js
  ${mongocmd}mongo --host $slaveip --port $slaveport $shpath/bundles/slaveok.js
  ${mongocmd}mongo --host $slaveip --port $slaveport $shpath/bundles/slaveok.js

  #echo " sshpass -p $sudopassword ssh -t $hostip ${mongocmd}mongo --host $slaveip --port $slaveport  $shpath/bundles/slaveok.js"
  su $sudouser -c "sshpass -p $sudopassword scp $shpath/bundles/slaveok.js $slaveip:/tmp/"  
  su $sudouser -c "sshpass -p $sudopassword ssh -t $slaveip ${mongocmd}mongo /tmp/slaveok.js"

  if [ ! 0 -eq $? ]; then
      echo "#################:从节点slaveok设置失败！#################"
      exit 884
  else       
      echo "#################:从节点slaveok设置成功！#################"
      
  fi 

  rm -rf $shpath/*.txt
  rm -rf $shpath/*.cnf

