class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.level = 1
        self.hp = 100
        self.damage = 25

    def level_up(self):
        self.level += 1
        self.hp += 75
        self.damage += 10

    def attack(self):
        pass
        
    def ultimate_attack(self):
        pass

    def run_away(self):
        pass