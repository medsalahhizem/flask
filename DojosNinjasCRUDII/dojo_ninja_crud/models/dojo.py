from dojo_ninja_crud.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas=[]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_ninjas_sql').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_ninjas_sql').query_db(query, data)
        
    @classmethod
    def get_one_with_ninjas(cls, data):
      query = """
      SELECT * FROM dojos 
      LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id 
      WHERE dojos.id = %(id)s;
      """
      results = connectToMySQL('dojos_ninjas_sql').query_db(query, data)
      
      if not results:
          # If there are no results, return None or an empty Dojo object
          return None  # Or `return cls(data)` if you want to return an empty dojo object

      dojo = cls(results[0])
      for row in results:
          n = {
              'id': row['ninjas.id'],
              'first_name': row['first_name'],
              'last_name': row['last_name'],
              'age': row['age'],
              'dojos_id': row['dojos_id'],
              'created_at': row['ninjas.created_at'],
              'updated_at': row['ninjas.updated_at']
          }
          dojo.ninjas.append(Ninja(n))
      return dojo
