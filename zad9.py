# Na podstawie otrzymanej listy stwórz nową listę gdzie znajdują się: Liczby parzyste większe od 50 ale mniejsze od  70.Wyświetl je w konsoli z informacją ile zawierają elementów.
lista0 = []
while True:
    inp = input("Wprowadź liczbę: ")
    if inp == "stop":
        break
    else:
        inp = int(inp)
    lista0.append(inp)
lista1 = []
i = 0
while i < len(lista0):
    if lista0[i]%2 == 0 and lista0[i] > 50 and lista0[i] < 70:
        lista1.append(lista0[i])
    i += 1
print(lista1)
print("Długość listy:", len(lista1))