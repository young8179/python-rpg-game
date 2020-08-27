"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

from classes_rpg import Hero, Goblin
from classes_rpg import Character


def main():
    goblin = Goblin( "goblin", 100, 5)
    hero = Hero("hero", 100, 7)
    
    while goblin.is_alive() and hero.is_alive():
        goblin.print_status()
        hero.print_status()
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
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
            if hero.health <= 0:
                print("You are dead.")

main()
