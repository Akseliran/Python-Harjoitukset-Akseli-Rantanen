pituus = float(input("Kuinka pitkä kuha on senttimetreissä?:\n"))
if pituus < 37:
    print(f"Kala on {37-pituus:.2f}alimittainen, päästä kala takaisin järveen")
else:
    print(f"Kala ei ole alamittainen, voit pitää sen.")
    