# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:20:19 2022

@author: sanaayak
"""
#https://www.listendata.com/2019/08/python-object-oriented-programming.html

#Example 1 : Create Car Class class : car attributes : year, mpg and speed methods : accelerate and brake
#object : car1

class car:
    def __init__(self,year,mpg,speed):
        self.year=year
        self.mpg=mpg
        self.speed=speed #these are all instance variables 
        
    cost=200    
        
    def accelerate(self):
        return f'the car, manu in {self.year}, can acc to {self.speed}'
  
    def brake(self):
        return self.speed-20
    
car1=car(2010,33,333)    
car1.accelerate()    
car1.brake()
car1.cost


# Methods-three types -static(independent),class and instance methods 
class Cab:
    
    numberofcabs  = 0
    numpassengers = 0

    def __init__(self,driver,kms,places,pay,passengers):
        self.driver = driver
        self.running = kms
        self.places = places
        self.bill = pay
        Cab.numberofcabs  =  Cab.numberofcabs + 1
        Cab.numpassengers =  Cab.numpassengers + passengers
        
    def rateperkm(self):
        """
        returns price of cab fare per km which is calculated by dividing total bill by no. of kms cab traveled.
        """
        return self.bill/Cab.numberofcabs

    @classmethod    
    def noofcabs(cls):
        return cls.numberofcabs
    
    @classmethod
    def avgnoofpassengers(cls):
        return cls.numpassengers/cls.numberofcabs
    
    @staticmethod
    def billvalidation(pay):
        return int(pay) > 0

    
cab1=Cab('ram',11,['sata','re'],400,2)

cab1.noofcabs()
cab1.numpassengers
cab1.avgnoofpassengers()




#inheritance
class Vehicle:
    minimumrate = 50
    def __init__(self,driver,wheels,seats,kms,bill):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats
        self.running = kms
        self.bill = bill
    
    def rateperkm(self):
        return self.bill/self.running

class Cab(Vehicle):
    def __init__(self,driver,wheels,seats,kms,bill,namedriver):
        super().__init__(driver,wheels,seats,kms,bill)
        self.namedriver=namedriver        
        
cab2=Cab('avi',2,1,11,2,'aa')        

#GETTER AND SETTER 
#GETTER-TO MAKE AN ATTRIBUTE 
#SETTER TO MAEK IT DYNAMIC 

class donation:
    def __init__(self,amount):
        self.amount = amount
        
    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        if amount < 10:
            self.__amount = 10
        elif amount > 1000000:
            self.__amount = 1000000
        else:
            self.__amount = amount


charity = donation(5)
charity.amount
10