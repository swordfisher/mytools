
supervisorctl stop all
ps -ef | grep supervisord | grep -v grep | awk ' {print $2}' | xargs -i kill -9 {}
/usr/bin/python /usr/bin/supervisord -c /etc/supervisord.conf
supervisorctl start all

