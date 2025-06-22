from player import Player
from werewolf import Werewolf
import random
from constants import (
    SWORD_CRIT, SWORD_ABOVE_AVG, SWORD_AVG, SWORD_BELOW_AVG, SWORD_MISS,
    WEREWOLF_CRIT, WEREWOLF_ABOVE_AVG, WEREWOLF_AVG, WEREWOLF_BELOW_AVG, WEREWOLF_MISS,
    WEREWOLF_DEATH, EVADE_SUCC, EVADE_MISS,
    HEAVY_SWORD_CRIT, HEAVY_SWORD_ABOVE_AVG, HEAVY_SWORD_AVG, HEAVY_SWORD_BELOW_AVG,
    THROW_SWORD_CRIT, THROW_SWORD_ABOVE_AVG, THROW_SWORD_AVG, THROW_SWORD_BELOW_AVG, THROW_SWORD_MISS,
    WEREWOLF_SLAY_LOOT, WEREWOLF_SLAY_SPECIAL_LOOT, WEREWOLF_MERCY_LOOT, WEREWOLF_MERCY_SPECIAL_LOOT,
    ACHIEVEMENTS
)

class Game:
    def __init__(self):
        self.player = Player("Hero")
        self.werewolf = Werewolf()
        self.running = True

    def start(self):
        print("Welcome to Natural Savagery!")
        self.game_loop()

    def game_loop(self):
        while self.player.is_alive() and self.werewolf.is_alive():
            self.display_status()
            action = input("Choose your action: [ATTACK] [EVADE]\n>").strip().lower()
            if action == "attack":
                self.player_attack()
            elif action == "evade":
                self.player_evade()
            else:
                print("Invalid action.")
            if self.werewolf.is_alive():
                self.werewolf_attack()
        self.end_game()

    def display_status(self):
        print(f"\nPlayer Health: {self.player.health}")
        print(f"Werewolf Health: {self.werewolf.health}")

    def player_attack(self):
        damage = random.randint(1, 20)
        if damage == 20:
            print(random.choice(SWORD_CRIT))
            damage = int(damage * 1.5)
        elif 16 <= damage <= 19:
            print(random.choice(SWORD_ABOVE_AVG))
        elif 6 <= damage <= 15:
            print(random.choice(SWORD_AVG))
        elif 1 <= damage <= 5:
            print(random.choice(SWORD_BELOW_AVG))
        else:
            print(random.choice(SWORD_MISS))
            damage = 0
        self.werewolf.take_damage(damage)
        print(f"You dealt {damage} damage to the werewolf.")

    def player_evade(self):
        if random.random() < 0.5:
            print(random.choice(EVADE_SUCC))
        else:
            print(random.choice(EVADE_MISS))

    def werewolf_attack(self):
        damage = random.randint(10, 25)
        if damage == 25:
            print(random.choice(WEREWOLF_CRIT))
            damage = int(damage * 1.5)
        elif 21 <= damage <= 24:
            print(random.choice(WEREWOLF_ABOVE_AVG))
        elif 16 <= damage <= 20:
            print(random.choice(WEREWOLF_AVG))
        elif 11 <= damage <= 15:
            print(random.choice(WEREWOLF_BELOW_AVG))
        else:
            print(random.choice(WEREWOLF_MISS))
            damage = 0
        self.player.take_damage(damage)
        print(f"The werewolf dealt {damage} damage to you.")

    def end_game(self):
        if self.player.is_alive():
            print(random.choice(WEREWOLF_DEATH))
            print("You have defeated the werewolf!")
            print("Loot:", random.choice(WEREWOLF_SLAY_LOOT))
            print("Special Loot:", random.choice(WEREWOLF_SLAY_SPECIAL_LOOT))
            print("Achievement Unlocked:", ACHIEVEMENTS[0])
        else:
            print("You have been defeated by the werewolf.")
        self.running = False

if __name__ == "__main__":
    game = Game()
    game.start()