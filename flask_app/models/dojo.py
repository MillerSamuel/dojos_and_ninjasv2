from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and)ninjas_schema').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name ,  created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and)ninjas_schema').query_db( query, data )

    @classmethod
    def get_one(cls,data):
        query="SELECT * FROM dojos WHERE id=%(id)s;"
        result=connectToMySQL('dojos_and)ninjas_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET name=%(name)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('dojos_and)ninjas_schema').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query="DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL('dojos_and)ninjas_schema').query_db(query,data)