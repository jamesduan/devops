#!/bin/bash -x


function funcdoinit(){
  hostip=$1
  
  myhostip=` /sbin/ifconfig |grep "inet addr:$hostip"|head -n+1 |awk  '{print $2}'|sed "s/addr://g"`
  echo "myhostip:"$myhostip
  
  if [ "$hostip" = "$myhostip" ]; then
      ps -aux|grep ${mongocmd}mongod > $shpath/tmp.txt
      ps -aux|grep ${mongocmd}mongod > $shpath/tmp1.txt
  else
      su $sudouser -c "sshpass -p $sudopassword ssh $hostip ps -aux|grep ${mongocmd}mongod" > $shpath/tmp.txt
      su $sudouser -c "sshpass -p $sudopassword ssh $hostip ps -aux|grep ${mongocmd}mongod" > $shpath/tmp2.txt
  fi
  echo $shpath/tmp.txt
  cat $shpath/tmp.txt
  congfile=`cat $shpath/tmp.txt |grep "${mongocmd}mongod -f " |awk  '{print $13}'`
  pid=`cat $shpath/tmp.txt |grep "${mongocmd}mongod -f " |awk  '{print $2}'`
  echo "pid="$pid
  echo "congfile="$congfile

  tmpcongfile="$mongobasedir/mongod.conf"

    dbpath=` cat $shpath/bundles/mongodrep.conf |grep "dbpath="|head -n+1 |sed "s/dbpath=//g"`
    logpath=` cat $shpath/bundles/mongodrep.conf |grep "logpath="|head -n+1 |sed "s/logpath=//g"|sed "s/mongo.log//g"`
echo "dbpath="$dbpath
echo "logpath="$logpath
  if [ "$hostip" = "$myhostip" ]; then
      #if [ ! -z "$congfile" ]; then
        if [ "$congfile" = "$tmpcongfile" ]; then
          echo "******停止  $hostip 的mongod："
          sudo stop mongod      
        else          
            if [ ! "$congfile" = "" ]; then
                echo "******kill  mongod："  
                kill -9 $pid
            fi 
        fi 
      #fi 
      mkdir -p $dbpath
      mkdir -p $logpath
      mkdir -p $mongobasedir/conf
      cp $shpath/bundles/mongodrep.conf $mongobasedir/conf/
      cp $shpath/bundles/mongod.conf $mongobasedir/conf/
      /usr/sbin/groupadd mongod
      /usr/sbin/useradd -g mongod mongod
      chown -R mongod:mongod  $dbpath
      chown -R mongod:mongod  $logpath
      chown -R mongod:mongod  $mongobasedir/conf
      rm /home/$sudouser/.mongorc.js
      echo "db.getMongo().setSlaveOk();" >/home/$sudouser/.mongorc.js
      echo "******重新启动$hostip 的mongod："

      sed -i 's/\/opt\/magima\/mongodb\/mongod.conf/\/opt\/magima\/mongodb\/conf\/mongodrep.conf/g' /etc/init/mongod.conf
        ${mongocmd}mongod -f $mongobasedir/conf/mongodrep.conf
  else   
      #if [ ! -z "$congfile" ]; then     
      if [ "$congfile" = "$tmpcongfile" ]; then
          echo "******停止  $hostip 的mongod："
          su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo stop mongod"
      else
          echo "******kill  $hostip 的mongod："  
          su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo kill -9 $pid"
      fi 
      #fi 
      
      echo "******$hostip 的conf："
      su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo mkdir -p $mongobasedir/conf"
      echo "******$hostip 的logs："
      su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo mkdir -p $logpath"
      echo "******$hostip 的data："
      su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo mkdir -p $dbpath"
      echo su $sudouser -c "sshpass -p $sudopassword scp $shpath/bundles/mongod*.conf $hostip:/tmp"
      su $sudouser -c "sshpass -p $sudopassword scp $shpath/bundles/mongod*.conf $hostip:/tmp"
      echo su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo  mv /tmp/mongod*.conf $mongobasedir/conf/"
      su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo  mv /tmp/mongod*.conf $mongobasedir/conf/"
      su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo /usr/sbin/groupadd mongod"
      su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo /usr/sbin/useradd -g mongod mongod"
      su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo chown -R mongod:mongod  $dbpath"
      su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo chown -R mongod:mongod  $logpath"
      su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo chown -R mongod:mongod  $mongobasedir/conf"
     
      echo su $sudouser -c "sshpass -p $sudopassword scp /home/$sudouser/.mongorc.js $hostip:/tmp"
      su $sudouser -c "sshpass -p $sudopassword scp /home/$sudouser/.mongorc.js $hostip:/tmp"
      echo su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo  mv /.mongorc.js /home/$sudouser/"
      su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo  mv /tmp/.mongorc.js /home/$sudouser/"

      echo "******重新启动远程$hostip 的mongod："
      echo "sshpass -p $sudopassword ssh -t $hostip sudo  ${mongocmd}mongod -f $mongobasedir/conf/mongodrep.conf"

      su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip \" sudo sed -i 's/\/opt\/magima\/mongodb\/mongod.conf/\/opt\/magima\/mongodb\/conf\/mongodrep.conf/g' /etc/init/mongod.conf\""

      su $sudouser -c "sshpass -p $sudopassword ssh -t $hostip sudo  ${mongocmd}mongod -f $mongobasedir/conf/mongodrep.conf "
  fi 
  #rm -rf $shpath/tmp*.txt
}


param_index=1
slaveserver_id=1;
server_id=1; 
  echo "$nodeip:"$nodeip
for param in ${nodeip[@]}
do
  echo "$param:"$param
  funcdoinit $param
done 


