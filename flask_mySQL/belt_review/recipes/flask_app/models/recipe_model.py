from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash #part of data validation
import re #regex access



class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    #Create
    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (name, description, instructions, under_30, user_id, created_at) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30)s, %(user_id)s, %(created_at)s);"
        return connectToMySQL(DATABASE).query_db(query, data)


    #Recipe edit
    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, under_30 = %(under_30)s, created_at = %(created_at)s" \
        " WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


    #Get recipe id
    @classmethod
    def get_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return cls(results[0])


    # Delete Recipe
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        return results


    #Get all with users
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_recipes = []
        for recipe_row in results:
            recipe_instance = cls(recipe_row)
            all_recipes.append(recipe_instance)
        return results

    #Get one with user
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results[0]


    # validations
    @staticmethod
    def validate(recipe_data):
        is_valid = True
        if len(recipe_data['name']) < 3:
            flash("Name must be at least 3 characters", "name")
            is_valid = False
        if len(recipe_data['description']) < 3:
            flash("Description cannot be blank", "description")
        if len(recipe_data['instructions']) < 3:
            flash("Please provide instructions", "instructions")
            is_valid = False
        if not recipe_data['created_at']:
            flash("Please provide a date", "date_made")
            is_valid = False
        return is_valid