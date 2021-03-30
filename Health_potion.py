import random

health = 50
difficultly = 1
potion_health = int(random.randint(25,50) / difficultly)

health = str(health + potion_health)
print('Your health is ' + (health) + ' HP')



