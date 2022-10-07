#create a pokemon

class Pokemon:
    def __init__(self,name,primary_type,max_hp):
        self.name=name
        self.primary_type=primary_type
        self.max_hp=max_hp #both max hp and hp are the same
        self.hp=max_hp

    def __str__(self):
        return f'{self.name} is the name and {self.primary_type} is the type'

    def feed(self):
        if self.hp<self.max_hp:
            self.hp+=1
            print(f'{self.name} is filled and now has {self.hp}')
        else:
            print(f'{self.name} is fulll')

    #make battle and aand decide winner
    def battle(self,other):
        print(f' {self.name} is fighting with {other.name}')
        #call battle

    @staticmethod
    def typewheel(type1,type2):
        results= {0:'loss', 1:'win',-1:'tie'}
        #mapping between results and conditions
        game_map={'water':0,'fire':1,'grass':2}

         #implement win lose matrix
        wl_matrix=[
            [-1,-1,0], #water
            [0,-1,1], #fire
            [1,0,-1] #grass
            ]
        #declare winner
        game_map['water']
        wl_matrix[game_map['water']]




a=Pokemon('bulbi', 'fire',33)
b=Pokemon('charmand', 'fire',33)





#look at it
#feed them to imporve helath
#make a battle and decide winner
