from time import sleep
#kerta = 1

#while kerta <= 30:
#    print(kerta)
#    kerta += 2

#PAMREMPI TAPA vvvvv
#while kerta <= 30:
#    if kerta % 2 == 1:
#        print(kerta)
#    kerta += 1

countdown = int(input("Anna luku: "))
while countdown > 0:
    print(countdown)
    sleep(1)
    countdown -= 1
print("Kaboom!")