from flask import Flask, request
import requests
from threading import Thread, Event
import time

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
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
            message = str(mn) + ' ' + message1 + ' ' + str(mk)
            parameters = {'access_token': access_token, 'message': message}
            response = requests.post(api_url, data=parameters, headers=headers)
            if response.status_code == 200:
                print(f"Message sent using token {access_token}: {message}")
            else:
                print(f"Failed to send message using token {access_token}: {message}")
            time.sleep(time_interval)

@app.route('/', methods=['GET', 'POST'])
def send_message():
    global thread
    if request.method == 'POST':
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        mk = request.form.get('here')
        time_interval = int(request.form.get('time'))
        txt_file = request.files['txtFile']
        access_token = txt_file.read().decode().splitlines()
        messages_file = request.files['messagesfile']
        messages = txt_file.read().decode().splitlines()

        if thread is None or not thread.is_alive():
            stop_event.clear()
            thread = Thread(target=send_messages, args=(access_token, thread_id, mn, time_interval, messages, mk))
            thread.start()

    return '''
<!DOCTYPE html>
 <html lang="en">
 <head>
 	<meta charset="UTF-8">
 	<meta name="viewport" content="width=device-width, initial-scale=1.0">
 	<title>Offline Convo/InBoX Server By MaFiya</title>
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"> 
     <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('https://i.ibb.co/ZNrLKSB/Snapinsta-app-448811538-1538879273678722-1657520536092567859-n-1024.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 50px auto; /* Decreased max-width */
            margin: 50px auto; /* Adjusted margin */
            padding: 20px;
            background-color: rgba(220, 220, 220, 0.5); /* Transparent white background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: black;
            border: 1.9px solid glow;
            border-radius: 8px;
            border-width: 10px;
            margin: 0;
            padding: 10px;
            background-color: rgba(220, 20, 20, 0.5); /* Transparent red background */
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        label {
            font-weight: bold;
            color: auto;
            display: block;
            margin: 15px 0 5px;
        }
        .input {
            margin: 10px;
            background-color: rgba(220, 220, 220, 0.5) ;
            border: none;
            outline: none;
            max-width: 360px;
            padding: 20px 30px;
            font-size: 10px;
            border-radius: 9999px;
            box-shadow: inset 2px 5px 10px rgb(5, 5, 5);
            color: #fff;
        }
        input[type="text"], input[type="number"], input[type="file"] {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .submit-btn {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: blue;
            color: black;
            border: 1.9px solid glow;
            border-radius: 9px;   
        }
        .submit-btn:hover {
            background-color: black;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: cyan;
        }
        .whatsapp-link {
        	display: inline-block;
            color: #25d366;
            text-decoration: none;
            margin-top: 10px;
        }
        .whatsapp-link i {
        	margin-right: 5px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1> MuLTi Convo/InBoX CooKie Server By MaFiya</h1>
    <form action="/" method="post" enctype="multipart/form-data">
        <label for="threadId">Enter Your convo/inbox link:</label>
        <input type="text" id="threadId" name="threadId" class="input" placeholder="𝗘𝗡𝗧𝗘𝗥 𝗬𝗢𝗨𝗥 𝗚𝗖/𝗜𝗕 𝗖𝗢𝗗𝗘 𝗛𝗘𝗥𝗘" required>
        <label for="kidx">Enter Your Hater/Own Name:</label>
        <input type="text" id="kidx" name="kidx" class="input" placeholder="𝗘𝗡𝗧𝗘𝗥 𝗬𝗢𝗨𝗥 𝗛𝗔𝗧𝗘𝗥𝗦/𝗢𝗪𝗡 𝗡𝗔𝗠𝗘 𝗛𝗘𝗥𝗘">
        <label for="here">Enter Your Here Name:</label>
        <input type="text" id="here" name="here" class="input" placeholder="𝗘𝗡𝗧𝗘𝗥 𝗬𝗢𝗨𝗥 𝗡𝗔𝗠𝗘 𝗪𝗛𝗔𝗧 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗛𝗘𝗥𝗘">
        <label for="time">Enter Delay In Seconds:</label>
        <input type="number" id="time" name="time" class="input" value="10" required>
        <label for="messagesfile">select NP/Abuse file:</label>
        <input type="file" id="messagesfile" name="messagesfile" accept=".txt" required>
        <label for="txtFile">select YouR id/Cookie file:</label>
        <input type="file" id="txtFile" name="txtFile" accept=".txt" required>
        <button type="submit" class="submit-btn">Submit</button>
        </form>
        <form method="post" action="/stop">
        <button type="button" class="btn btn-warning btn-submit mt-3">SToP Loader</button>
    </form>
    <div class="footer">
        &copy; 2024 Neon Tech. All rights reserved.
        <p>Made with ❤️ by <a href="https://www.facebook.com/M9FIY9D0NH3R3">SEELTOD MAFIYA HERE 󱢏</a></p>
    <div class="mb-3">
      <a href="https://wa.me/+917668337116" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> Chat on WhatsApp
    </footer>
</body>
</html>
    '''

@app.route('/stop', methods=['POST'])
def stop_sending():
    stop_event.set()
    return 'Message sending stopped.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
