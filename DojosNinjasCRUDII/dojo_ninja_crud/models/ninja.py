from dojo_ninja_crud.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojos_id = data['dojos_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_ninjas_sql').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO ninjas (dojos_id,first_name, last_name, age)
        VALUES (%(dojos_id)s,%(first_name)s, %(last_name)s, %(age)s);
        """
        return connectToMySQL('dojos_ninjas_sql').query_db(query, data)

    @classmethod
    def get_by_dojo(cls, dojos_id):
        query = "SELECT * FROM ninjas WHERE dojos_id = %(dojos_id)s;"
        results = connectToMySQL('dojos_ninjas_sql').query_db(query, {'dojos_id': dojos_id})
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
      
    @classmethod
    def get_one_by_id(cls, ninja_id):
      #query for a ninja
      query = """SELECT * from ninjas
      WHERE id = %(ninja_id)s"""
      data = {
      "ninja_id": ninja_id
      }
      # make a ninja object... BUT must have the dojo id
      result_list = connectToMySQL('dojos_ninjas_sql').query_db(query,data)
      ninja = cls(result_list[0])
      return ninja
    
    @classmethod
    def delete_by_id(cls, ninja_id):
      query = """DELETE from ninjas
              WHERE id = %(ninja_id)s;"""
      data = {
      "ninja_id": ninja_id
      }
      connectToMySQL('dojos_ninjas_sql').query_db(query, data)
      return ninja_id
    
    @classmethod
    def update(cls, data):
      query = """UPDATE ninjas
              SET first_name = %(first_name)s, last_name = %(last_name)s , age= %(age)s, dojos_id= %(dojo_id)s
              WHERE id = %(id)s;
              """
      return  connectToMySQL('dojos_ninjas_sql').query_db(query, data)
      