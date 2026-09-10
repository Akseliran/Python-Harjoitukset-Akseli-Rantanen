def toLiter(x):
    liter = x / 3.785
    return liter

gallon = float(input("Anna bensan määrä gallonoina: "))
print(f"Bensan määrä litroina on {toLiter(gallon):0.2f} litraa")