"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
from lib.hero import Hero
from lib.goblin import Goblin


def main():
    hunter = Hero('Hunter')
    goo = Goblin('Goo E.')
    hunter.health
    hunter.power
    goo.health 
    goo.power 

    while goo.is_alive() and hunter.is_alive():
        print("You have %d health and %d power." % (hunter.health, hunter.power))
        print("The goblin has %d health and %d power." % (goo.health, goo.power))
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
