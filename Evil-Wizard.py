import random

# -----------------------------
# Base Character Class
# -----------------------------
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power

    def attack(self, opponent):
        damage = random.randint(int(self.attack_power*0.8), int(self.attack_power*1.2))
        # 20% chance for critical hit
        if random.random() < 0.2:
            damage *= 2
            print("Critical Hit!")
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = random.randint(15, 25)
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# -----------------------------
# Warrior Class
# -----------------------------
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.berserk_cd = 0

    def berserk(self, opponent):
        if self.berserk_cd > 0:
            print("Berserk is on cooldown!")
            return
        damage = random.randint(30, 50)
        opponent.health -= damage
        print(f"{self.name} uses Berserk! Deals {damage} damage to {opponent.name}.")
        self.berserk_cd = 3  # cooldown 3 turns

# -----------------------------
# Mage Class
# -----------------------------
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.fireball_cd = 0
        self.shield_cd = 0

    def fireball(self, opponent):
        if self.fireball_cd > 0:
            print("Fireball is on cooldown!")
            return
        damage = random.randint(25, 45)
        opponent.health -= damage
        print(f"{self.name} casts Fireball! Deals {damage} damage to {opponent.name}.")
        self.fireball_cd = 3

    def shield(self):
        if self.shield_cd > 0:
            print("Shield is on cooldown!")
            return
        shield_amount = random.randint(10, 20)
        self.health += shield_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} casts Shield! Gains {shield_amount} health.")
        self.shield_cd = 3

# -----------------------------
# Archer Class
# -----------------------------
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=20)
        self.quick_shot_cd = 0
        self.evade_next = False

    def quick_shot(self, opponent):
        if self.quick_shot_cd > 0:
            print("Quick Shot is on cooldown!")
            return
        damage1 = random.randint(10, 20)
        damage2 = random.randint(10, 20)
        total = damage1 + damage2
        opponent.health -= total
        print(f"{self.name} uses Quick Shot! Hits {opponent.name} twice for {total} damage.")
        self.quick_shot_cd = 3

    def evade(self):
        self.evade_next = True
        print(f"{self.name} prepares to evade the next attack!")

# -----------------------------
# Paladin Class
# -----------------------------
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=22)
        self.holy_strike_cd = 0
        self.shield_next = False

    def holy_strike(self, opponent):
        if self.holy_strike_cd > 0:
            print("Holy Strike is on cooldown!")
            return
        damage = random.randint(20, 35)
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike! Deals {damage} damage to {opponent.name}.")
        self.holy_strike_cd = 3

    def divine_shield(self):
        self.shield_next = True
        print(f"{self.name} activates Divine Shield! Will block the next attack.")

# -----------------------------
# Evil Wizard Class
# -----------------------------
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        regen = random.randint(5, 15)
        self.health += regen
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates {regen} health! Current health: {self.health}")

    def take_turn(self, player):
        # 20% chance to cast Dark Blast
        if random.random() < 0.2:
            damage = random.randint(25, 40)
            player.health -= damage
            print(f"{self.name} casts Dark Blast! Deals {damage} damage to {player.name}!")
        # 10% chance to summon minion
        elif random.random() < 0.1:
            damage = random.randint(5, 15)
            player.health -= damage
            print(f"{self.name} summons a minion! Deals {damage} extra damage to {player.name}!")
        else:
            damage = random.randint(int(self.attack_power*0.8), int(self.attack_power*1.2))
            # Archer dodge chance
            if isinstance(player, Archer) and (player.evade_next or random.random() < 0.1):
                print(f"{player.name} evades the attack!")
                player.evade_next = False
                return
            # Paladin shield
            if isinstance(player, Paladin) and player.shield_next:
                print(f"{player.name}'s Divine Shield blocks the attack!")
                player.shield_next = False
                return
            player.health -= damage
            print(f"{self.name} attacks {player.name} for {damage} damage!")

        if player.health < 0:
            player.health = 0

# -----------------------------
# Character Creation
# -----------------------------
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# -----------------------------
# Battle System
# -----------------------------
def battle(player, wizard):
    turn_counter = 1
    while wizard.health > 0 and player.health > 0:
        print(f"\n--- Turn {turn_counter} ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        choice = input("Choose an action: ")

        # Player Turn
        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                player.berserk(wizard)
            elif isinstance(player, Mage):
                sub = input("1. Fireball\n2. Shield\nChoose ability: ")
                if sub == '1':
                    player.fireball(wizard)
                else:
                    player.shield()
            elif isinstance(player, Archer):
                sub = input("1. Quick Shot\n2. Evade\nChoose ability: ")
                if sub == '1':
                    player.quick_shot(wizard)
                else:
                    player.evade()
            elif isinstance(player, Paladin):
                sub = input("1. Holy Strike\n2. Divine Shield\nChoose ability: ")
                if sub == '1':
                    player.holy_strike(wizard)
                else:
                    player.divine_shield()
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            wizard.display_stats()
        else:
            print("Invalid choice!")

        # Cooldown reductions
        for attr in ['berserk_cd', 'fireball_cd', 'shield_cd', 'quick_shot_cd', 'holy_strike_cd']:
            if hasattr(player, attr) and getattr(player, attr) > 0:
                setattr(player, attr, getattr(player, attr)-1)

        if wizard.health <= 0:
            print(f"\n{wizard.name} has been defeated! Victory for {player.name}!")
            break

        # Enemy Turn
        print("\n--- Evil Wizard's Turn ---")
        wizard.regenerate()
        wizard.take_turn(player)

        if player.health <= 0:
            print(f"\n{player.name} has been defeated! The Evil Wizard wins!")
            break

        turn_counter += 1

# -----------------------------
# Main Game
# -----------------------------
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
