from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash #part of data validation
import re #regex access
ALPHANUMERIC = re.compile(r"^[a-zA-Z0-9]+$") #No special Characters re


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #Create a Ninja
    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        ninja_id = connectToMySQL(DATABASE).query_db(query, data)
        return ninja_id


    # Validator
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['first_name']) < 1:
            is_valid = False
            flash("First Name must be provided", "err_first_name")
        elif not ALPHANUMERIC.match(data['first_name']):
            is_valid = False
            flash("First Name connot contain special characters", "err_first_name")
        if len(data['last_name']) < 1:
            is_valid = False
            flash("Last Name must be provided", "err_last_name")
        elif not ALPHANUMERIC.match(data['last_name']):
            is_valid = False
            flash("Last Name connot contain special characters", "err_last_name")
        # if int(data['age']) < 15:
        #     is_valid = False
        #     flash("Must be 15 to register")
        return is_valid