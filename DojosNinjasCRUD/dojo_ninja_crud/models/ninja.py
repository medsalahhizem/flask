# flask_app/models/ninja.py

from dojo_ninja_crud.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
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
        INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW());
        """
        return connectToMySQL('dojos_ninjas_sql').query_db(query, data)

    @classmethod
    def get_by_dojo(cls, dojo_id):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;"
        results = connectToMySQL('dojos_ninjas_sql').query_db(query, {'dojo_id': dojo_id})
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
