from flask import Flask

example_app = Flask(__name__)

LOCAL_RUN = True
AWS_PORT = 5000


@example_app.route('/')
def hello_world():
    return 'Hello Fellows October 2021.  Great to see you.  This is cool'


if __name__ == '__main__':

    if LOCAL_RUN:
        example_app.run()
    else:
        example_app.run(host='0.0.0.0', port=AWS_PORT)
