
from datetime import datetime

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_age(cls, name, year):
        age = datetime.today().year - year
        p1 = Person(name, age)
        return p1
    
    def check_age(self):
        return self.age > 19
    

#Driver's code
person1 = Person('Mark', 10)
person2 = Person.get_age('Rohan', 1992)

print(person1.name, person1.age) 
print(person2.name, person2.age)
print(person1.check_age())
print(person2.check_age())        
print(type(person1))


