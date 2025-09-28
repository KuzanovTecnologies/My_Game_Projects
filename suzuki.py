class Bike:
    name = ''
    color = ' '
    price = 0
    def info(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
        print("{}: {} and".format(self.name,self.color,self.price))

class Bike:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def info(self):
        print("{}: {} and {}".format(self.name,self.color,self.price))

class Bike:
    def __init__(self):
        self.__updateTech()
    def Ride(self):
        print("Riding...")
    def __updateTech(self):
        print("Updating your Bike..")

class Bike:
    __name = " "
    __color = " "
    def __init__(self,name,color):
        self.__name = name
        self.__color = color
    def info(self):
        print("{} is of {} color".format(self.__name,self.__color))

class Bike:
    __name = " "
    __color = " "
def __init__(self,name,color):
    self.__name = name
    self.__color = color
def setNewColor(self, color):
    self.__color = color
def info(self):
    print("{} is of {} color".format(self.__name,self.__color))

class Child_class(Parent_class):
    <child-class-members>

class Child_class(Base_class1, Base_class2, Base_class3 .....):
    <child-class-members>

class Bike:
    def __init__(self):
        print("Bike is starting..")
    def Ride(self):
        print("Riding...")

class Suzuki(Bike):
    def __init__(self):
        self.name = name
        self.color = color
    def info(self):
        print("You are riding {0} and it's color is
        {1}".format(self.name,self.color")

#Save above code in python file and Run it

class Bike:
    def __init__(self):
        print("Bike is starting..")
    def Ride(self):
        print("Riding...")

class Suzuki(Bike):
    def __init__(self,name,color):
        self.name = name
        self.color = color
        super().__init__()

class Mobile:
    def __init__(self):
        print("Mobile features: Camera, Phone, Applications")
class Samsung(Mobile):
    def __init__(self):
        print("Samsung Company")
        super().__init__()
class Samsung_Prime(Samsung):
    def __init__(self):
        print("Samsung latest Mobile")
        super().__init__()
class Bird:
    def about(self):
        print("Species: Bird")
    def Dance(self):
        print("Not all but some birds can dance")
class Peacock(Bird):
    def Dance(self):
        print("Peacock can dance")
class Sparrow(Bird):
    def Dance(self):
        print("Sparrow can't dance")