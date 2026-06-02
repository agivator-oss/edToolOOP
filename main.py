from cave import Cave
from character import Enemy, Friend
from item import Item

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

harry = Enemy("Harry", "A smelly Wumpus")
harry.set_conversation("Hangry…Hanggrry")
harry.set_weakness("vegemite")
dungeon.set_character(harry)

josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)

vegemite = Item("vegemite")
vegemite.set_description("a Wumpuses worst nightmare")
grotto.set_item(vegemite)

torch = Item("torch")
torch.set_description("a light for the end of the tunnel")
dungeon.set_item(torch)

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

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item)
            current_cave.set_item(None)



    


