from flask_app import app
from flask import render_template, redirect,request,session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/")
def start():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos=Dojo.get_all()
    return render_template("dojos.html",dojos=dojos)

@app.route("/dojoshow/<int:dojo_id>")
def dojoshow(dojo_id):
    data={
        "id":dojo_id
    }
    dojo=Dojo.get_one(data)
    ninjas=Ninja.get_some(data)
    return render_template("dojoshow.html",dojo=dojo,ninjas=ninjas)

@app.route("/createdojo", methods=["post"])
def newdojo():
    data={
        "name":request.form["name"],
    }
    Dojo.save(data)
    return redirect("/dojos")
