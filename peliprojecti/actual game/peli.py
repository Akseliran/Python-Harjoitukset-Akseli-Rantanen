import baseValues
import classes
import display
import saveRead
import random



# creating the games objects here, im not sure where if i should do this somewhere else so this will do
home = classes.Room("Home")
shop = classes.Room("Shop", [classes.Accelerant("growth accelerator", 5, 0.5), classes.Seed("pumpkin seed", 1, random.randint(1, 3))])
farm = classes.Room("Farm", [classes.Accelerant("pumpkin", 5, 0.1)])
rooms = {"home": home, "shop": shop, "farm": farm}



def PlayerSetup():
    name = input("Player name: ")
    player = classes.Pelaaja(name, home, None)
    return player

def main():
    player = PlayerSetup()
    ants = baseValues.startingAnts
    day = 1
    today_boost = 0.0


    saved = saveRead.load_game(player.name)
    if saved:
        if input("Saved game found. Continue? (y/n) ").lower() == "y":
            day, ants, today_boost = saved

    while day <= baseValues.days:
        display.show_status(day, ants, today_boost)
        command = input("> ").lower()

        if command == "end":
            growth = baseValues.baseGrowth + today_boost
            new_ants = int(ants * growth)
            print(f"The colony grew by +{display.format_ants(new_ants - ants)} overnight.")
            ants = new_ants
            today_boost = 0.0
            day += 1
        elif command.startswith("use "):
            item = player.findItem(command[4:])
            
            if item is None:
                print("You don't have that item.")
            elif isinstance(item, classes.Accelerant):
                today_boost += item.boost
                # DOESNT REMOVE THE ITEM WHEN USED DUE TO THE GAME OTHERWISE UNBEATABLE IN ITS CURRENT STATE
                print(f"Used {item.name}: +{item.boost:.2f} growth tonight.")
            elif isinstance(item, classes.Seed):
                # UNFINISHED
                print("Seed test")

        elif command == "inventory":
            for item in player.inventory: # print different info depending on the type of item
                if isinstance(item, classes.Accelerant):
                    print(f"- {item.name} (+{item.boost:.2f})")
                elif isinstance(item, classes.Seed):
                    print(f"- {item.name} ({item.growtime:.2f} days growtime)")
       
        elif command == "quit":
            print("Saving game and stopping.")
            saveRead.save_game(player.name, day, ants, today_boost)
            return
        
        elif command.startswith("move" ):
            destination = player.findRoom(command[5:])
            room = rooms.get(destination)
            if room is None:
                print(f"No such place. Options: {', '.join(rooms)}")
            else:
                player.move(room)
                print(f"You walk to the {room.name}.")

        elif command.startswith("pickup "):
            item = player.pickUp(command[7:])
            if item is None:
                print("There's no such item in this room")
            else:
                print(f"You picked up {item}.")

        elif command == "look":
            print(f"You are in the {player.position.name}.")
            if player.position.items:
                for item in player.position.items:
                    print(f"- {item.name}")
            else:
                print("There's nothing here.")

        else:
            print("Commands: use <item name>, move <destination>, pickup <item name>, inventory, end, quit, look")

    print(f"\nFinal count: {display.format_ants(ants)} ants")
    if ants >= baseValues.target:
        print("You reached the goal, you win!")
    else:
        print("You couldn't reach your goal in time, You lose.")

main()