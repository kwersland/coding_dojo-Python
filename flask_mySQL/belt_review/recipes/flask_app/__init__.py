from flask import Flask
DATABASE = "users_and_recipes_schema"
app = Flask(__name__)
app.secret_key = "don't tell secrets"

