from flask import Flask

example_app = Flask(__name__)

LOCAL_RUN = False
AWS_PORT = 8080


@example_app.route('/')
def hello_world():
    return 'Hello Fellows June 2022.  Are you excited for the Hackathon?'


if __name__ == '__main__':

    if LOCAL_RUN:
        example_app.run()
    else:
        example_app.run(host='0.0.0.0', port=AWS_PORT)
