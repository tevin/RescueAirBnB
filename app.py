from flask import Flask, request, render_template
from pymongo import MongoClient
from envparse import env
import os.path

app = Flask(__name__)


def mongo_login():
	if (os.path.exists('./env')):
		env.read_envfile('./env')
	mongo_uri = env('MONGO_URI')
	print mongo_uri
	client = MongoClient(mongo_uri)
	return client['rescuebnb']

@app.route('/')
def show_home():
    return render_template('starter.html')

@app.route('/hosts', methods = ['GET', 'POST'])
def hosts():
	if request.method == 'POST':
		add_host(request.form.to_dict())

	#return render_template('hosts.html')
	return render_template('starter.html')

def add_host(host):
	db = mongo_login()
	hosts = db.hosts
	host_id = hosts.insert_one(host).inserted_id

if __name__ == '__main__':
    app.run()
    #app.run(debug=True)