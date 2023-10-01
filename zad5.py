# Zsumuj wszystkie liczby które są są podzielne przez 5 do wartości podanej przez użytkownika.
suma = 0
inp = int(input("Podaj liczbę: "))
i = 0
while i <= inp:
    if i%5 == 0:
        suma += i
    i += 132
print(suma) 