from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'welcome to the continental grou0000000nds john!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
