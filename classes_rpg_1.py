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
            print("--------------------------")
            print("Double damage!!!!!!!!!!!!")
            print("--------------------------")
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
        print(f"goblin do {self.power} damage to the enemy.\n" )
    
    
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
        print(f"""{self.name}'s health: {self.health}, \n{self.name}'s power: {self.power}\n""")


class Medic(Character):
    
    
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana
        
    
    def recuperate(self, team):
        if random.random() <= 0.2:
            team.health = team.health + 2
            self.mana -= 5 
            print("--------------------------")
            print(f"medic heal(+2) the hero." )
            print("--------------------------")
        else:
            pass
        
        def print_status(self):
            print(f"""{self.name}'s health: {self.health}, \n{self.name}'s power: {self.power}\n""")

class Shadow(Character):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        

    def attack(self, enemy):
        enemy.health -= self.power
        print(f"shadow do {self.power} damage to the enemy." )
    
    def print_status(self):
            print(f"""{self.name}'s health: {self.health}, \n{self.name}'s power: {self.power}\n""")

    def defense(self, enemy):
        if random.random() <= 0.1 and attack(self, enemy):
            self.health = self.health

class Sorceress(Character):
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana

    def attack(self, enemy):
        enemy.health = 100
        print("-------------------------------------------------")
        print(f"sorceress broke infinite health (Health: 100) " )
        print("-------------------------------------------------")
    
    def print_status(self):
            print(f"""{self.name}'s health: {self.health}, \n{self.name}'s power: {self.power}\n""")

class Healer(Character):
    def __init__(self, name, health, mana):
        self.name = name
        self.health = health
        self.mana = mana

    def heal(self, hero):
        hero.health = 100
        print("--------------------------------------")
        print(f"Healer healed Hero!!! (health: 100)" )
        print("--------------------------------------")
    def print_status(self):
            print(f"""{self.name}'s health: {self.health}, \n{self.name}'s power: {self.power}\n""")

    
