from flask import Flask, make_response
from Utils import SCORES_FILE_NAME,BAD_RETURN_CODE

app = Flask(__name__)


@app.route("/")
def content():
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read()
            scoreHtml = open("successScore.html").read().format(gameScore=score)
            return make_response(scoreHtml, 200)
    except:
        scoreHtml = open("errorScore.html").read().format(errorHtml="Something went wrong...")
        return make_response(scoreHtml, BAD_RETURN_CODE)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30000)
