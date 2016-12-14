#!/usr/bin/env python
# -*- coding: utf-8 -*-
# app.py

from flask import Flask, request
from flask.ext.cors import CORS, cross_origin
from Crypto.Cipher import AES
import base64
import sys 

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
	return 'Error : URI vacía'

@app.route('/encode', methods=['GET', 'POST'])
def encode():
	key = request.args.get('key')
	texto = request.args.get('texto')
	cipher = AES.new(key,AES.MODE_ECB)
	
	return base64.b64encode(cipher.encrypt(texto.rjust(32)))

@app.route('/decode', methods=['GET', 'POST'])
def decode():
	key = request.args.get('key')
	texto = request.args.get('texto')
	cipher = AES.new(key,AES.MODE_ECB)
	
	return cipher.decrypt(base64.b64decode(texto)).strip()
	
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)