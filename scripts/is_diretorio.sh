#!/bin/bash

#----------------------------------------------------------------#
#								 #
# Script para identificar se um path é um diretorno              #
#  ./is_diretorio.sh /home/wagner/dev  return 1                  #
#  ./is_diretorio.sh /home/wagner/Imagens/teste.jpg  return 0	 #
#                             					 #
#  chmod +x is_diretorio.sh  permissao de execucao do scritp     #
#                                                                # 
#----------------------------------------------------------------#

path=$1

if [ -d $path ]; then 
	echo 1;
else
	echo 0;
fi


# ------------------ Fim do script -------------------------------#
