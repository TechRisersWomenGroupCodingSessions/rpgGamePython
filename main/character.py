class Character:
    health = 1000
    level = 1
    alive = True

    def giveDamage(self, character, damageAmount):
        character.health = character.health - damageAmount
        if character.health <= 0:
            character.health = 0
            character.alive = False
