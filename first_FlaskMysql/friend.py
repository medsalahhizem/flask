# friend.py
from mysqlconnection import connectToMySQL

class Friend:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL('first_flaskmysql').query_db(query)
        friends = []
        for friend in results:
            friends.append(cls(friend))
        return friends
    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(occ)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('first_flaskmysql').query_db(query, data)
    def display(self):
      print("welcome kouba")
