#!/bin/bash
#sudo nsenter --target `docker inspect --format {{.State.Pid}} $1` --mount --uts --ipc --net --pid bash

container_id=`sudo docker ps | awk '{print $1}' | sed -n 2p `
echo $container_id 
PID=$(sudo docker inspect --format {{.State.Pid}} $container_id)
echo $PID 
sudo nsenter --target $PID --mount --uts --ipc --net --pid


