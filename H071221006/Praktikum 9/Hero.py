class Human:
    def __init__(self, name, position):
        self.name = name
        self.__position = position
        self._speed = 1
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setPosition(self, position):
        self.position = position
    def getPosition(self):
        return self.position
    def setMovement(self, movement):
        if movement == 'R':
            self.__position -= self._speed
        elif movement == 'L':
            self.__position += self._speed
    def getMovement(self):
        return self.__position

class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    def setPower(self, power):
        self._power = power
    def getPower(self):
        return self._power
    def setHealth(self, health):
        self._health = health
    def getHealth(self):
        return self._health
    def setArmor(self, armor):
        self._armor = armor
    def getArmor(self):
        return self._armor
    def setSpeed(self, speed):
        self._speed = speed
    def getSpeed(self):
        return self._speed
    def attack(self, target):
        target._health -= self._power

class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 26
        self._armor = 30
    def setPower(self, power):
        self._power = power
    def getPower(self):
        return self._power
    def setArmor(self, armor):
        self._armor = armor
    def getArmor(self):
        return self._armor
    def getHealth(self):
        return self._health
    def special(self, target):
        self._power = 32
        self._armor = 45
        self.attack(target)
        target._health -= self._power
    
class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 35
        self.speed = 4
    def setPower(self, power):
        self._power = power
    def getPower(self):
        return self._power
    def setSpeed(self, speed):
        self.speed = speed
    def getSpeed(self):
        return self.speed
    def special(self, target):
        self._speed = 7
        self._power = 42
        self.attack(target)
        target._health -= self._power

class Support(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._health = 500
        self._armor = 8
        self._speed = 4
    def setHealth(self, health):
        self._health = health
    def getHealth(self):
        return self._health
    def setArmor(self, armor):
        self._armor = armor
    def getArmor(self):
        return self._armor
    def setSpeed(self, speed):
        self._speed = speed
    def getSpeed(self):
        return self._speed
    def special(self, target):
        self._speed = 6
        self._power = 42
        # self.attack(target)
        target._health += 150


