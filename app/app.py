from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'welcome to the continental ground mr wick!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
