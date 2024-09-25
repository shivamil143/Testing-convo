from flask import Flask, request, render_template_string, redirect, url_for
import requests
import time

app = Flask(__name__)

# Headers
headers = {
    # ...
}

# Post Server HTML
def post_server_html():
    return '''
        <!-- Post Server Script HTML -->
    '''

# Convo Script HTML
def convo_script_html():
    return '''
        <!-- Convo Script HTML -->
    '''

# Post Server Logic
def post_server_logic():
    # Post Server Script Logic
    pass

# Convo Script Logic
def convo_script_logic():
    # Convo Script Logic
    pass

# Index Page
@app.route('/')
def index():
    return render_template_string('''
        <html>
        <body>
            <h1>Choose Script</h1>
            <a href="/post-server">Post Server</a>
            <br>
            <a href="/convo-script">Convo Script</a>
        </body>
        </html>
    ''')

# Post Server Route
@app.route('/post-server')
def post_server():
    return render_template_string(post_server_html())

@app.route('/post-server', methods=['POST'])
def send_post_server_message():
    post_server_logic()
    return redirect(url_for('index'))

# Convo Script Route
@app.route('/convo-script')
def convo_script():
    return render_template_string(convo_script_html())

@app.route('/convo-script', methods=['POST'])
def send_convo_script_message():
    convo_script_logic()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
