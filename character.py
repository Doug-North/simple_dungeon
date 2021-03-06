from combat import Combat
import random

class Character(Combat):
    xp = 0
    base_hit_points = 30
    atk_lim = 10

    def attack(self):
        roll = random.randint(1, self.atk_lim)
        if self.weapon == 'sword':
            roll += 1
        elif self.weapon == 'axe':
            roll += 2
        return roll > 5


    def get_weapon(self):
        weapon_choice = input("Weapon: ([S]word, [A]xe, [B]ow): ").lower()

        if weapon_choice in 'sab':
            if weapon_choice == 's':
                return 'Sword'
            elif weapon_choice == 'a':
                return 'Axe'
            else:
                return 'Bow'
        else:
            return self.get_weapon()

    def __init__(self, **kwargs):
        self.name = input("Name: ")
        self.weapon = self.get_weapon()
        self.hit_points = self.base_hit_points

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return "{}, HP: {}, XP: {}".format(self.name, self.hit_points, self.xp)

    def rest(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points += 1
            return self.hit_points

    def level_up(self):
        return self.xp >= 5

