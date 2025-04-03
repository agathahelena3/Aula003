e = 4.90
g = 5.80

combustivel = input("Gasolina ou Etanol?\n"
                    "G para Gasolina\n"
                     "E para Etanol\n")
litros = float(input("Quantos litros foram abastecidos?"))


if combustivel == "g" or combustivel == "G":
  valor = g * litros
elif combustivel == "e" or combustivel == "E":
    valor =  e * litros
else: print ("Opção inválida. Selecione uma das opções.")

print (f"Você deverá pagar, R${valor:.2f}")