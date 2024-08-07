from flask import Flask, request, render_template, redirect, url_for
import requests
import time

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		username == "MR M4FIY4"
		password == "M4FIY4"
		if username == password:
			return redirect(url_for('choose_method'))
		else:
			return render_template('login.html', error="Incorrect Password! Try again.")
	return render_template('login.html')
@app.route('/choose_method', methods=['GET'])
def choose_method():
	if request.method == 'GET':
		return render_template("index.html")
		
@app.route('/convo_token', methods=['GET'])
def convo_loader():
	if request.method = 'GET':
		return render_template("convo.html")

@app.route('/post_token', methods=['GET'])
def post_loader():
	#Handel From Post Server Submission
	print("POST SERVER FORM SUCCESSFULLY SUBMITTED")
	return"POST SERVER FORM SUCCESSFULLY SUBMITTED"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
