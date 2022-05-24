import math
i = int(input())
for x in range(i):
  liczby = input().split(" ")
  for x in liczby:
    int(x)
  list=[]
  list.append(liczby)
  suma=[]
  for liczba in list: 
        if len(list) == 1:
          pole = 3.14*(list[0]**2)
          suma.append(pole)
        elif len(list) == 2:
          pole1 = list[0]*list[1]
          suma.append(pole1)
        elif len(list) == 3:
          pole2 = list[0]*list[1]/2
          suma.append(pole2)
        elif len(list) == 4:
          print("Błąd: można podać maksymalnie 3 liczby")
        print(sum(suma))