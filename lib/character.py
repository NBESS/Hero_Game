class Character():
    def __init__(self, name):
        self.name = name
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False 
    
    