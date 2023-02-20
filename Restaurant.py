class Restaurant():


    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    

    def describe_restaurant(self):
        print(self.restaurant_name.title(), 'is serve ', self.cuisine_type)


    def open_restaurant(self):
        print(self.restaurant_name.title(), " is open. ")

r1 = Restaurant('macdano', 'amarcano')
print(type(r1))
r1.describe_restaurant()
print(type(r1.describe_restaurant()))
r1.open_restaurant()
print(type(r1.cuisine_type))
print('finish')