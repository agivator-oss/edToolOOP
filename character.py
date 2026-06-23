from item import Weapon

class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        # Extension 2: new attribute for characters (simple health points)
        # This attribute demonstrates adding a new attribute to a sample class.
        self.hp = 100

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Extension 2: new method to change or report HP
    # Demonstrates adding a method operating on a new attribute
    def adjust_hp(self, amount):
        self.hp += amount
        # Keep hp within reasonable bounds
        if self.hp < 0:
            self.hp = 0
        print(self.name + " now has " + str(self.hp) + " HP")

    # Extension 4: polymorphic method defined on superclass
    # Subclasses will override this to provide different interactions
    def interact(self):
        print(self.name + " does not react in a special way.")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
class Player(Character):
    def __init__(self, char_name, hp=100):
        super().__init__(char_name, "A brave adventurer")
        self.hp = hp
        self.bag = []

    def add_to_bag(self, item):
        self.bag.append(item)
        print("You put the " + item.get_name() + " in your bag")

    def list_bag(self):
        if len(self.bag) == 0:
            print("Your bag is empty.")
        else:
            print(self.name + "'s bag contains:")
            for item in self.bag:
                if isinstance(item, Weapon):
                    print("  - " + item.get_name() + " (weapon, damage " + str(item.get_damage()) + ", durability " + str(item.get_durability()) + ")")
                else:
                    print("  - " + item.get_name())

    def get_bag_item(self, item_name):
        for item in self.bag:
            if item.get_name() == item_name:
                return item
        return None

class Enemy(Character):

    enemies_to_defeat = 0

    def __init__(self, char_name, char_description, hp=50, damage=10):
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1

        super().__init__(char_name, char_description)
        self.hp = hp
        self.damage = damage
        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item, player=None):
        # Weapon-based fight system uses weapon damage and enemy HP.
        if isinstance(combat_item, Weapon):
            weapon = combat_item
            weapon_damage = weapon.use()
            if weapon_damage == 0:
                print("Your weapon is broken and does no damage.")
                return False

            print("You attack " + self.name + " with the " + weapon.get_name())
            self.adjust_hp(-weapon_damage)

            if weapon.get_name() == self.weakness:
                print("The " + weapon.get_name() + " is especially effective!")
                Enemy.enemies_to_defeat -= 1
                return True

            if self.hp == 0:
                print("You defeat " + self.name + " with the " + weapon.get_name())
                Enemy.enemies_to_defeat -= 1
                return True

            print(self.name + " still stands with " + str(self.hp) + " HP.")
            if player is not None:
                player.adjust_hp(-self.damage)
                print(self.name + " hits you for " + str(self.damage) + " damage.")
            return False

        # Backwards compatibility for old string-based fight calls
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1
            return True
        else:
            print(self.name + " swallows you, little wimp")
            return False

    # Extension 4: override polymorphic method from Character
    def interact(self):
        print(self.name + " snarls and tries to intimidate you!")
        
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None

    def pat(self):
        print(self.name + " pats you back!")

    # Extension 4: override polymorphic method from Character
    def interact(self):
        print(self.name + " smiles and offers friendly help.")

