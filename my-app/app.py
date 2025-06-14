from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "This is for Phase 02 Project 05"
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
