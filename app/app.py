from flask import Flask, render_template, request

app = Flask(__name__, static_folder='.', static_url_path='')

THRESHOLD = 1500

@app.route('/')
def index():
    if get_co2() > THRESHOLD:
        message = '混雑しています'
    else:
        message = '空いています'

    return render_template('index.html', state=message)

def get_co2():
    return 1000


app.run(port=8000, debug=True)