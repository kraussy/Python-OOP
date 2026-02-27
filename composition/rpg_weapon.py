"""7. Mini RPG Game
Build a tiny game where players have weapons, armor, and an inventory — all composed objects.
▲ Hide
Create a Weapon class with name and damage."""
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

"""Create an Armor class with name and defense."""
class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense
        
"""Create an Inventory class that holds a list of item names and has add_item() and show() methods."""
class Inventory:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
        
    def show(self):
        print("List of items:")
        for i in self.items:
            print(i)

"""Create a Player class with name, health, and composed Weapon, Armor, and Inventory objects."""
class Player:
    def __init__(self, name, health, weapon_name, weapon_damage, armor_name, armor_defense):
        self.name = name
        self.health = health
        self.weapon = Weapon(weapon_name, weapon_damage)
        self.armor = Armor(armor_name, armor_defense)
        self.inventory = Inventory()
        
    """Add an attack(other_player) method that reduces the other player's health by weapon. damage - other.armor.defense."""
    def attack(self, other_player):
        damage = self.weapon.damage - other_player.armor.defense
        
        if damage < 0:
            damage = 0 
            
        other_player.health -= damage
        print(f"{self.name} attacks {other_player.name} for {damage} damage!")
        
    def status(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Weapon: {self.weapon.name} (Damage: {self.weapon.damage})")
        print(f"Armor: {self.armor.name} (Defense: {self.armor.defense})")
        print()
    
player1 = Player("Arthur", 100, "Sword", 25, "Steel Armor", 10)
player2 = Player("Lancelot", 100, "Axe", 20, "Iron Armor", 5)

for round in range(10):
    print(f"--- Round {round + 1} ---")
    player1.attack(player2)
    player2.attack(player1)
    player1.status()
    player2.status()
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
