from flask import Flask
DATABASE = "users_schema"
app = Flask(__name__)
app.secret_key = "its_a_secret"