from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo


#Read All Route
@app.route("/")
def index():
    all_dojos = Dojo.get_all()
    return render_template("index.html", dojos=all_dojos)


#Create a Dojo
@app.route("/dojos/new", methods=["POST"])
def newDojo():
    new_dojo_id = Dojo.create(request.form)
    return redirect("/")


#Display one Dojo
@app.route("/dojos/<int:id>")
def one_dojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.read_one(data)
    return render_template("one_dojo.html", dojo=dojo)
