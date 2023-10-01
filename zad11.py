# Napisz program do którego możemy wprowadzić dowolne zdanie. Niech nasz program wyświetli ile mamy samogłosek.
samogloski = ["a", "A", "ą", "Ą", "e", "E", "ę", "Ę", "i", "I", "o", "O", "ó", "Ó", "u", "U", "y", "Y"]
zdanie = input("Wprowadź zdanie: ")

def jestsamogloska(litera):
    samogloska = False
    j = 0
    while j < len(samogloski):
        if litera == samogloski[j]:
            samogloska = True
        j += 1
    return samogloska

i = 0
suma = 0
while i < len(zdanie):
    if jestsamogloska(zdanie[i]):
        suma += 1
    i += 1

print("Liczba samogłosek:", suma)