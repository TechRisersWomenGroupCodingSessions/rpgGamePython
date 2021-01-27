class Character:
    health = 1000
    level = 1
    alive = True

    def attacks(self, opponent, damageAmount):
        if opponent.level - self.level >= 5:
           damageAmount = damageAmount * 0.5
        elif self.level - opponent.level >= 5:
            damageAmount = damageAmount * 1.5
        if self != opponent:
            opponent.health = opponent.health - damageAmount
            if opponent.health <= 0:
                opponent.health = 0
                opponent.alive = False


    def heals(self, comrade, healingAmount):
        if comrade.alive:

            comrade.health = comrade.health + healingAmount
            if comrade.health >1000:
                comrade.health = 1000

    def heals2(self, comrade, healingAmount):
        if comrade.alive and self == comrade:

            comrade.health = comrade.health + healingAmount
            if comrade.health >1000:
                comrade.health = 1000
