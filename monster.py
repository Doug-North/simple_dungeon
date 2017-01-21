import random
from combat import Combat

COLORS = ['red', 'black', 'blue', 'green', 'white']


class Monster(Combat):
    min_hit = 1
    max_hit = 5
    min_xp = 1
    max_xp = 5
    weapon = 'sword'
    sound = 'roar!'

    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit, self.max_hit)
        self.xp = random.randint(self.min_xp, self.max_xp)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{} {} HP: {} XP: {}'.format(self.color,
                                            self.__class__.__name__,
                                            self.hit_points,
                                            self.xp)

    def battlecry(self):
        return self.sound.upper()


class Goblin(Monster):
    min_hit = 6
    max_hit = 10
    min_xp = 6
    max_xp = 10
    weapon = 'serrated katana'
    sound = 'wraawk!'


class Troll(Monster):
    min_hit = 11
    max_hit = 15
    min_xp = 11
    max_xp = 15
    weapon = 'bloody club'
    sound = 'graaaaaa!'


class Dragon(Monster):
    min_hit = 16
    max_hit = 20
    min_xp = 16
    max_xp = 20
    weapon = 'fire'
    sound = 'krawwkraa'





