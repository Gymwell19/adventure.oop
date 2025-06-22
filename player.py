from character import Character

class Player(Character):
    def __init__(self, name, health=115):
        super().__init__(name, health)
        self.bleed = 1  # Example of a player-specific attribute

    def attack(self, enemy, attack_type="sword"):
        # Placeholder for attack logic, which you will expand later
        # You can use attack_type to differentiate between sword, heavy, or throw attacks
        pass

    def evade(self):
        # Placeholder for evade logic
        pass

    def heal(self, amount):
        super().heal(amount)
        # You can add player-specific healing logic here if needed
    
    def is_alive(self):
        return super().is_alive()