class Character:
    health = 1000
    level = 1
    alive = True

    def giveDamage(self, character):
        character.health = character.health - 20
