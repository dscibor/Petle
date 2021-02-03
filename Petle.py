import time
import os

for i in range(1, 10, 1):
    if i <= 10:
        print(i)


for i in range(4, -1, -1):
    if i >= -1:
        print(i)


for i in range(15 , -1, -1):
    os.system("cls")
    print(i)
    time.sleep(1)

    
print("Jebut")

imie = input("Podaj imię: ")    
liczba = input("Podaj liczbę całkowitą: ")
x = range(int(liczba))
for liczba in x:
      print(liczba + 1, imie)
      

populacja = 1
godzin = 0

while(populacja <= 1_000_000_000):
    godzin += 1
    populacja *= 2
    print("Minęło godzin: ", (godzin))
    print("Liczba bakterii: ", (populacja))
    
