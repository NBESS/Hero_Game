class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False 

    def attack(self, enemy):
        # Goblin attacks hero
        enemy.health -= self.power
        print("%s does %d damage to %s." % (self.name, self.power, enemy.name))
        if enemy.health <= 0:
            print("%s is dead." % enemy.name)
    
    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))