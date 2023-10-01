# Napisz program który z wypisze wszystkie liczby które NIE są podzielne przez 3.  Do wartości podanej przez użytkownika
inp = int(input("Podaj liczbę: "))
i = 0
while i <= inp:
    if i%3 != 0:
        print(i)
    i += 1