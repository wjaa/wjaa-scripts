#!/bin/bash

#pull do admin do mpr e build do admin
cd /home/mpr-server/mpr/mpr-admin && git pull && mvn clean install

path=target/admin.war

if [ ! -d $path ]; then
	#removendo as imagens antigas
	echo 'chegou aqui...'
else
    echo "Algum erro no build não gerou o war. Implementar envio de email"
fi
