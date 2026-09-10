
def move(x, y, z):
    wasd = input("move up down left or right? (WASD, space or down)\n")
    if wasd == "w":
        x += 1
    if wasd == "s":
        x -=1
    if wasd == "a":
        z -= 1
    if wasd == "d":
        z += 1
    if wasd == " ":
        y += 1
    if wasd == "down":
        y -=1
    return x, y, z




# initial coordinates
x, y, z = 0, 0, 0

while True:
    print("Your coordinates ", x, y, z)
    x, y, z = move(x, y, z)
