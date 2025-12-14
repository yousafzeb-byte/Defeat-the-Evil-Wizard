# 🧙‍♂️ Evil Wizard Battle

A turn-based RPG game built with Python using Object-Oriented Programming principles. Choose your hero class and battle the powerful Evil Wizard using unique abilities, strategic healing, and tactical combat.

## 🎮 Features

- **4 Playable Character Classes** with unique stats and abilities
- **Turn-Based Combat System** with strategic decision-making
- **Special Abilities** with cooldown mechanics
- **Randomized Damage** with critical hit system (20% chance for 2x damage)
- **Healing System** that respects maximum health limits
- **Smart Enemy AI** with regeneration, varied attacks, and special moves
- **Defensive Mechanics** including evasion and shield blocking

## 🎯 Character Classes

### ⚔️ Warrior

- **Health:** 140 | **Attack:** 25
- **Abilities:**
  - **Berserk:** Unleash fury for 30-50 damage (3-turn cooldown)

### 🔮 Mage

- **Health:** 100 | **Attack:** 35
- **Abilities:**
  - **Fireball:** Cast a powerful fireball for 25-45 damage (3-turn cooldown)
  - **Shield:** Generate a protective shield restoring 10-20 health (3-turn cooldown)

### 🏹 Archer

- **Health:** 90 | **Attack:** 20
- **Abilities:**
  - **Quick Shot:** Fire two arrows dealing combined 20-40 damage (3-turn cooldown)
  - **Evade:** Dodge the next incoming attack

### 🛡️ Paladin

- **Health:** 120 | **Attack:** 22
- **Abilities:**
  - **Holy Strike:** Divine attack dealing 20-35 damage (3-turn cooldown)
  - **Divine Shield:** Block the next attack completely

## 🎲 Evil Wizard Mechanics

The Dark Wizard is a formidable opponent with:

- **150 Health**
- **Regeneration:** Heals 5-15 HP per turn
- **Dark Blast:** Powerful spell dealing 25-40 damage (20% chance)
- **Minion Summoning:** Summons creatures for 5-15 extra damage (10% chance)
- **Regular Attacks:** Base attack with damage variation

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yousafzeb-byte/Defeat-the-Evil-Wizard.git
```

2. Navigate to the project directory:

```bash
cd Defeat-the-Evil-Wizard
```

3. Run the game:

```bash
python Evil-Wizard.py
```

## 🕹️ How to Play

1. **Choose Your Class:** Select from Warrior, Mage, Archer, or Paladin
2. **Enter Your Name:** Personalize your hero
3. **Battle Menu:**

   - **Attack:** Standard attack with random damage
   - **Use Special Ability:** Access class-specific powerful moves
   - **Heal:** Restore 15-25 health points
   - **View Stats:** Check current health and attack power

4. **Victory Condition:** Reduce the Evil Wizard's health to 0
5. **Defeat Condition:** Your health reaches 0

## 💻 Technical Highlights

- **Object-Oriented Design:** Base `Character` class with inheritance for all heroes and enemies
- **Encapsulation:** Each class manages its own attributes and methods
- **Polymorphism:** Specialized behaviors for different character types
- **Random Module:** Dynamic damage calculation and probability-based events
- **Game Loop:** Clean turn-based system with state management

## 📂 Project Structure

```
Defeat the Evil Wizard/
├── Evil-Wizard.py    # Main game file with all classes and logic
└── README.md         # Project documentation
```

## 🎓 Learning Objectives Achieved

✅ Implemented OOP principles (inheritance, encapsulation, polymorphism)  
✅ Created interactive menu-driven program  
✅ Designed turn-based game logic  
✅ Managed object interactions and state  
✅ Implemented cooldown and status effect systems  
✅ Added randomization for dynamic gameplay

## 🌟 Bonus Features

- **Critical Hit System:** 20% chance for double damage
- **Cooldown Management:** Prevents ability spam
- **Enhanced Enemy AI:** Multiple attack patterns
- **Defensive Abilities:** Evasion and blocking mechanics
- **Turn Counter:** Track battle progression
- **Dynamic Health Regeneration:** Variable healing amounts

## 👤 Author

**Yousaf Zeb**

- GitHub: [@yousafzeb-byte](https://github.com/yousafzeb-byte)

## 📝 License

This project is open source and available for educational purposes.

## 🎬 Demo

Run the game to experience:

- Strategic character selection
- Engaging turn-based combat
- Unique class abilities in action
- Dynamic battle outcomes

---

_Defeat the Evil Wizard and save the realm! 🏆_
