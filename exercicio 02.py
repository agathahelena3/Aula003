n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))

adição = n1 + n2
subtração = n1 - n2
divisão = n1 / n2
multiplicação = n1 * n2

print (f"{n1} mais {n2} é igual a {adição}. "
       f"{n1} menos {n2} é igual a {subtração}. {n1} dividido por {n2} é igual a {divisão:2f}. {n1} vezes {n2} é igual a {multiplicação}.")