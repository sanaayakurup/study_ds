#code with harry video on getters and setter


class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=f'{self.fname}{self.lname}@gmail.com'
        
    def explain(self):
        return f'this emp is {self.fname} {self.lname}'
    
   
hindustani_supporter=employee('hindustani','supporter')
hindustani_supporter.explain()
hindustani_supporter.email

#nowhindustani supporter changes his nam to us supporter 
hindustani_supporter.fname='US'
hindustani_supporter.email #this is not changing to US supported 
#the above is not dynamic

#now i will make aan email function which will make it dynamic 
#so that the fname even if set from outside will change email 
class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

        #self.email=f'{self.fname}{self.lname}@gmail.com'
        
    def explain(self):
        return f'this emp is {self.fname} {self.lname}'
    
    def email(self):
        return f'{self.lname}@gmail.com'
    
    
hindustani_supporter=employee('supp','hindustan')    
hindustani_supporter.lname='UK'
hindustani_supporter.email() #now this is dynamic 

#however we are calling an attribute as a function
#how can we change this 
#we can use something called a SETTER 
class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f'{self.fname}{self.lname}@gmail.com'
        
    def explain(self):
        return f'this emp is {self.fname} {self.lname}'
    
    @property #this is a getter 
    def email(self):
        return f'{self.lname}@gmail.com'
    
hindustani_supporter=employee('supp','hindustan')    
hindustani_supporter.lname='UK'
hindustani_supporter.email #now WE CAN DIRECTOLY ACCESS THIS WITHOUT CALLING THE METHOD 
hindustani_supporter.email
#WE USED THE PROPERTY DECORATOR TO EXTEND THE FUNCTIONALITY OF A FUNCTION AND CHANGE IT TO AN ATTRIBUTE


#What if i want to setthe email externally, and dynamically change the fname and lname acc to the set email?
hindustani_supporter.email='uk.sup@gmail.com' #cant set attribute as there is no setter
#this is called a setter- as we want to set all the other vars from out  
class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f'{self.fname}{self.lname}@gmail.com'
        
    def explain(self):
        return f'this emp is {self.fname} {self.lname}'
    
    @property
    def email(self):
        return f'{self.lname}@gmail.com'

    @email.setter
    def email(self,string):
        names=string.split('@')[0]
        self.fname,self.lname=names.split(".")
        return
hindustani_supporter=employee('supp','hindustan')    
hindustani_supporter.lname='UK'
hindustani_supporter.email #now WE CAN DIRECTOLY ACCESS THIS WITHOUT CALLING THE METHOD 
hindustani_supporter.email='uk.sup@gmail.com' 
hindustani_supporter.fname
hindustani_supporter.lname #dynamically changed 

#now we want to delete the email
del hindustani_supporter.email
#but it cant as theres no deleter 

#this is called a setter- as we want to set all the other vars from out  
class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f'{self.fname}{self.lname}@gmail.com'
        
    def explain(self):
        return f'this emp is {self.fname} {self.lname}'
    
    @property
    def email(self):
        return f'{self.lname}@gmail.com'

    @email.setter
    def email(self,string):
        names=string.split('@')[0]
        self.fname,self.lname=names.split(".")
        return
    
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
        
hindustani_supporter=employee('supp','hindustan')    
hindustani_supporter.lname='UK'
hindustani_supporter.email #now WE CAN DIRECTOLY ACCESS THIS WITHOUT CALLING THE METHOD 
hindustani_supporter.email='uk.sup@gmail.com' 
hindustani_supporter.fname
hindustani_supporter.lname #dynamically changed 

#now we want to delete the email
del hindustani_supporter.email

#lname and fname are gone however email is coming as none
#We change the code a little bit 

class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        #self.email=f'{self.fname}{self.lname}@gmail.com'
        
    def explain(self):
        return f'this emp is {self.fname} {self.lname}'
    
    @property
    def email(self):
        if self.lname==None or self.fname==None:
            return 'email not set'
        else:
            return f'{self.lname}@gmail.com'

    @email.setter
    def email(self,string):
        names=string.split('@')[0]
        self.fname,self.lname=names.split(".")
        return
    
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
        
hindustani_supporter=employee('supp','hindustan')    
hindustani_supporter.lname='UK'
hindustani_supporter.email #now WE CAN DIRECTOLY ACCESS THIS WITHOUT CALLING THE METHOD 
hindustani_supporter.email='uk.sup@gmail.com' 
hindustani_supporter.fname
hindustani_supporter.lname #dynamically changed 
del hindustani_supporter.email
hindustani_supporter.email

