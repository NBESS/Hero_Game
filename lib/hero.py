class Hero():
    def __init__(self, name, health=10, power=5):

        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        # Hero attacks goblin
        enemy.health -= self.power
        print("You do %d damage to the goblin." % self.power)
        if enemy.health <= 0:
            print("The goblin is dead.")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        