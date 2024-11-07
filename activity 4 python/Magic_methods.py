# __init__ like double underscore methods are called magic or dunder methods.
# mainly in the classes.
# automatically called by suing python operation
# printing
# equal objects
# less then or greater then

class cars:

    def __init__(self, brand, model, price, type):
        self.brand=brand
        self.model=model
        self.price=price
        self.type=type

    def __str__(self):
        return f"'{self.brand}'cost'{self.price}'"
    
    def __eq__(self,other):
        return self.brand==other.brand and self.price==other.price

    def __lt__(self,other):
        return self.price < other.price
    
    def __gt__(self,other):
        return self.price > other.price
    
    def __add__(self,other):
        return f"{self.price + other.price} price"
    
    def __contains__(self,keyword):
        return keyword in self.brand or keyword in self.author
    
    def __getitem__(self, key):
        if isinstance(key, tuple): 
            return {k: self[k] for k in key} 
        if key == "brand":
              return self.brand
        elif key == "model":
             return self.model
        elif key == "price":
            return self.price
        elif key == "type":
            return self.type
        else:
            raise KeyError(f"'{key}' not found")
    

car1 = cars("Lamborghini","2020", 260000,"Coupe")
car4 = cars("Lamborghini","2020", 260000,"Coupe")
car2 = cars("BMW","2024", 160000,"Sedan")
car3 = cars("Audi","2020", 130000,"Sedan")

#print(car1) we get the memory address
print(car1)
print(car1 == car4)
print(car1 < car2)
print(car1 > car2)
print(car1+car2)
print("Audi" in car3)   
print(car2["brand","model"])    
    