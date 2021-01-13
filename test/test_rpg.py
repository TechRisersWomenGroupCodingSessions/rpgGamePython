from main.character import Character


class TestCharacter:

    def test_new_character(self):
        character = Character()

        assert character.health == 1000
        assert character.level == 1
        assert character.alive == True

#Damage is subtracted from Health
    def test_take_damage(self):
        character1 = Character()
        character2 = Character()

        character1.giveDamage(character2)

        assert character2.health == 980