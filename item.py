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

