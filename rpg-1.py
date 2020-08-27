"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

from classes_rpg_1 import Hero, Goblin, Zombie, Character
from classes_rpg import Character


def main():
    goblin = Goblin( "goblin", 100, 5)
    hero = Hero("hero", 100, 10)
    zombie = Zombie("zombie", float('inf'), 2)
    
    while hero.is_alive() :
        goblin.print_status()
        hero.print_status()
        
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("4. summon friend")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            if goblin.health <= 0:
                print("The goblin is dead.")
                goblin = zombie
                zombie.attack(hero)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        
        elif user_input == "4":
            summon_pick = int(input("Which friends do you want to summon?"))
            print("1. Medic\n2. Shadow\n3. magic")
            if summon_pick == "1": 
                #--------continue coding(start with making class for char)--------- 
        else:
            print("Invalid input %r" % user_input)
        
        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
            if hero.health <= 0:
                print("You are dead.")

main()
