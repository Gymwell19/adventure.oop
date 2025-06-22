from character import Character

class Werewolf(Character):
    def __init__(self, name="Werewolf", health=150):
        super().__init__(name, health)

    def attack(self, enemy):
        # Placeholder for werewolf attack logic
        pass

    def is_alive(self):
        return super().is_alive()