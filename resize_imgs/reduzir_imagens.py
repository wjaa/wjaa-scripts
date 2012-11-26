# /usr/bin/env python
 # -*- coding: UTF-8 -*-
import re
import os
import time
from django.http import HttpResponse


# metodo que recebe as requests.
def init(request):
	path_origem = request.GET['path_origem'].encode('utf-8')
	path_destino = request.GET['path_destino'].encode('utf-8');
	largura =  request.GET['largura']
	altura = request.GET['altura']
	
	
	line = os.popen("./is_diretorio.sh " + path_origem.replace("(","\\(").replace(")","\\)").replace(" ","\\"))
	
	isDir = str(line.read()).rstrip() 

	if isDir == '1':
		doResize(path_origem,path_destino,[int(largura),int(altura)])
		return HttpResponse("<h1>Imagens reduzidas com sucesso!!!</h1>")
	else:
		return HttpResponse("<b> Diretorio das imagens não existe! </b> ")
	




#Metodo que chama o imagemagic para redimensionar as imagens
def doResize(image_dir,image_des,resolution,sub_dir = ''):

	full_dir = image_dir
	if len(sub_dir) != 0:
		print 'existe um subdir'
		full_dir = image_dir + "/" + sub_dir

	#commando para resize da imagem
	command_resize = "convert {0} -resize {1} {2}";

	#criando o diretorio resultante
  	os.popen("mkdir " + image_des + "/" + sub_dir);

	print full_dir

	time.sleep(2)

	imagens = os.popen("ls -1 " + full_dir)
	
 
	#pegando o resultado do comando para listar todas as imagens do diretorio
	imagens2 = os.popen("./list_imagens.sh " + full_dir);

	# variaveis contadores de imagens
	count_imagens = 0;
	total_imagens = 0;

	#encontrar uma forma melhor sem usar a interacao novamente.
	for img in imagens2:
		total_imagens = total_imagens +1 ;


	#interando sobre as imagens
	for img  in imagens:

		scape_path = "'" + full_dir + "/" + img.rstrip() + "'"
		line = os.popen("./is_diretorio.sh " + scape_path.replace("(","\\(").replace(")","\\)").replace(" ","\\"))

		isDir = str(line.read()).rstrip() 
		print isDir

		#isDir é um objeto, verificar como pegar o resultado
		if ( isDir == '1' ):
			print 'Encontrado um subfolder = ' + img
			time.sleep(3)
			doResize(image_dir, image_des, resolution, sub_dir + "/" + img.rstrip())
			continue


		count_imagens = count_imagens + 1;
		#caminho da image original
		path_image = "'" + full_dir + "/" + img.rstrip() + "'";
		#caminho da imagem resultante
		path_image_result = "'" + image_des + "/" + sub_dir + "/" + img.rstrip() + "'";

		#pegando o resultado do comando que busca a resolucao da imagem
		commandResult = os.popen("identify -verbose " + path_image ) ;
	 	out = commandResult.read();

		#extraindo a resolucao do conteudo do -verbose do identify
		p = re.compile("Geometry: [0-9]+x[0-9]+");
		reResult = p.search(out);
		if reResult:
			#pegando as dimensoes da imagem
			valor = reResult.group();
			dim =  valor.replace("Geometry: ","").replace("x",",").split(",");
	
			#posicao das dimensoes da imagem
			l = 0;
			a = 1;
	
			#chegando qual e o maior lado da imagem
			if int(dim[0]) < int(dim[1]) :
				#invertendo os lados da imagem 
				l,a = 1,0;

			#construindo comando para reduzir as imagens
			command = command_resize.format(path_image,str(resolution[l]) + 'x' + str(resolution[a]),path_image_result);
			print '[' + str(count_imagens) + '/'  + str(total_imagens) +'] - Convertendo imagem [' + img.rstrip() + ']';
			os.popen(command);
		else:
			print 'Erro: No image ' + img.rstrip();




doResize('/home/wagner/Imagens','/home/wagner/testeImg',[500,500])
