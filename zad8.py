# Stwórz listę zawierającą x liczb wprowadzonych przez użytkownika od (1 do 200)
lista = []
while True:
    inp = input("Wprowadź liczbę: ")
    if inp == "stop":
        break
    else:
        inp = int(inp)
    if inp >= 1 and inp <= 200:
        lista.append(inp)
    else:
        print("Niepoprawna liczba")
print(lista)