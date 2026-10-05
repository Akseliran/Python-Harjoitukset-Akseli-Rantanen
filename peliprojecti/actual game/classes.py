class Pelaaja:
    def __init__(self, name, position, inventory = None):
        self.name = name
        self.inventory = inventory if inventory is not None else []
        self.position = position

    def findItem(self, itemName):
        for item in self.inventory:
            if item.name.lower() == itemName.lower():
                return item
        return None
    
    def findRoom(self, roomName):
        self.roomName = roomName.lower()
        return self.roomName
    
    def move(self, room):
        self.position = room
    
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

class Farm(Room):
    def __init__(self, name, items = None, crops = None):
        super().__init__(name, items)
        self.crops = crops if crops is not None else []
    def plant(self, seed):
        self.crops.append[seed, seed.growtime]
    def time(self):
        finished = []
        for crop in self.crops[:]:
            crop[-1] -= 1
            if crop[1]<=0:
                self.crops.remove(crop)
                if crop[0].grown is not None:
                    self.items.append(crop[0].grown)
                    finished.append(crop[0].grown.name)
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