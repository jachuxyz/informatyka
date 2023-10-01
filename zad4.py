# Napisz program który wyświetli n potęg liczby 2.
inp = int(input("Podaj liczbę: "))
i = 0
while i <= inp:
    print("2 ^", i, "=", 2**i)
    i += 1