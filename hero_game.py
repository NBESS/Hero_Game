"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
from lib.character import Character
from lib.hero import Hero
from lib.goblin import Goblin
from lib.zombie import Zombie


def main():
    hunter = Hero('Hunter', health=10, power=5)
    goo = Goblin('Goo E.', health=6, power=2)
    zim = Zombie('Zimm', health=1, power=3)
    hunter.health
    hunter.power
    goo.health 
    goo.power 
    zim.health
    zim.power

    while goo.is_alive() and hunter.is_alive():
        hunter.print_status()
        goo.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hunter.attack(goo)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goo.health > 0:
            # Goblin attacks hero
            goo.attack(hunter)

main()
