from main.main import inc


class TestCharacter:

    def test_answer(self):
        assert inc(3) == 5
