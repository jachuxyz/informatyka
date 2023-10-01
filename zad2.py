# Napiszmy program który wyświetli nam wszystkie liczby podzielne przez 9. Do wartości podanej przez użytkownika.
inp = int(input("Podaj liczbę: "))
i = 0
while i <= inp:
    if i%9 == 0:
        print(i)
    i += 1