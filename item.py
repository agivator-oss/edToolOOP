class Item():
    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    def get_name(self):
        return self.name
    
    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description
    
    def set_description(self, item_description):
        self.description = item_description

    # Describe this item
    def describe(self):
        print( "The " + self.name + " item is here!" )
        print( "  It is " + self.description )


# Extension 3 - Inheritance:
# New subclass `Weapon` inherits from `Item` and adds two attributes
# (`damage` and `durability`) plus getter/setter methods and a `use()` method.
class Weapon(Item):
    def __init__(self, item_name, damage=5, durability=10):
        super().__init__(item_name)
        self.damage = damage
        self.durability = durability

    # Getter and setter for damage
    def get_damage(self):
        return self.damage

    def set_damage(self, damage):
        self.damage = damage

    # Getter and setter for durability
    def get_durability(self):
        return self.durability

    def set_durability(self, durability):
        self.durability = durability

    # A simple method to 'use' the weapon; it reduces durability and
    # returns the damage value so the game can apply it.
    def use(self):
        if self.durability <= 0:
            print("The " + self.name + " is broken and cannot be used.")
            return 0
        self.durability -= 1
        print("You swing the " + self.name + ", durability now " + str(self.durability))
        return self.damage

