from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


# Read All Recipes
@app.route('/recipes')
def read_all():
    all_recipes = Recipe.get_all()
    if not 'user_id' in session:
        return redirect('/')
    return render_template('welcome.html', recipes = all_recipes)



# Read one recipe
@app.route('/recipes/<int:id>')
def read_one(id):
    data = {
        'id': id
    }
    user_data = {
        'id': session['user_id']
    }
    user = User.get_by_id(user_data)
    recipe = Recipe.get_one(data)
    return render_template('one_recipe.html', recipe = recipe, user = user)



# Create a recipe
@app.route('/recipes/create')
def create_recipe():
    return render_template('add_recipe.html')

@app.route('/recipes/new', methods = ['POST'])
def new_recipe():
    if not Recipe.validate(request.form):
        return redirect('/recipes/create')
    Recipe.create(request.form)
    return redirect("/welcome")



# Delete a recipe
@app.route('/recipes/delete/<int:id>')
def del_recipe(id):
    data = {
        'id': id
    }
    Recipe.delete_recipe(data)
    return redirect('/welcome')


#Edit Recipe
@app.route("/recipes/edit/<int:id>")
def edit_recipe(id):
    data = {
    "id": id
    }
    this_recipe = Recipe.get_recipe(data)
    return render_template("edit_recipe.html", recipe=this_recipe)

@app.route("/recipes/update/<int:id>", methods=["POST"])
def update_recipe(id):
    data = {
        ** request.form,
        "id": id
    }
    Recipe.update(data)
    return redirect("/welcome")


