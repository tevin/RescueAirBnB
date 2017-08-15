from flask import Flask, request, render_template, redirect
from pymongo import MongoClient
from envparse import env
from flask_httpauth import HTTPDigestAuth
import os.path


# Get env vars stored either in an env file or on the machine
def get_env(name):
	if (os.path.exists('./env')):
		env.read_envfile('./env')
	return env(name)

app = Flask(__name__)
app.config['SECRET_KEY'] = get_env('SECRET_KEY')
users = users = {
    "admin": get_env('ADMIN_PASS')
}
auth = HTTPDigestAuth()

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


# Utility method for mongo connections
def mongo_login():
	mongo_uri=get_env('MONGO_URI')
	client = MongoClient(mongo_uri)
	return client['rescuebnb']

# Home page with host form
@app.route('/')
def show_home():
	return render_template('index.html')

# Post endpoint for committing host to db
@app.route('/addhost', methods = ['GET', 'POST'])
def hosts():
	if request.method == 'POST':
		db = mongo_login()
		hosts_collection = db.hosts
		host = request.form.to_dict()
		hosts_collection.insert_one(host) # should probably check for completed insert
		return redirect('/')
	return render_template('addhosts.html')

# Post endpoint for committing people who need shelter to db
@app.route('/requestshelter', methods = ['GET', 'POST'])
def guests():
	if request.method == 'POST':
		db = mongo_login()
		guest_collection = db.guests
		guest = request.form.to_dict()
		guest_collection.insert_one(guest) # should probably check for completed insert
		return redirect('/')
	return render_template('request_shelter.html')

# Get involved page
@app.route('/getinvolved')
def get_involved():
	return render_template('get_involved.html')

# Get involved page
@app.route('/volunteer')
def volunteer():
	return render_template('volunteer.html')

# "Secured" endpoint for viewing registered hosts
@app.route('/hosts')
@auth.login_required
def viewhosts():
	db = mongo_login()
	hosts_collection = db.hosts
	guests_collection = db.guests
	
	return render_template('viewhosts.html', hosts=list(hosts_collection.find()),
		guests=list(guests_collection.find()))

@app.route('/ussd')
def ussd():
	return render_template('index.html')

if __name__ == '__main__':
	app.run()
    #app.run(debug=True)