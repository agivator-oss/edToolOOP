from cave import Cave
from character import Enemy, Friend
from item import Item, Weapon

cavern = Cave("cavern")
cavern.set_description("A damp and dirty cave.")

grotto = Cave("grotto")
grotto.set_description("A small cave with ancient graffiti")

dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack")

cavern.link_cave(dungeon, "south")
dungeon.link_cave(cavern, "north")
grotto.link_cave(dungeon, "east")
dungeon.link_cave(grotto, "west")

# Extension 1 - Instantiation:
# Create one new Cave, Enemy, Friend and Item to demonstrate instantiation
crypt = Cave("crypt")
crypt.set_description("An eerie crypt with moss-covered stones")
grotto.link_cave(crypt, "south")
crypt.link_cave(grotto, "north")

goblin = Enemy("Goblin", "A small, sneaky cave goblin")
goblin.set_conversation("Graaah! Leave my shiny!")
goblin.set_weakness("sword")
crypt.set_character(goblin)

old_sage = Friend("Old Sage", "A wise old traveller")
old_sage.set_conversation("Seek and you shall find")
cavern.set_character(old_sage)

amulet = Item("amulet")
amulet.set_description("a glowing talisman with strange runes")
crypt.set_item(amulet)

harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry…Hanggrry")
harry.set_weakness("vegemite")
dungeon.set_character(harry)

josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)

# Extension 2 - Method and Attribute:
# Demonstrate new `hp` attribute and `adjust_hp()` method on a character.
# We call `adjust_hp` on Josephine to show the attribute in use.
josephine.adjust_hp(-10)

vegemite = Item("vegemite")
vegemite.set_description("a Wumpuses worst nightmare")
grotto.set_item(vegemite)

torch = Item("torch")
torch.set_description("a light for the end of the tunnel")
dungeon.set_item(torch)

# Extension 3 - Inheritance:
# Instantiate a `Weapon` (subclass of Item) that has damage and durability.
sword = Weapon("sword", damage=8, durability=3)
sword.set_description("a sturdy iron sword")
cavern.set_item(sword)

bag = []

# Method to see if an item name matches an item in the bag
def in_bag(item_name):
    for item in bag:
        if item.get_name() == item_name:
            return True
        
    return False

current_cave = cavern  
endGame = False        
while endGame == False:		
    print("\n")         
    current_cave.get_details()

    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_cave.get_item()
    if item is not None:
        item.describe()

    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_cave = current_cave.move(command)  

    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Check the item is in the bag
            if in_bag(fight_with):
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Bravo,hero you won the fight!")
                    current_cave.set_character(None)

                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have survived another adventure!")
                        endGame = True

                else:
                    print("Scurry home, you lost the fight.")
                    print("That's the end of the game")
                    endGame = True
            else:
                print("You don't have a " + fight_with)

        else:
            print("There is no one here to fight with")

    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you…")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat :(")

    elif command == "interact":
        # Extension 4 - Polymorphism:
        # Calls `interact()` on the inhabitant. The method is defined on the
        # superclass and overridden in `Enemy` and `Friend` to show polymorphism.
        if inhabitant is not None:
            inhabitant.interact()
        else:
            print("There is no one here to interact with")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item)
            current_cave.set_item(None)



    


