
class Character:
    health = 1000
    level = 1
    alive = True
    range = 0
    position = (0, 0)
    factions = []
    allies = False

    def leave_faction(self, factions):

        for faction in factions:
            self.factions.remove(faction)
    def join_faction(self, faction):
        self.factions += faction

    def is_ally(self, character):
        if self.factions == None or character.factions == None:
            return False
        else:
            return any(item in self.factions for item in character.factions)

    def type(self, fighter):
        fighter = fighter.lower()
        if fighter =='melee':
            self.range = 2
        elif fighter == 'ranged':
            self.range = 20

    def attacks(self, opponent, damageAmount):

        if self.isOpponentInRange(opponent) and not self.is_ally(opponent):
            if opponent.level - self.level >= 5:
                damageAmount = damageAmount * 0.5
            elif self.level - opponent.level >= 5:
                damageAmount = damageAmount * 1.5
            if self != opponent:
                opponent.health = opponent.health - damageAmount
                if opponent.health <= 0:
                    opponent.health = 0
                    opponent.alive = False

    def damageprop(self, prop,damageAmount):

        prop.health = prop.health - damageAmount

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


    # def heals3(self, comrade, healingAmount):
    #     if comrade.alive:
    #
    #         comrade.health = comrade.health + healingAmount
    #         if comrade.health > 1000:
    #             comrade.health = 1000
    # we may delete this later

    def heals(self, comrade, healingAmount):
        if isinstance(comrade,Character):
            if comrade.alive and (self == comrade or self.is_ally(comrade)):

                comrade.health = comrade.health + healingAmount
                if comrade.health > 1000:
                    comrade.health = 1000
