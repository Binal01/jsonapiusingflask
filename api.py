from flask import Flask
import os
from flask import request, jsonify,make_response, render_template




app = Flask(__name__)

Data = { }

Data ['1']= {
	"Name": "Binal",
	"Age":29,
	"favouritenumber": 7,
	"favourite colour": "blue"
},
Data ['2']= {
	"Name": "Kushal",
	"Age":30,
	"favouritenumber": 5,
	"favourite colour": "red"
}

@app.route("/",methods = ['GET'])
def home():
	return render_template('./index.html')

@app.route("/all",methods = ['GET'])
def display():
	return jsonify(Data)


@app.route('/data/<obj>',methods = ['GET'])
def display_part(obj):
	if obj in Data:
		res = make_response(jsonify(Data[obj]), 200)
		return res
	else:
		res = make_response(jsonify({"Error": "Object not found"}), 404)

	





