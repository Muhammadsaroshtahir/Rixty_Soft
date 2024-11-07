#class Cars:
#    def __init__(self, name, brand):
#        self.car_name = name
#        self.car_brand = brand
#
#    def __str__(self):
#        return f"{self.car_name}({self.car_brand})"
#
#c1 = Cars("Chiron", "Bugatti")
#print(c1) 

#class Cars:
#    def __init__(self,make,model):
#        self.make=make
#        self.model=model
#    
#    def start(self):
#        print(f"{self.make} {self.model} is starting...")
#    
#
#class car(Cars):
#    def __init__(self,make,model,doors):
#        super().__init__(make,model)
#        self.doors = doors
#    
#    def open_trunk(self):
#        print(f"{self.make}{self.model} trunk is now open.")
#
#
#my_car = car("Lamborghini","Aventador",2)
#my_car.start()
#my_car.open_trunk()
#my_car=print(f"Doors:{my_car.doors}")

# class Cars:
#     def vehicles(self):
#         print("Aventador")


# class Bike:
#     def vehicles(self):
#         print("Panigale V4s")

# def call(auto):
#     auto.vehicles()


# sarosh = Cars()
# ali = Bike()

# call(sarosh)
# call(ali)
class Vehicle:
    def vehicles(self):
        raise NotImplementedError("Subclasses must implement this method")

class Cars(Vehicle): 
    def vehicles(self):
        print("Aventador")  

class Bike(Vehicle): 
    def vehicles(self):
        print("Panigale V4s")

def call(auto):
    auto.vehicles()

sarosh = Cars()
ali = Bike()

call(sarosh)  
call(ali)    

