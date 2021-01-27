class Character:
    health = 1000
    level = 1
    alive = True

    def attacks(self, opponent, damageAmount):
        opponent.health = opponent.health - damageAmount
        if opponent.health <= 0:
            opponent.health = 0
            opponent.alive = False

    def heals(self, comrade, healingAmount):
        if comrade.alive:

            comrade.health = comrade.health + healingAmount
            if comrade.health >1000:
                comrade.health = 1000


