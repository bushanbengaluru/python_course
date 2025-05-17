#Polymorphism:
#Some code, different behaviuor different situation
class Cat:
    def sounds(self):
        print('Meow Meow')
class Dog:
    def sounds(self):
        print('Bow Bow')
class Rat:
    def sounds(self):
        print('Keech Keech')
c=Cat()
d=Dog()
r=Rat()
list_obj=[c,d,r]

import random
random.shuffle(list_obj)
for obj in list_obj:
    obj.sounds()