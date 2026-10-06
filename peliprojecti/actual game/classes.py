class Pelaaja:
    def __init__(self, name, position, inventory = None):
        self.name = name
        self.inventory = inventory if inventory is not None else []
        self.position = position


# look through the players inventory for an item with a specific name, retunr none if it doesnt exist
    def findItem(self, itemName):
        for item in self.inventory:
            if item.name.lower() == itemName.lower():
                return item
        return None
# same thing as above but for rooms
    def findRoom(self, roomName):
        self.roomName = roomName.lower()
        return self.roomName
# move the player int odifferent rooms    
    def move(self, room):
        self.position = room
# removes an item from a rooms item list and adds it to players inventory.    
    def pickUp(self, itemName):
            for roomItem in self.position.items:
                if roomItem.name == itemName:
                    self.position.items.remove(roomItem)
                    self.inventory.append(roomItem)
                    return itemName
            

class Room:
    def __init__(self, name, items = None):
        self.name = name
        self.items = items if items is not None else []

class Farm(Room): # NOT FULLY FUNCTIONAL YET
    def __init__(self, name, items = None, crops = None):
        super().__init__(name, items)
        self.crops = crops if crops is not None else []

    def plant(self, seed):
        self.crops.append([seed, seed.growtime])

    def time(self):
        
        finished = [] #names of the crops that finish growing
        for crop in self.crops[:]:

            # subtract one day from the crops days_left
            crop[1] -= 1
            if crop[1] <= 0: # if the crop is done, remove it
                self.crops.remove(crop)
                if crop[0].grown is not None: # if the crop has the grown item set, append that to the farms item list
                    self.items.append(crop[0].grown)
                    finished.append(crop[0].grown.name) # add the name of the crop to the list of names getting returned
        return finished


class Item:
    def __init__(self, itemName, weight):
        self.name = itemName
        self.weight = weight

class Accelerant(Item):
    def __init__(self, itemName, weight, boost):
        super().__init__(itemName, weight)
        self.boost = boost

class Seed(Item):
    def __init__(self, itemName, weight, growtime, grown=None):
        super().__init__(itemName, weight)
        self.growtime = growtime
        self.grown = grown