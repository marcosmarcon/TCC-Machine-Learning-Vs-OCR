import numpy as np
import cv2
import time
import json
from openalpr import Alpr

#us - para americano
#eu - para mercosul

def identifica_us_eu(str_padrao):
 autorizado = False
 alpr = Alpr(str_padrao, "openalpr.conf", "runtime_data")
 if not alpr.is_loaded():
     print("Error loading OpenALPR")
     sys.exit(1)
	    
 alpr.set_top_n(1)
 alpr.set_default_region("md")
 results = alpr.recognize_file("/home/marcos/Desktop/prototipo 3/placas mercosul/4.jpg")

 i = 0

 for plate in results['results']:
     i += 1
     for candidate in plate['candidates']:
	prefix = "-"
	if candidate['matches_template']:
	    prefix = "*"
	licPlate = results       
	
	print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))
	obj  = json.load(open("cadastros.json"))
	for i in xrange(len(obj)):
	    if obj[i]["id"] == candidate['plate']: # se encontrar no cadastro grava entrada
		autorizado = True
		with open('entradas.json') as data_file:    
		    old_data = json.load(data_file)
		    data = [{"placa": candidate['plate'],"dia": time.strftime("%d/%m/%Y"),"hora": time.strftime("%H:%M:%S"),"liberadopor": "Open VCR"}]
		data = old_data + data
		path = '/home/marcos/Desktop/prototipo 3'
		filePathNameWExt =  path + '/' + 'entradas' + '.json'
		with open(filePathNameWExt, 'w') as fp:
		   json.dump(data, fp)
		break
 if autorizado: 
 	print("   %12s %12s" % ("Placa", "Certeza"))  
 	print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))
	# printa dentro da funcao, so para demonstrar que identifica a placa, no final nao ira precisar desse print

 return autorizado

#alpr.unload()


str_padrao = "eu"
autorizado = identifica_us_eu(str_padrao)


if autorizado == True:
	print("Entrada liberada")
else:
    	#se nao encontrou com o padrao mercosul, tenta com o americano
	str_padrao = "us"
	autorizado = identifica_us_eu(str_padrao)
	if autorizado == True:
		print("Entrada liberada")
	else:
		print("Nao autorizado")










