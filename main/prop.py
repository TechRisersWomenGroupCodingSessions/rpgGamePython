class Prop:
    health = 1000
    destroyed = False
    position = (0, 0)


    def is_prop_destroyed(self):
        if self.health <= 0:
            self.health = 0
            return True




