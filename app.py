from flask import Flask,jsonify,request
from flask.templating import render_template
from main import *;
from she import *;
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello"

@app.route('/in/<data>')
def my_view_func(data):
    return data

@app.route('/gps')
def gps_fun():
    return jsonify(gps())

@app.route("/getdata",methods=["POST","GET"])
def getdata():
    p_data = process(request.form.get("data"))
    print(p_data)
    return jsonify(p_data)

@app.route("/temp")
def temp():
    list = [2,3,4,1]
    return render_template("index.html",students=list)

@app.route("/sav",methods=["POST"])
def handle():
    f = request.files['file']
    f.save(f.filename)
    with open(f.filename,'r') as src:
        return jsonify(process(src.read()))

if __name__ == "__main__":
    app.run(debug=True)