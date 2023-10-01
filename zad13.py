# Oblicz średnią harmoniczną wymyślonej listy
lista = []
while True:
    inp = input("Wprowadź liczbę: ")
    if inp == "stop":
        break
    else:
        inp = int(inp)
        if inp != 0:
            lista.append(inp)
i = 0
a = 0
while i < len(lista):
    a += 1/lista[i]
    i += 1

if a != 0:
    print("Średnia harmoniczna:", len(lista)/a)
