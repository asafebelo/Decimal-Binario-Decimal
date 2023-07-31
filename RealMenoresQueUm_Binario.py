def decimal_fracionario_para_binario(decimal_fracionario, precisao=10):
    binario = ""
    while decimal_fracionario > 0 and precisao > 0:
        decimal_fracionario *= 2
        inteiro_parte = int(decimal_fracionario)
        binario += str(inteiro_parte)
        decimal_fracionario -= inteiro_parte
        precisao -= 1
    return "0." + binario

def binario_fracionario_para_decimal(binario_fracionario):
    decimal = 0
    for i, bit in enumerate(binario_fracionario, start=1):
        decimal += int(bit) * (2 ** -i)
    return decimal

escolha = input("Escolha a conversão:\n1 - Decimal para Binário\n2 - Binário para Decimal\n")

if escolha == '1':
  numero_decimal = float(input("Digite um número real menor que 1: "))
  resultado_binario =     decimal_fracionario_para_binario(numero_decimal)
  print(f"O número binário equivalente é: {resultado_binario}")
  
elif escolha == '2':
  numero_binario = input("Digite um número binário fracionário (exemplo: 0.101): ")
  resultado_decimal = binario_fracionario_para_decimal(numero_binario)
  print(f"O número decimal equivalente é: {resultado_decimal}")
else:
  print("Opção inválida. Escolha '1' para converter Decimal para Binário ou '2' para converter Binário para Decimal.")

