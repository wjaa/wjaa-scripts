#!/bin/bash
echo "INICIANDO BUILD DO ADMIN"
#pull do admin do mpr e build do admin
cd /home/mpr-server/mpr/mpr-admin && git pull && mvn clean install

path=target/admin.war

if [ -f "$path" ]; then
    echo "Removendo o container e a imagem anterior"
    docker rmi mpr/admin && sudo docker rm -f mpr-admin_fe_1
    echo "Gerando nova imagem"
    docker build .
    echo "Gerando container"
    docker-compose up -d 
    echo "FIM DO BUILD"

else
    echo "ERROR: Algum erro no build não gerou o war. Implementar envio de email"
fi