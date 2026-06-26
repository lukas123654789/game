
class Player():
    def __init__(self, player_name):
        self.name = player_name
        self.level = 1
        self.hp = 100
        self.damage = 25

    def level_up(self):
        self.level += 1
        self.hp += 75
        self.damage += 10

    def attack(self, health):
        return health - self.damage
             
    def ultimate_attack(self, health):
        return health - self.damage * 2

    def run_away(self):
        return True