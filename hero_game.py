"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
from lib.hero import Hero
from lib.goblin import Goblin

block = Hero('Blockade', 10, 5)
goo = Goblin('Goo E.', 6, 2)


def main():
    block.health
    block.power
    goo.health 
    goo.power 

    while goo.health > 0 and block.health > 0:
        print("You have %d health and %d power." % (block.health, block.power))
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
            goo.health -= block.power
            print("You do %d damage to the goblin." % block.power)
            if goo.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goo.health > 0:
            # Goblin attacks hero
            block.health -= goo.power
            print("The goblin does %d damage to you." % goo.power)
            if block.health() <= 0:
                print("You are dead.")

main()
