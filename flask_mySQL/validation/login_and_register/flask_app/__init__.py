from flask import Flask
DATABASE = "newusers_schema"
app = Flask(__name__)
app.secret_key = "don't tell secrets"

