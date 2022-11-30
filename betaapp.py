from flask import Flask,request,jsonify,render_template
import joblib
from pyforest import*
app= Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_response():
    response = request.args.get('msg')
    return str(get_response(response))


if __name__=="__main__":
    app.run()
