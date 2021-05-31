from flask import Flask,jsonify,request
from main import *;
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello"

@app.route('/in/<data>')
def my_view_func(data):
    return data

@app.route("/getdata",methods=["POST","GET"])
def getdata():
    p_data = process(request.form.get("data"))
    print(p_data)
    return jsonify(p_data)

if __name__ == "__main__":
    app.run()