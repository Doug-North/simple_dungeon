import random


class Combat:
    dodge_lim = 6
    attack_lim = 6

    def dodge(self):
        roll = random.randint(1, self.dodge_lim)
        return roll < 4

    def attack(self):
        roll = random.randint(1, self.attack_lim)
        return roll < 4


