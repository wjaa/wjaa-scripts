#!/bin/bash

#--------------------------------------------------#
#                                                  #
# Lista apenas arquivos do diretorio solicitado    #
# pastas e arquivos ocultos seram ignorados        # 
# permissão de execucao chmod +x ./list_imagens.sh #
# ex: ./list_imagens.sh /home/wagner/Imagens       #
#                                                  # 
#--------------------------------------------------#

# utiliazado para quando encontrar path com espaços ou retorno de linha
# os ifs e fors nao quebram a string
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

#pegando o diretorio informado.
path=$1

#interando sobre os arquivos listados no diretorio
for i in $(ls -1 $path); do
   if [ ! -d $path/$i ]; then
      echo $i
   fi
done


#------------------ Fim do script -----------------#
