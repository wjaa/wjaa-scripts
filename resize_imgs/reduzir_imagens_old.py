# /usr/bin/env python
 # -*- coding: UTF-8 -*-
import re
import os
from django.http import HttpResponse


# metodo que recebe as requests.
def init(request):
	path = request.GET['path'].encode('utf-8')
	largura =  request.GET['largura']
	altura = request.GET['altura']
	
	doResize(path,[int(largura),int(altura)])
	return HttpResponse("Olá")
	




#Metodo que chama o imagemagic para redimensionar as imagens
def doResize(image_dir,resolution):
	#commando para resize da imagem
	command_resize = "convert {0} -resize {1} {2}";

	#criando o diretorio resultante
	os.popen("mkdir " + image_dir + "/result");

	#pegando o resultado do comando para listar todas as imagens do diretorio
	imagens = os.popen("./list_imagens.sh " + image_dir);
	imagens2 = os.popen("./list_imagens.sh " + image_dir);

	# variaveis contadores de imagens
	count_imagens = 0;
	total_imagens = 0;

	#encontrar uma forma melhor sem usar a interacao novamente.
	for img in imagens2:
		total_imagens = total_imagens +1 ;


	#interando sobre as imagens
	for img  in imagens:
		count_imagens = count_imagens + 1;
		#caminho da image original
		path_image = "'" + image_dir + "/" + img.rstrip() + "'";
		#caminho da imagem resultante
		path_image_result = "'" + image_dir + "/result/" + img.rstrip() + "'";

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




