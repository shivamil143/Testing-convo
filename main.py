from flask import Flask, render_template

app = Flask(__name__)

class AllInOneServerCreator:
    def __init__(self):
        pass

    def run(self):
        return "Server Creator Prem"

class SingleConvo:
    def __init__(self):
        pass

    def run(self):
        return "Single Convo"

@app.route('/')
def index():
    tools = [
        AllInOneServerCreator(),
        SingleConvo(),
  ]
    return render_template('index.html', tools=tools)

@app.route('/feature/<name>')
def feature(name):
    template_name = f"{name.lower().replace(' ', '_')}.html"
    return render_template(template_name, name=name)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
