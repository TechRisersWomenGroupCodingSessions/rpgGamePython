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

    # def test_character_can_heal_another_character(self):
    #     character1 = Character()
    #     character2 = Character()
    #
    #     character1.attacks(character2, 20)
    #     character1.heals2(character2, 20)
    #
    #     assert character2.health == 1000
    # we can delete this later if not needed

    def test_dead_character_cannot_be_healed(self):
        character1 = Character()
        character2 = Character()
        character1.health = 0
        character1.alive = False
        character2.heals(character1, 1)

        assert character1.health == 0
        assert character1.alive is False

    def test_healing_cannot_raise_health_above_1000(self):
        character1 = Character()
        character2 = Character()

        character1.health = 900
        character1.heals(character1, 300)
        assert character1.health == 1000

    def test_character_cannot_self_harm(self):
        character1 = Character()

        character1.health = 980
        character1.attacks(character1,20)
        assert character1.health == 980

    def test_character_can_only_self_heal(self):
        character1 = Character()
        character2 = Character()

        character1.health = 980
        character2.health = 600
        character2.heals(character1, 20)
        character2.heals(character2, 20)
        assert character1.health == 980
        assert character2.health == 620

    def test_character_attacked_by_Level5_or_more(self):
        character1 = Character()
        character2 = Character()
        character1.level = 6
        character2.level = 1

        character1.health = 100
        character2.health = 100
        character2.attacks(character1,20)
        character1.attacks(character2, 20)
        assert character1.health == 90
        assert character2.health == 70

    def test_character_attack_max_range_melee_out_of_range(self):
        character1 = Character()
        character2 = Character()
        character1.range = 2
        character1.position = (4, 3)
        character2.position = (3, -2)
        character1.attacks(character2, 20)
        assert character1.health == 1000
        assert character2.health == 1000

    def test_character_attack_max_range_melee_in_range(self):
        character1 = Character()
        character2 = Character()
        character1.range = 2
        character1.position = (0, 0)
        character2.position = (1,1)
        character1.attacks(character2, 20)
        assert character1.health == 1000
        assert character2.health == 980

    def test_character_change_type(self):
        character1 = Character()
        character2 = Character()
        character1.type('melee')
        character2.type('RAngeD')
        assert character1.range == 2
        assert character2.range == 20

    def test_character_in_range_hurt(self):
        character1 = Character()
        character2 = Character()
        character1.type('Melee')
        character2.type('ranged')
        character1.position = (0, 0)
        character2.position = (3, 3)
        character1.attacks(character2, 50)
        character2.attacks(character1, 40)

        assert character1.health == 960
        assert character2.health == 1000

    def test_new_character_no_faction(self):
        character1 = Character()

        assert character1.factions == None

    def test_new_character_joins_a_faction(self):
        character1 = Character()

        character1.join_faction('Titans')

        assert character1.factions == 'Titans'

    def test_new_character_chooses_a_faction_from_multiple_options(self):
        character1 = Character()

        character1.join_faction(['Titans','Spartans'])

        assert 'Titans' in character1.factions
        assert 'Spartans' in character1.factions

    def test_character_leaves_faction(self):
        character1 = Character()
        character1.join_faction(['Titans'])
        character1.leave_faction(['Titans'])

        assert 'Titans' not in character1.factions

    def test_characters_are_allies(self):
        character1 = Character()
        character2 = Character()

        character1.join_faction(['Titans'])
        character2.join_faction(['Titans'])

        assert character1.allies(character2) is True
