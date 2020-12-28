#!/bin/bash
#docker ps | grep bb
#[ $? -eq 0 ] && docker rm -f bb
docker run -d --name nginx -p 82:80 nginx
