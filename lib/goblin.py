class Goblin():
    def __init__(self, name, health=6, power=2):
        
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        # Goblin attacks hero
        enemy.health -= self.power
        print("The goblin does %d damage to you." % self.power)
        if enemy.health <= 0:
            print("You are dead.")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False 
    
    def print_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))


        