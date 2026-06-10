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
    
class Enemy(Character):

    enemies_to_defeat = 0

    def __init__(self, char_name, char_description):
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1

        super().__init__(char_name, char_description)

        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
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

