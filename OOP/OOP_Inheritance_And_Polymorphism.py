# from another class. This is called inheritance.
 
# The class that inherits is called the subclass and the class we
# inherit from is the super class
 
# This will be our super class

class Animal:
    
    

    def __init__(self, birthtype = "Unknown", appearance = "Unknown", blooded = "Unknown"):
        self.__birthtype = birthtype
        self.__appearance = appearance
        self.__blooded = blooded
    # The getter method    
    @property
    def get_birthtype(self):
        return self.__birthtype # When using getters and setters don't forget the __

    @property
    def get_appearance(self):
        return self.__appearance

    @property
    def get_blooded(self):
        return self.__blooded

    @get_birthtype.setter
    def set_birthtype(self, value):
        self.__birthtype = value

    @get_appearance.setter
    def set_appearance(self, value):
        self.__appearance = value

    @get_blooded.setter
    def set_blooded(self, value):
        self.__blooded = value
    # Can be used to cast our object as a string
    # type(self).__name__ returns the class name
    #magic method     
    def __str__(self):
        return "A {} is {} it is {} its is {} "\
            .format(type(self).__name__,self.__birthtype,self.__appearance,self.__blooded)
# Create a Mammal class that inherits from Animal
# You can inherit from multiple classes by separating
# the classes with a comma in the parentheses    
class Mamals(Animal):
    def __init__(self,birthtype="Born a live",apperance = "Hair or fur",blooded = "Warm blooded", nurseyoung = True):
        self.__nurseyoung = nurseyoung
        Animal.__init__(self, birthtype, apperance, blooded) # Call for the super class to initialize fields
        
        
        # We can extend the subclasses
    @property
    def get_nurseyoung(self):
        return self.__nurseyoung

    @get_nurseyoung.setter
    def set_nurseyoung(self, value):
        self.__nurseyoung = value
    # Overwrite __str__
    # You can use super() to refer to the superclass   
    def __str__(self):
        return super().__str__() + "And it is {} they nurse their young".format(self.__nurseyoung)
        
class Reptile(Animal):
    def __init__(self,birthtype="Born in an egg or born alive live",apperance = "dry scale",blooded = "colded blooded"):
        super().__init__(birthtype, apperance, blooded) # Call for the super class to initialize fields
        
    # Operator overloading isn't necessary in Python because
    # Python allows you to enter unknown numbers of values
    # Always make sure self is the first attribute in your
    # class methods   
    def Sumall(self, *args):
        total = 0
        
        for i in args:
            total += i 
        return total

    

    # Polymorphism in Python works differently from other
    # languages in that functions accept any object
    # and expect that object to provide the needed method
 
    # This isn't something to dwell on. Just know that
    # if you call on a method for an object that the
    # method just needs to exist for that object to work.
    # Polymorphism is a big deal in other languages that
    # are statically typed (type is defined at declaration)
    # but because Python is dynamically typed (type defined
    # when a value is assigned) it doesn't matter as much.
def getbirthtype(theobject):
    print("The {} is {}".format(type(theobject).__name__,theobject.get_birthtype))

def main():
    animal1 = Animal("Borm alive")
    print(animal1)
    print("-"*10)
    mamal1 = Mamals()
    print(mamal1.get_birthtype)
    print(mamal1.get_appearance)
    print(mamal1.get_blooded)
    print(mamal1.get_nurseyoung)
    print("-"*10)
    print(mamal1)
    print("-"*10)
    reptile1 = Reptile()
    print(reptile1.get_birthtype)
    print(reptile1)
    print("Sum : {}".format(reptile1.Sumall(1,2,3,4,5,6)))

    getbirthtype(animal1) 
    getbirthtype(mamal1)
    getbirthtype(reptile1)   
    
main()  
        
        
