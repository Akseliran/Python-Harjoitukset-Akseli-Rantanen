from math import pi
def pizzaCostValue(halkaisija, hinta):
    size = halkaisija**2 * pi
    return hinta / size

inputHinta = float(input("Anna pizzan hinta: "))
inputHalkaisija = float(input("Anna pizzan halkaisija: "))
inputHinta2 = float(input("Anna toisen pizzan hinta: "))
inputHalkaisija2 = float(input("Anna toisen pizzan halkaisija: "))
print(f"Pizzan hinta per neliösenttimetri on {pizzaCostValue(inputHalkaisija, inputHinta):0.2f} euroa\nToisen pizzan hinta per neliösenttimetri on {pizzaCostValue(inputHalkaisija2, inputHinta2):0.2f} euroa")
if pizzaCostValue(inputHalkaisija, inputHinta) < pizzaCostValue(inputHalkaisija2, inputHinta2):
    print("Ensimmäinen pizza on parempi hinnan puolesta.")
elif pizzaCostValue(inputHalkaisija, inputHinta) == pizzaCostValue(inputHalkaisija2, inputHinta2):
    print("Pizzat ovat yhtä hyviä hinnan puolesta.")
else:
    print("Toinen pizza on parempi hinnan puolesta.")