from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello():
    return 'Hello, AWS Flask App!'

if __name__ == "__main__":
    application.run(debug=False, host='0.0.0.0', port=8000)