from BURGERS.config.mysqlconnection import connectToMySQL
from BURGERS.models import topping

class Burger:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # We now create a list so that later we can add in all the topping objects that relate to a burger.
        self.toppings = []
        self.restaurant = None
    # This method will retrieve the burger with all the toppings that are associated with the burger.
    @classmethod
    def get_burger_with_toppings(cls, data):
        query = "SELECT * FROM burgers LEFT JOIN add_ons ON add_ons.burger_id = burgers.id LEFT JOIN toppings ON add_ons.topping_id = toppings.id WHERE burgers.id = %(id)s;"
        results = connectToMySQL('burgers').query_db(query, data)
        # results will be a list of topping objects with the burger attached to each row. 
        burger = cls( results[0] )
        for row_from_db in results:
            # Now we parse the topping data to make instances of toppings and add them into our list.
            topping_data = {
                "id": row_from_db["toppings.id"],
                "topping_name": row_from_db["topping_name"],
                "created_at": row_from_db["toppings.created_at"],
                "updated_at": row_from_db["toppings.updated_at"]
            }
            burger.toppings.append( topping.Topping( topping_data ) )
        return burger

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers;"
        results = connectToMySQL('burgers').query_db(query)
        burgers = []
        for row in results:
            burgers.append(cls(row))
        return burgers
