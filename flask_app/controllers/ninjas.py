from flask_app import app
from flask import render_template, redirect,request,session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/ninja")
def ninjas():
    dojos=Dojo.get_all()
    return render_template("new_ninja.html",dojos=dojos)

@app.route("/addninja",methods=["post"])
def newninja():
    data={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "age":request.form["age"],
        "dojo_id":request.form["dojo"]
    }
    Ninja.save(data)
    return redirect ("/dojos")
