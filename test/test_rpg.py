from main.character import Character


class TestCharacter:

    def test_new_character(self):
        character = Character()

        assert character.health == 1000
        assert character.level == 1
        assert character.alive is True

    # Damage is subtracted from Health
    def test_take_damage(self):
        character1 = Character()
        character2 = Character()

        character1.attacks(character2, 20)

        assert character2.health == 980

    # When damage received exceeds current Health, Health becomes 0 and the character dies
    def test_character_dies(self):
        character1 = Character()
        character2 = Character()

        character1.attacks(character2, 1010)

        assert character2.health == 0
        assert character2.alive is False

    def test_character_can_heal_another_character(self):
        character1 = Character()
        character2 = Character()

        character1.attacks(character2, 20)
        character1.heals(character2, 20)

        assert character2.health == 1000
