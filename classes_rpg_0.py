import random
class Character:
    def is_alive(self):
        if self.health > 0 or self.health == float('inf'):
            return True
        else:
            return False
  


class Hero(Character):
    
    
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        
    
    def attack(self, enemy):
        if random.random() <= 0.2:
            enemy.health -= (self.power * 2)
            print(f"You do {self.power * 2} damage to the enemy." )
        else:
            enemy.health -= self.power
            print(f"You do {self.power} damage to the enemy." )
    
  
            
    
    def print_status(self):
        print(f"""{self.name}'s health: {self.health}, \n{self.name}'s power: {self.power}\n""")


class Goblin(Character):
    
    
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        
        
    
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"goblin do {self.power} damage to the hero." )
    
    
    def print_status(self):
        print(f"""\n{self.name}'s health: {self.health},\n{self.name}'s power: {self.power}""")

    


class Zombie(Character):
    
    
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        
    
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"zombie do {self.power} damage to the hero" )
    
  
            
    
    def print_status(self):
        print(f"""{self.name}'s health: {self.health}, \n{self.name}'s power: {self.power}""")
