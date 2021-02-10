
class Character:
    health = 1000
    level = 1
    alive = True
    range = 0
    position = (0, 0)

    def type(self, fighter):
        fighter = fighter.lower()
        if fighter =='melee':
            self.range = 2
        elif fighter == 'ranged':
            self.range = 20

    def attacks(self, opponent, damageAmount):

        if self.isOpponentInRange(opponent):
            if opponent.level - self.level >= 5:
                damageAmount = damageAmount * 0.5
            elif self.level - opponent.level >= 5:
                damageAmount = damageAmount * 1.5
            if self != opponent:
                opponent.health = opponent.health - damageAmount
                if opponent.health <= 0:
                    opponent.health = 0
                    opponent.alive = False

    def isOpponentInRange(self, opponent):
        position1 = self.position
        position2 = opponent.position

        a = position1[0]
        b = position1[1]

        c = position2[0]
        d = position2[1]

        x = ( c -a )**2
        y = ( d -b )**2

        distance = ( x +y )**0.5

        return distance <= self.range


    def heals3(self, comrade, healingAmount):
        if comrade.alive:

            comrade.health = comrade.health + healingAmount
            if comrade.health > 1000:
                comrade.health = 1000

    def heals2(self, comrade, healingAmount):
        if comrade.alive and self == comrade:

            comrade.health = comrade.health + healingAmount
            if comrade.health > 1000:
                comrade.health = 1000
