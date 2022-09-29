from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
# bcrypt.generate_password_hash(password_string) #Generates hash for password
# bcrypt.check_password_hash(hashed_password, password_string) #checks for current hashed password


# home/index route
@app.route('/')
def index():
    if 'user_id' in session:
        user = session['user_id']
        return redirect('/welcome')
    return render_template('index.html')


# Login successful
@app.route('/welcome')
def welcome():
    all_recipes = Recipe.get_all()
    if not 'user_id' in session:
        return redirect('/')
    data = {
        'id': session['user_id']
    }
    user = User.get_by_id(data)
    return render_template('welcome.html', recipes = all_recipes, user=user)


# Register
@app.route('/register', methods=['POST'])
def register():
    if not User.validate(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.create(data)
    session['user_id'] = user_id
    return redirect("/welcome")


# logout
@app.route('/logout')
def logout():
    del session['user_id']
    return redirect('/')


# login
@app.route('/login', methods = ['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Credentials", "log")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Credentials", "log")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/welcome')


