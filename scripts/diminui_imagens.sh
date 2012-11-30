#!/bin/bash
# Exemplo Final de Script Shell
#http://www.devin.com.br/shell_script/
Principal() {
   echo "Esse script usa o convert e gera preview de 1024x768"
   echo "------------------------------------------"
   echo "Opções:"
   echo
   echo "1. Diminuir a resolucao de todas as imagens de um diretorio"
   echo "2. Sair"
   echo -n "Qual a opção desejada? "
   read opcao
   case $opcao in
      1) Transformar ;;
      2) exit ;;
      *) "Opção desconhecida." ; echo ; Principal ;;
   esac
}
Transformar() {
      echo -n "Informe o diretorio das imagens: "
      read dir

      echo -n "Confirma o diretorio = $dir ? s/n "
      read confirma

      if [ $confirma = "s" ]; then
      	echo -n "Informe o diretorio de distino das imagens:"
      	read dirDestino

      	echo -n "Confirma o diretorio de destino = $dirDestino ? s/n"
      	read confirmaDestino

      	if [ $confirmaDestino = "s" ]; then
          cd $dirDestino
          mkdir 1024x768
          cd $dir
	  #aqui tem um problema, ele corta nomes de arquivos que tem espacos.
          for x in `ls -b --escape -1`; do
            if [ -d $x ]; then
              echo "$x eh um diretorio."
            else
              echo "trabalhando na imagem = $x"
              convert $x -resize 1024x768 $dirDestino/1024x768/$x
            fi
          done
       fi
     fi 
}
Principal
