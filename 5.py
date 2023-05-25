valor = float(input("Digite o valor: "))
taxa = float(input("Digite a taxa: "))
tempo = float(input("Digite o tempo: "))

prestacao = valor + (valor * (taxa/100) * tempo)

print(f"O valor da prestação é: {prestacao}")