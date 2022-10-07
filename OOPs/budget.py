# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:05:20 2022

@author: sanaayak
"""
#Complete the Category class in budget.py.
#It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment.
#When objects are created, they are passed in the name of the category.
#The class should have an instance variable called ledger that is a list. 

class Category:
    def __init__(self,name,ledger):
        self.name=name
        self.ledger=list()
        
        
        
    def deposit_amount(self,amount,description=""): 
        '''pls fill fescription'''
        self.ledger.append({'amount':amount,'description':description})
        
        
    def withdraw(self,amount,description=""):
        if(self.check_funds(amount)):
            self.ledger.append({'amount':-amount,'description':description})
            return True
        return False 
    
    def get_balance(self):
        total_cash=0   
        for item in self.ledger:
            total_cash+=item['amount']
        return total_cash 
    
    def transfer(self,amount,category)
            