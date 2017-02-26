import logging  # library

import facebookfeed

from flask import Flask, render_template  # for flask

from flask_ask import Ask, statement, question, session  # to initiate flask skills

app = Flask(__name__)  # initializing object named flask

ask = Ask(app, "/")

app.config['ASK_VERIFY_REQUESTS'] = False  # disables certificate ssl authentication

logging.getLogger("flask_ask").setLevel(logging.DEBUG)  # to log any bugs

facebooksession = facebookfeed.FacebookUser()



@ask.launch  # called when program is launched
def new_session():  # def stands for function

    # if facebooksession.set:

    welcome_msg = render_template('welcome')  # assigns a variable and goes to what alexa says

    return question(welcome_msg)  # when alexa says the message

    # else:
    #     print(session)
    #
    #     failure_msg = render_template('loginFailure')
    #     return statement(failure_msg)

@ask.intent("readDirections")
def help():
    directions_msg = render_template('directions')
    return question(directions_msg)

@ask.intent("Directive")
def directive():
    dir_msg = render_template('directive')
    return question(dir_msg)

@ask.intent("ReadingIntent")
def read():
    read_msg = render_template('read')
    return question(read_msg)


@ask.intent("SearchIntent")
def search():
    search_msg = render_template('search')
    return question(search_msg)

if __name__ == '__main__':
    app.run(debug=True)
