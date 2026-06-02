class Cave:
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = None
        self.item = None

    # Here is a method to get the description of the cave:
    def get_description(self):
        return self.description
    
    # Here is a method to set the description of the cave:
    def set_description(self, cave_description):
        self.description = cave_description

    # Here is a method to get the name of the cave:
    def get_name(self):
        return self.name
    
    # Here is a method to set the name of the cave:
    def set_name(self, cave_name):
        self.name = cave_name

    # Setter for character
    def set_character(self, character):
        self.character = character

    # Getter for character
    def get_character(self):
        return self.character
    
    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def describe(self):
        print(self.description)

    # This method is used to link caves
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link
        #print( self.name + " linked caves :" + repr(self.linked_caves) )

    def get_details(self):
        print(self.name + ": " + self.description)

        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print( "The " + cave.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way")
            return self


