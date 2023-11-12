# 1. Napisz funkcję która przyjmuje trzy listy i powie w której z nich znajduje się największa średnia.

# def najwiekszasrednia(list1, list2, list3):
#     avg = lambda list0: sum(list0)/len(list0)
#     lists = [list1, list2, list3]
#     avglists = []
#     for i in range(0, 3):
#         avglists.append(avg(lists[i]))
#     return avglists.index(max(avglists))+1
#
# print(najwiekszasrednia([3, 6, 9], [1, 2, 3], [4, 5, 6, 7, 8, 9, 2943]))

# 2. Napisz funkcję która generuje losową listę o wielkości k i zakresie n i m.
# import random
# randomlist = lambda k,n,m: [random.randint(n,m) for i in range(k)]
# print(randomlist(15, 20, 40))

# 3. Napisz funkcję która przyjmuje listę i podniesie wszystkie elementy do kwadratu
# tosquare = lambda lst: list(map(lambda el: el**2, lst))
# print(tosquare([1, 5, 6, 9, 12, 15]))

# 4. Napisz funkcję która przyjmuje listę i podniesie wszystkie elementy do 1/2
# toroot = lambda lst: list(map(lambda el: el**(1/2), lst))
# print(toroot([1, 5, 6, 9, 12, 15]))

# 5. Napisz funkcję która przyjmuje listę jako argument w zwróci ile występuje liczb parzystych
parzystych = lambda lst: len(list(filter(lambda el: el % 2 == 0, lst)))
print(parzystych([1, 4, 3, 5, 7, 8, 12, 10]))