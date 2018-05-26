from flask import Flask, render_template
import json

"""
A example for creating a Table that is sortable by its header
"""

app = Flask(__name__)

#data = jsondata.json 
with open('file-name.json') as data_file:    
    data = json.load(data_file)

# other column settings -> http://bootstrap-table.wenzhixin.net.cn/documentation/#column-options
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

#jdata=json.dumps(data)

@app.route('/')
def index():
    return render_template("table.html",
      data=data,
      columns=columns,
      title='Placas')


if __name__ == '__main__':
	#print jdata
  app.run(debug=True)
