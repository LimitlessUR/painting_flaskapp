from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Painting:
    db_name = 'paintings'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.title = db_data['title']
        self.description = db_data['description']
        self.price = db_data['price']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO paintings (title, description, price, user_id) VALUES (%(title)s,%(description)s,%(price)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM paintings;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_paintings = []
        for row in results:
        
            all_paintings.append( cls(row) )
        return all_paintings

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM paintings WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )
    
    
    @classmethod
    def update(cls, data):
        query = "UPDATE paintings SET title=%(title)s, description=%(description)s, price=%(price)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM paintings WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_painting(painting):
        is_valid = True
        if len(painting['title']) < 3:
            is_valid = False
            flash("Title must be at least 3 characters","painting")
        if len(painting['description']) < 3:
            is_valid = False
            flash("description must have 3 characters","painting")
        if len(painting['price']) < 2:
            is_valid = False
            flash("price must be at least 2 dolla","painting")
        
        return is_valid