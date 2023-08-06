import os
from flask import Flask, request, jsonify
from minio import Minio
from minio.error import S3Error

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!!!"

@app.route('/backups')
def backups():
    client = Minio(os.getenv('S3_ENDPOINT'), os.getenv('S3_ACCESS_KEY'),
                   os.getenv('S3_SECRET_KEY'), secure=False)
    backup_exists = client.bucket_exists("discord-bot-data")
    
    if backup_exists:
        return "Discord backup found"
    else:
         return "Go a make a backup"

@app.route('/cache-me')
def cache():
    return "this will be nginx cache"

@app.route('/info')
def info():

	resp = {
		'connecting_ip': request.headers['X-Real-IP'],
		'proxy_ip': request.headers['X-Forwarded-For'],
		'host': request.headers['Host'],
		'user-agent': request.headers['User-Agent']
	}

	return jsonify(resp)

@app.route('/flask-health-check')
def flask_health_check():
	return "success"