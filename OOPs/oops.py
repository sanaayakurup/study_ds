# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 18:30:45 2022

@author: sanaayak
https://alpopkes.com/posts/python/magical_universe/day_1_first_post_oop/

"""
#classes are blueprints-the give the structure of the object

#create a class
class CastleKilmereMember:
    pass

#create an instance of a class
kilmere_member =CastleKilmereMember()

#there are no attributes of the class 
class CastleKilmereMember:
    def __init__(self,name, birthyear, sex):
        self.name=name
        self.birthyear=birthyear
        self.sex=sex
        
    def says(self,word):
        return(f'{self.name} says {word}')

bromley = CastleKilmereMember('Bromley Huckabee', 1959, 'male')
print(bromley.says("Hello!"))
        
#Type annotation
##add metadata to your classes-control the type of inputs and returns 
class CastleKilmereMember_withannotation():
    def __init__(self, name:str):
        self.name=name
        
    def sayname(self)->str:
        return f'my name is {self.name}'
    


trial=CastleKilmereMember_withannotation(12)
trial.name.type

#type annotations are jsut annotations-no checking going on 

-------------Inheritance-------------

-Create a class that can inherit the attributes of another class 
-this helps in code reusing and keeping it clean 

class Pupil(CastleKilmereMember):
    """ Create a Castle Kilmere Pupil """

    def __init__(self, name, birthyear, sex, start_year, pet=None):
        super().__init__(name, birthyear, sex)
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._elms = {
                  'Critical Thinking': False,
                  'Self-Defense Against Fresh Fruit': False,
                  'Broomstick Flying': False,
                  'Magical Theory': False,
                  'Foreign Magical Systems': False,
                  'Charms': False,
                  'Defence Against Dark Magic': False,
                  'History of Magic': False,
                  'Potions': False,
                  'Transfiguration': False}
            
            
luke = Pupil(name='Luke Bery',
              birthyear=2008,
              sex='male',
              start_year=2020,
              pet=('Cotton', 'owl'))


class CastleKilmereMember:
    def __init__(self, name: str, birthyear: int, sex: str):
    	...
        
    def says(self, words: str) -> str:
        return f"{self.name} says: {words}"
    
    
    
    
 #decorators 
#used to extend or modify the functionality of an already existing function
#it is a function that takes in a function and returns one 
#some examples below 
# https://dbader.org/blog/python-decorators

def say_sup(function):
    def wrapper():
        original_output=function()
        new_output=original_output + ' ssup!'
        return new_output 
    return wrapper 


@say_sup
def say_hello():
    return('Hi')

say_hello()


##adding inputs to decorators 
def say_sup(function):
    def wrapper(*args,**kwargs):
        original_function_op=function(*args,**kwargs)
        new_function_op=original_function_op+',then says bye'
        return new_function_op
    return wrapper

@say_sup 
def say_name(person,word):
    return f"{person} says {word}"

say_name('san','ban')
    

#Here’s a slightly more complex decorator which converts the result of the decorated function to uppercase letters:

#the plain function 
def give_a_word(word):
    return word
give_a_word('henlo')

#now we want to modify this to make it all into uppercase-without changing the original function 
#we do this by creating a decorator function
def make_uppercase(function):
    def wrapper(*args,**kwargs):
        input_from_function=function(*args,**kwargs)
        converted_output=input_from_function.upper()
        return converted_output
    return wrapper 

#the decorated plain function -now with extended features
@make_uppercase
def give_a_word(word):
    return word
give_a_word('henlo')


##polymorphism
class Bird:
     def intro(self):
       print("There are different types of birds")
 
     def flight(self):
       print("Most of the birds can fly but some cannot")
 
class parrot(Bird):
     def flight(self):
       print("Parrots can fly")
 
class penguin(Bird):
     def flight(self):
       print("Penguins do not fly")
 
obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()
 
obj_bird.intro()
obj_bird.flight()
 
obj_parr.intro()
obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()

#encapsulation
#private and protected variables 
protected-single underscore
private-double underscore 

class trial:
    def __init__(self,name,age):
        self.__name=name #private
        self._age=age #protected 
        
 obj1=trial('san',11)       
obj1._age #accessing the protected variable 
obj1._trial__name #accesing the private var 


##@p#roperty-getter and setter
#https://powerfulpython.com/blog/python-properties-refactoring/
class Money:
    def __init__(self,dollars,cents):
        self.dollars=dollars
        self.cents=cents
        
money = Money(27, 12)
message = "I have {:d} dollars and {:d} cents."
print(message.format(money.dollars, money.cents))
# "I have 27 dollars and 12 cents."

#This class was packaged into a library, and over time, was used in many different pieces of code, in many different applications. For example, one developer on another team - Bob - used it this way in his code:

money.dollars += 2
money.cents += 20
print(message.format(money.dollars, money.cents))
# "I have 29 dollars and 32 cents."        



# Fast forward a few months or years. Alice needs to refactor the internals of the Money class. Instead of keeping track of dollars and cents, she wants the class to just keep track of cents, because it will make certain operations much simpler. Here's the first change she might try to make:
# Second version of Money class.
class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

#This change has a consequence: every line of code referencing a Money object's dollars has to be changed. Sometimes when this happens, you're luckily the maintainer of all the code using this class, and you merely have a refactoring job on your hands
# Fortunately, Alice knows a better way, which will let her avoid the whole more-fun-than-going-to-the-dentist thing: The built-in property decorator. @property is applied to a method, and effectively transforms an attribute access into a method call. Let me show you an example. Push that Money class onto your mental stack for a moment, and imagine instead a class representing a person
class Person:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        
    @property
    def full_name(self): #instance method 
        return f'my full name is {self.first} {self.last}'

buddy= Person('Jonathan', 'Doe')
buddy.full_name     #this is kind of a dynamic attribute 
#Note that even though full_name is defined as a method, it is accessed like a member variable attribute. There are no parenthesis in that last line of code; I'm not invoking the method. What we've done is create a kind of dynamic attribute.

#back to the money class 
class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    # Getter and setter for dollars...
    @property
    def dollars(self):
        return self.total_cents // 100
    
    @dollars.setter
    def dollars(self, new_dollars):
        self.total_cents = 100 * new_dollars + self.cents

    # And the getter and setter for cents.
    @property
    def cents(self):
        return self.total_cents % 100
    @cents.setter
    def cents(self, new_cents):
        self.total_cents = 100 * self.dollars + new_cents   


# What does Bob's code look like now? Exactly the same!
# His code is COMPLETELY UNCHANGED, yet works
# with the final Money class. High five!
money = Money(27, 12)
message = "I have {:d} dollars and {:d} cents."
print(message.format(money.dollars, money.cents))
# "I have 27 dollars and 12 cents."

money.dollars += 2
money.cents += 20
print(message.format(money.dollars, money.cents))
# "I have 29 dollars and 32 cents."

# This works correctly, too.
money.ceNnts += 112
print(message.format(money.dollars, money.cents))
# "I have 30 dollars and 44 cents."



#######abstract classses
from abc import ABC, abstractmethod
# Python program showing
# abstract base class work
https://www.geeksforgeeks.org/abstract-classes-in-python/       
 
 
class Polygon(ABC):
 
    @abstractmethod
    def noofsides(self):
        pass
 
class Triangle(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
 
class Pentagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
 
class Hexagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")
 
class Quadrilateral(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")
 
# Driver code
R = Triangle()
R.noofsides()
 
K = Quadrilateral()
K.noofsides()
 
R = Pentagon()
R.noofsides()
 
K = Hexagon()
K.noofsides()

# Python program showing
# implementation of abstract
# class through subclassing
# Python program invoking a
# method using super()
 
import abc
from abc import ABC, abstractmethod
 
class R(ABC):
    def rk(self):
        print("Abstract Base Class")
 
class K(R):
    def rk(self):
        super().rk()
        print("subclass ")
 
# Driver code
r = K()
r.rk() 
# In the above program, we can invoke the methods in abstract classes by using super(). 

# Python program showing
# abstract properties
 
import abc
from abc import ABC, abstractmethod
 
class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"
class child(parent):
    @property
    def geeks(self):
        return "child class"
  
  
try:
    r =parent()
    print( r.geeks)
except Exception as err:
    print (err)
  
r = child()
print (r.geeks)
