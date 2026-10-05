import os
import json

baseDirectory = os.path.dirname(os.path.abspath(__file__))
saveDirectory = os.path.join(baseDirectory, "saves")

def save_path(name):
   return os.path.join(saveDirectory, f"save_{name}.txt")

def save_game(name, day, ants, today_boost):
    with open(save_path(name), "w", encoding="utf-8") as saveFile:
        json.dump({"day": day, "ants": ants, "boost": today_boost}, saveFile)

def load_game(name):
    try:
        with open(save_path(name), "r", encoding="utf-8") as file:
            data = json.load(file)
        return data["day"], data["ants"], data["boost"]
    except (FileNotFoundError, KeyError, ValueError):
        return None