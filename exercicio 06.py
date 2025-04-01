from glob import glob1

time1 = input ("Digite o nome do primeiro time: ")
time2 = input ("Digite o nome do segundo time: ")
goltime1 = int(input(f"Digite a quantidade de gols do {time1}."))
goltime2 = int(input(f"Digite a quantidade de gols do {time2}."))

if goltime1 > goltime2:
    print (f"{time1} venceu!")
else:
    if goltime2 > goltime1:
        print (f"{time2} venceu!")
    else:
        print ("Empate!")