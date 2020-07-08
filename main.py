from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.error("root dir")
    res = jsonify({"result": "main root page"})
    return res


@app.route("/xsup")
def x():
    app.logger.info("x dir")
    res = jsonify({"result": "x support page"})
    return res


@app.route("/ysup")
def y():
    app.logger.error("y dir")
    res = jsonify({"result": "y support page"})
    return res


if __name__ == '__main__':
    app.run("0.0.0.0", debug=False, port=11155)
