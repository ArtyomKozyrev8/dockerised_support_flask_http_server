from flask import Flask, jsonify
import logging

app = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


@app.route("/")
def hello():
    app.logger.error("root dir")
    mes = jsonify({"result": "main root page"})
    return mes


@app.route("/xsup")
def x():
    app.logger.info("x dir")
    mes = jsonify({"result": "x support page"})
    return mes


@app.route("/ysup")
def y():
    app.logger.error("y dir")
    mes = jsonify({"result": "y support page"})
    return mes


if __name__ == '__main__':
    app.run("0.0.0.0", debug=False, port=11155)
