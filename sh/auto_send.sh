ip=$1
user=$2
passwd=$3
echo $ip,$user,$passwd
#for obj in "${objs[@]}";
#for line in ${cat
for line in $(cat ./objs.txt)
	do
		obj=$line
		md5sum $obj
		sshpass -p $passwd scp $obj $user@$ip:/root/
	done

