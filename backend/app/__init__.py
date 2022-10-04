from flask import Flask

app = Flask(__name__) 

@app.route('/')
def default():
    return 'Welcome to my page'

app.run(port=5001)