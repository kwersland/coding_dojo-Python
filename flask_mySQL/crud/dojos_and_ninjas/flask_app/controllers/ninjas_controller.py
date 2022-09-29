from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo


#Create New Ninja
@app.route("/ninjas")
def ninja_form():
    all_dojos = Dojo.get_all()
    return render_template("new_ninja.html", dojos = all_dojos)

# Process form and redirect to dojo
@app.route("/ninjas/new", methods=["POST"])
def newNinja():
    if not Ninja.validate(request.form):
        return redirect('/ninjas')
    new_ninja_id = Ninja.create(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")
