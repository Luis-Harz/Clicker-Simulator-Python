from ursina import *

class Game(Entity):
    def __init__(self):
        super().__init__()
        self.boss_health = 100  # Startleben des Bosses
        self.sword_power = 50  # Anfangskraft des Schwertes
        self.sword_upgrade_price = 10000
        self.boss_reward = 150
        self.player_money = 5000  # Startgeld des Spielers

        self.health_text = Text(position=(-0.6, 0.4), scale=2)
        self.power_text = Text(position=(-0.6, 0.3), scale=2)
        self.price_text = Text(position=(-0.6, 0.2), scale=2)
        self.reward_text = Text(position=(-0.6, 0.1), scale=2)
        self.money_text = Text(position=(-0.6, 0.0), scale=2)

        self.update_text()

        self.attack_button = Button(text='Attack', color=color.azure, position=(0, 0), scale=(0.3, 0.1), on_click=self.attack_boss)
        self.upgrade_button = Button(text='Upgrade Sword', color=color.orange, position=(0, -0.2), scale=(0.3, 0.1), on_click=self.upgrade_sword)
        self.new_sword_button = Button(text='Buy New Sword', color=color.green, position=(0, -0.4), scale=(0.3, 0.1), on_click=self.buy_new_sword)

    def attack_boss(self):
        self.boss_health -= self.sword_power
        if self.boss_health <= 0:
            print("Boss defeatet!")
            self.boss_health = 100 + (self.sword_power - self.boss_health)  # Der neue Boss hat 100 Leben mehr als der vorherige
            self.boss_reward += 150
            self.sword_upgrade_price += 1000
            self.player_money += self.boss_reward  # Belohnung wird dem Geld des Spielers hinzugefügt
        self.update_text()

        print(f"New life of the Boss: {self.boss_health}")
        print(f"New Price of the Sword: {self.sword_upgrade_price}€")
        print("-" * 30)

    def update_text(self):
        self.power_text.text = f"Sword Power: {self.sword_power}"
        self.health_text.text = f"Boss Life: {self.boss_health}"
        self.price_text.text = f"Sword Upgrade Price: {self.sword_upgrade_price}€"
        self.reward_text.text = f"Reward: {self.boss_reward}€"
        self.money_text.text = f"Money: {self.player_money}€"

    def upgrade_sword(self):
        if self.player_money >= self.sword_upgrade_price:
            self.sword_power += 10
            self.sword_upgrade_price += 10000
            self.player_money -= self.sword_upgrade_price
            self.update_text()
            print(f"New Sword Power: {self.sword_power}")
            print(f"New Price of the Sword: {self.sword_upgrade_price}€")
        else:
            print("Not enough Money for The Upgrade!")
        print("-" * 30)

    def buy_new_sword(self):
        new_sword_cost = self.sword_upgrade_price * 2  # Beispiel: Das neue Schwert kostet das Doppelte des aktuellen Schwertpreises
        if self.player_money >= new_sword_cost:
            self.sword_power += 20  # Beispiel: Das neue Schwert ist stärker
            self.sword_upgrade_price = new_sword_cost
            self.player_money -= new_sword_cost
            self.update_text()
            print(f"New Sword Power: {self.sword_power}")
            print(f"New Price of the Sword: {self.sword_upgrade_price}€")
        else:
            print("Not enough Money for a New Sword!")
        print("-" * 30)

if __name__ == '__main__':
    app = Ursina()
    game = Game()
    app.run()
