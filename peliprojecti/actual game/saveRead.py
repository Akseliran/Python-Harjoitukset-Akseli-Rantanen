import os
import json

baseDirectory = os.path.dirname(os.path.abspath(__file__)) # get the path of the script
saveDirectory = os.path.join(baseDirectory, "saves") # saves folder inside the directory // SCRIPT DOES NOT MAKE THIS, YOU NEED TO ADD IT MANUALLY

def save_path(name):
   return os.path.join(saveDirectory, f"save_{name}.txt") #/saves/save_name.txt

def save_game(name, day, ants, today_boost): # only saves the day, the amount of ants and active buffs. Unfinished
    with open(save_path(name), "w", encoding="utf-8") as saveFile:
        json.dump({"day": day, "ants": ants, "boost": today_boost}, saveFile)

def load_game(name): # reads the json file, returns null if anything is invalid
    try:
        with open(save_path(name), "r", encoding="utf-8") as file:
            data = json.load(file)
        return data["day"], data["ants"], data["boost"]
    except (FileNotFoundError, KeyError, ValueError):
        return None