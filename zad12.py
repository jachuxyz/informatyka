# Wygeneruj listę losowych liczb o n wielkości z zakresu od 1 do 100.
import random

inp = int(input("Podaj liczbę: "))
losowe = []

i = 0
while i < inp:
    losowe.append(random.randint(1, 100))
    i += 1
print(losowe)