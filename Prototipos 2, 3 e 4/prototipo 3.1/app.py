#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, request, url_for, redirect
import json
import time

app = Flask(__name__)

#data = jsondata.json
@app.route("/")
@app.route("/home")
def home():

	with open('file-name.json') as data_file:    
	    data = json.load(data_file)

	columns = [
	  {
	    "field": "placa", # which is the field's name of data key 
	    "title": "placa", # display as the table header's name
	    "sortable": True,
	  },
	  {
	    "field": "hora",
	    "title": "hora",
	    "sortable": True,
	  },
	  {
	    "field": "dia",
	    "title": "dia",
	    "sortable": True,
	  }
	  
	]

	return render_template("table.html",
	      data=data,
	      columns=columns,
	      title='Entradas')



@app.route("/")
@app.route("/cadastrar")
def cadastrar():
	return render_template("cadastro.html")

def voltar():
	return render_template("home")

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
	if request.method == "POST":
	        id = (request.form.get("id"))
		ano = (request.form.get("ano"))
		cor = (request.form.get("cor"))
		modelo = (request.form.get("modelo"))

		with open('cadastros.json') as data_file:    
	    	    old_data = json.load(data_file)

        data = [{"id": id, "ano": ano, "cor": cor, "modelo": modelo}]
	data = old_data + data
	path = '/home/marcos/Desktop/apresentacao TCC (copy)'
	filePathNameWExt =  path + '/' + 'cadastros' + '.json'
	with open(filePathNameWExt, 'w') as fp:
		json.dump(data, fp)		
	
		return redirect(url_for("home"))




@app.route("/atualizar/<string:id>", methods=['GET', 'POST'])
def atualizar(id):
	
	caranos = carano = (request.form.get("ano"))
	carro= {}
	obj  = json.load(open("cadastros.json"))

	for i in xrange(len(obj)):
	    if obj[i]["id"] == id:
		carid = id
		carano = obj[i]["ano"]
		carcor = obj[i]["cor"]
		carmodelo = obj[i]["modelo"]
		carro = ({'id': carid, 'ano': carano, 'cor': carcor, 'modelo': carmodelo})
		if caranos != None:		
		   obj.pop(i)
		break


	
	open("cadastros.json", "w").write(
	    json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
	) 
		

	
	
	if request.method == "POST":
	        carid = (request.form.get("id"))
		carano = (request.form.get("ano"))
		carcor = (request.form.get("cor"))
		carmodelo = (request.form.get("modelo"))
		
		with open('cadastros.json') as data_file:    
	    	    old_data = json.load(data_file)

		data = [{"id": carid, "ano": carano, "cor": carcor, "modelo": carmodelo}]
		data = old_data + data
		path = '/home/marcos/Desktop/apresentacao TCC (copy)'
		filePathNameWExt =  path + '/' + 'cadastros' + '.json'
		with open(filePathNameWExt, 'w') as fp:
			json.dump(data, fp)		
	if caranos == None:
		return render_template("atualizar.html", carro=carro)
	return redirect(url_for("home"))




@app.route("/lista")
def lista():
	with open('cadastros.json') as data_files:    
	    carro = json.load(data_files)

	columns1 = [
	  {
	    "field": "id", # which is the field's name of data key 
	    "title": "id", # display as the table header's name
	    "sortable": True,
	  },
	  {
	    "field": "ano",
	    "title": "ano",
	    "sortable": True,
	  },
	  {
	    "field": "cor",
	    "title": "cor",
	    "sortable": True,
	  },
	  {
	    "field": "modelo",
	    "title": "modelo",
	    "sortable": True,
	  }
	  
	]

	return render_template("lista.html", carro=carro)


@app.route("/excluir/<string:id>")
def excluir(id):

	#print(id)
	obj  = json.load(open("cadastros.json"))

	for i in xrange(len(obj)):
	    if obj[i]["id"] == id:
		obj.pop(i)
		break

	open("cadastros.json", "w").write(
	    json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
	)
	
	with open('cadastros.json') as data_files:    
	    carro = json.load(data_files)

	columns1 = [
	  {
	    "field": "id", # which is the field's name of data key 
	    "title": "id", # display as the table header's name
	    "sortable": True,
	  },
	  {
	    "field": "ano",
	    "title": "ano",
	    "sortable": True,
	  },
	  {
	    "field": "cor",
	    "title": "cor",
	    "sortable": True,
	  },
	  {
	    "field": "modelo",
	    "title": "modelo",
	    "sortable": True,
	  }
	  
	]
	

	return redirect(url_for("home"))
	#return render_template("lista.html", carro=carro)







if __name__ == "__main__":
	app.run(debug=True)
