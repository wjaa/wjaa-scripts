
!/bin/bash
# Exemplo Final de Script Shell
#http://www.devin.com.br/shell_script/


# utiliazado para quando encontrar path com espaços ou retorno de linha
# os ifs e fors nao quebram a string
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

dirOrigem=""
dirDestino=""
largura="800"
altura="600"

Principal() {   
   clear	
   echo "###### Script criado por Wagner Araujo. ######"
   echo "Esse script usa o convert para diminuir a resolucao das imagens"
   echo "------------------------------------------"
   echo "Opções:"
   echo
   echo "1. Diminuir a resolucao de todas as imagens de um diretorio"
   echo "2. Sair"
   echo -n "Qual a opção desejada? "
   read opcao
   case $opcao in
      1) transformar ;;
      2) exit ;;
      *) "Opção desconhecida." ; echo ; Principal ;;
   esac
}
transformar() {
	#pedindo pro usuario o diretorio de origem.
	inputDirOrigem

	#pedindo pro usuario o diretorio de destino.
	inputDirDestino
	
        #pedindo pro usuario a largura da imagem
	inputLargura

	#pedindo pro usuario a altura da imagem
	inputAltura

	echo "A configuração ficou assim:"
	echo "------------------------------------"
	echo "PATH_ORIGEM = $dirOrigem"
	echo "PATH_DESTINO = $dirDestino"
	echo "LARGURA = $largura"
	echo "ALTURA = $altura"
	echo "------------------------------------"
	echo -n "Confirma os dados? S/N: "
	read confirma
	if [ $confirma = "S"] || [ $confirma = "s" ]; then
		echo "Executando o script python para reduzir as imagens...."
		python reduzir_imagens.py doResize $dirOrigem $dirDestino $largura $altura
	else
		transformar
	fi

}

inputDirOrigem(){
	dirOrigem=""
	echo -n "Informe o diretorio de origem das imagens: "
        read dirOrigem
        retorno=$(./is_diretorio.sh $dirOrigem)
        if [ $retorno = "0" ]; then
                echo "ERROOOOO  Path não é um diretório [$dirOrigem] "       
                inputDirOrigem
        fi  
}

inputDirDestino(){
	echo -n "Informe o diretório de destino das imagens: "
	read dirDestino
	retorno=$(./is_diretorio.sh $dirDestino)
	if [ $retorno = "0" ]; then
		echo "ERROOOOO Path não é em diretório [$dirDestino]"
		inputDirDestino
	fi
} 

inputAltura(){
	echo -n "Informe a altura da imagem final: "
	read altura
	if [ $altura == [0-9] ]; then
		echo "ERROOOOO Essa altura é inválida [$altura]"
	fi

}

inputLargura(){
	echo -n "Informe a largura da imagem final: "
	read largura
	 if [ $largura == [0-9] ]; then
		echo "ERROOOOO Essa largura é inválida [$largura]"
	fi
}




Principal
