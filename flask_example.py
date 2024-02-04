from flask import Flask

example_app = Flask(__name__)

AWS_PORT = 8080


@example_app.route('/')
def hello_world():
    return 'Hello Fellows October 2023.  Are you excited for the Hackathon?'


if __name__ == '__main__':
    example_app.run(host='0.0.0.0', port=AWS_PORT)
