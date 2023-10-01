# Sprawdzić czy zapytana liczba x jest liczbą pierwszą?
inp = int(input("Podaj liczbę: "))
pierwsza = True
i = 2
if inp > 1:
    while i < inp:
        if inp%i == 0:
            pierwsza = False
        i += 1
    if pierwsza:
        print("Liczba pierwsza")
    else:
        print("Liczba złożona")
else:
    print("Liczba musi być większa od 1")
