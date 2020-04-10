from lib.character import Character

class Zombie(Character):
    
    def undead_rebirth(self, amount_received):
        if self.health < 0:
            print("%s Invokes Undead Rebirth!!!" % self.name)
            self.health += amount_received