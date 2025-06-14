from flask import Flask, jsonify
from calc import Calculator

app = Flask(__name__)

@app.route("/calc/add/<float:a>/<float:b>", methods=["GET"])
def add(a, b):
    return jsonify({"result": Calculator.add(a, b)})

@app.route("/calc/subtract/<float:a>/<float:b>", methods=["GET"])
def subtract(a, b):
    return jsonify({"result": Calculator.subtract(a, b)})

@app.route("/calc/multiply/<float:a>/<float:b>", methods=["GET"])
def multiply(a, b):
    return jsonify({"result": Calculator.multiply(a, b)})

@app.route("/calc/divide/<float:a>/<float:b>", methods=["GET"])
def divide(a, b):
    try:
        result = Calculator.divide(a, b)
        return jsonify({"result": result})
    except TypeError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/calc/power/<float:a>/<float:b>", methods=["GET"])
def power(a, b):
    return jsonify({"result": Calculator.power(a, b)})

@app.route("/calc/sqrt/<float:a>", methods=["GET"])
def sqrt(a):
    try:
        result = Calculator.sqrt(a)
        return jsonify({"result": result})
    except TypeError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/calc/log10/<float:a>", methods=["GET"])
def log10(a):
    try:
        result = Calculator.log10(a)
        return jsonify({"result": result})
    except TypeError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)