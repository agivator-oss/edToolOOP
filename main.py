from cave import Cave
from character import Enemy, Friend, Player
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

goblin = Enemy("Goblin", "A small, sneaky cave goblin", hp=40, damage=12)
goblin.set_conversation("Graaah! Leave my shiny!")
goblin.set_weakness("sword")
crypt.set_character(goblin)

old_sage = Friend("Old Sage", "A wise old traveller")
old_sage.set_conversation("Seek and you shall find")
cavern.set_character(old_sage)

amulet = Item("amulet")
amulet.set_description("a glowing talisman with strange runes")
crypt.set_item(amulet)

harry = Enemy("Harry", "A smelly Wumpus", hp=60, damage=15)
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

player = Player("Hero", hp=100)
current_cave = cavern
endGame = False

print("Welcome to the RPG. Use commands: north, south, east, west, stats, bag, take, fight, interact, talk, pat")

while endGame == False:
    print("\n")
    current_cave.get_details()
    print("Player HP: " + str(player.hp))

    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_cave.get_item()
    if item is not None:
        item.describe()

    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_cave = current_cave.move(command)

    elif command == "stats":
        print("--- Player Stats ---")
        print("Name: " + player.name)
        print("HP: " + str(player.hp))
        print("Enemies left: " + str(Enemy.enemies_to_defeat))

    elif command == "bag":
        player.list_bag()

    elif command == "take":
        if item is not None:
            player.add_to_bag(item)
            current_cave.set_item(None)
        else:
            print("There is nothing here to take.")

    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            bag_item = player.get_bag_item(fight_with)

            if bag_item is None:
                print("You don't have a " + fight_with)
            else:
                result = inhabitant.fight(bag_item, player=player)
                if result == True:
                    print("Bravo, hero, you won the fight!")
                    current_cave.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have survived another adventure!")
                        endGame = True
                else:
                    if player.hp == 0:
                        print("You have been defeated and your HP is 0.")
                        print("Game Over")
                        endGame = True
                    else:
                        print("You survived the fight but did not defeat " + inhabitant.name + ".")

        else:
            print("There is no one here to fight with")

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is no one here to talk to")

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
        # Calls `interact()` on the inhabitant.
        if inhabitant is not None:
            inhabitant.interact()
        else:
            print("There is no one here to interact with")

    else:
        print("I don't understand that command.")

    if player.hp == 0:
        print("Your HP has reached 0. The adventure ends.")
        endGame = True


