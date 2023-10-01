# Napisz program co wprowadzi x ocen (1 do 6) a następnie obliczy nam średnią  arytmetyczną.
oceny = []
while True:
    inp = input("Wprowadź ocenę: ")
    if inp == "stop":
        break
    else:
        inp = int(inp)
        if inp >= 1 and inp <= 6:
            oceny.append(inp)
        else:
            print("Podałeś złe liczby Nobie!")
i = 0
srednia = 0
while i < len(oceny):
    srednia += oceny[i]
    i += 1
srednia = srednia/len(oceny)
print("Średnia:", srednia)