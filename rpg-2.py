"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee
"""

class Warrior:
    def __init__(self, health, power, coins):
        self.name = '<undefined>'
        self.health = health
        self.power = power
        self.coins = coins

    def attack(self, enemy):
        enemy.health -= self.power
        print("%s did %d damage to %s." % (self.name, self.power, enemy.name))

    def alive(self): 
        return self.health > 0

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

class Hero(Warrior):
    def __init__(self):
        self.name = 'Hiro'
        self.health = 10
        self.power = 5

class Goblin(Warrior):
    def __init__(self):
        self.name = 'Goblin'
        self.health = 10
        self.power = 5

hero = Hero()
goblin = Goblin()

def main():
    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            if goblin.alive() == False:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)
            print("The goblin does %d damage to you." % goblin.power)
            if hero.health <= 0:
                print("You are dead.")

main()
