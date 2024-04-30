class Hero():
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0

class Game():
    def __init__(self, player_name):
        self.player = Hero(player_name, 100, 20)
        self.computer = Hero("BOT", 100, 15)

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            print(f"{self.player.name} атакует {self.computer.name}")
            self.player.attack(self.computer)
            print(f"У {self.computer.name} здоровье - {self.computer.health}")

            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break

            print(f"{self.computer.name} атакует {self.player.name}")
            self.computer.attack(self.player)
            print(f"У {self.player.name} здоровье - {self.player.health}")

            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break

if __name__ == "__main__":
    game = Game("Игрок")
    game.start()

