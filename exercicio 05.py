nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

media = (nota1 + nota2 + nota3)/3
print (media)

if media >= 7:
    print ("Aprova")
else:
    if media <=4:
        print ("Reprovado!")
    else:
         print ("Recuperação!")