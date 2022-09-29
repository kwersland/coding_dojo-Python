from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user_model import User


# Read All Route
@app.route("/")
def home():
    return redirect("/dojos")

@app.route("/dojos")
def index():
    all_users = User.get_all()
    return render_template("index.html", users = all_users)


# Create a User
@app.route("/users/new") #display route to render the form
def newUser_form():
    return render_template("new_user.html")

@app.route("/users/create", methods=["POST"]) #action route
def create():
    new_user_id = User.create(request.form)
    return redirect(f"/users/{new_user_id}")


# Show One User
@app.route("/users/<int:id>")
def display_one(id):
    data = {
        "id": id
    }
    user = User.read_one(data)
    return render_template("one_user.html", user=user)


#Edit User
@app.route("/users/<int:id>/edit")
def edit_user(id):
    data = {
    "id": id
    }
    this_user = User.read_one(data)
    return render_template("edit_user.html", user=this_user)

@app.route("/users/<int:id>/update", methods=["POST"])
def update_user(id):
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id": id
    }
    User.update(data)
    return redirect("/")


# Delete
@app.route("/users/<int:id>/delete")
def delete_user(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect("/")
