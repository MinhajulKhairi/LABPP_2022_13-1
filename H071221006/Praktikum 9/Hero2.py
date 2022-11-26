from Hero import Warrior, Assassin, Support

warrior = Warrior("bambang", position = 10)
assassin = Assassin("joko", position = 25)
support = Support("udin", position = 30)

#sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
#sesudah
print("health (after)", warrior.getHealth())
print("="*20)

#sebelum
print("warrior (health)", warrior.getHealth())
print("support (speed) : ", support.getSpeed())
support.special(warrior)
#sesudah
print("warrior (health)", warrior.getHealth())
print("support (speed) : ", support.getSpeed())
