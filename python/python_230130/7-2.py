class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def __del__(self):
        Doggy.num_of_dogs -=1

    def bark(self):
        print('bark! bark!')
    
    @classmethod
    def get_status(cls):
        print(f'birth_of_dogs: {Doggy.birth_of_dogs}')
        print(f'num_of_dogs: {Doggy.num_of_dogs}')

    

A = Doggy('ssafy', 'chiwawa')    

B = Doggy('BB', 'bbbb')
B.get_status()
Doggy.get_status()
del B
Doggy.get_status()