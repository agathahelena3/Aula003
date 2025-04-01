nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salário = float(input("Digite o seu salário:"))
aumento = float(input("Digite a porcentagem do seu aumento:"))
aumentoreal = salário * aumento /100
salárioatual = salário + aumentoreal


print (f"Olá, seu nome é {nome}, você tem {idade} anos e seu salário é {salário:.2f}. O aumento do seu salário foi de {aumento}%, ou seja R${aumentoreal:.2f}. Seu salário atual é de R${salárioatual:.2f}")
