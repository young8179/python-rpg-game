"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
import random
from classes_rpg_1 import Hero, Goblin, Zombie, Character, Medic, Shadow, Sorceress, Healer



def main():
    goblin = Goblin( "goblin", 100, 5)
    hero = Hero("hero", 100, 10)
    zombie = Zombie("zombie", float('inf'), 2)
    medic = Medic("medic", 100, 100)
    shadow = Shadow("shadow",100, 20)
    sorceress = Sorceress("sorceress", 100, 100)
    healer = Healer("healer", 100, 100)
    enemy = [goblin, zombie]
    while hero.is_alive() :
        goblin.print_status()
        hero.print_status()
        
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. change charater")
        print("4. summon friend")
        print("5. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            
            if goblin.health <= 0:
                print("The goblin is dead.")
                print("---------------------")
                print("face another enemy!")
                print("---------------------")
                goblin = zombie
                if zombie.health == 0:
                    print("zombie is dead")
                    print("You won")
                    break                
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("1) shadow\n2) ")
            another_char = int(input("Which character: "))
            if another_char == 1:
                while True:
                     shadow.attack(goblin)
                     goblin.attack(shadow)
                     shadow.print_status()
                     goblin.print_status()
                     change_back_char = input("Change character back to hero? yes or no: ")
                     if goblin.health <=0:
                         print("goblin is dead")
                         print("zombie is comming")
                         goblin = zombie 
                     if change_back_char.lower() == "yes":
                        break
                     elif change_back_char.lower == "no":
                        pass
            else:
                print("invalid input")
        elif user_input == "4":
            print("1)sorceress \n2)healer")
            summon_pick = int(input("Which friends do you want to summon?"))
            if summon_pick == 1:
                sorceress.attack(zombie)
                
            elif summon_pick == 2:
                healer.heal(hero)
            
            else:
                print("Invalid value")
                
            
            #--------continue coding(start with making class for char)--------- 
        elif user_input == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid input %r" % user_input)
        
        if goblin.health > 0:
            if hero == shadow:
                goblin.attack(shadow)
                medic.recuperate(shadow)
                if shadow.health <= 0:
                    print("You are dead.")
                    print("You lose")
            # Goblin attacks hero
            else:
                goblin.attack(hero)
                medic.recuperate(hero)
                if hero.health <= 0:
                    print("You are dead.")
                    print("You lose")
main()
