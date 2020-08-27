
class Character:
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
  


class Hero(Character):
    
    
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        
    
    def attack(self, enemy):
        enemy.health -= self.power
        print(f"You do {self.power} damage to the goblin." )
    
  
            
    
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



