def decimal_para_binario(decimal):
    binario = ""
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal = decimal // 2
    return binario if binario != "" else "0"

def binario_para_decimal(binario):
    decimal = 0
    potencia = 0
    for digito in reversed(binario):
        if digito == '1':
            decimal += 2 ** potencia
        potencia += 1
    return decimal

entrada = input("Digite o número a ser convertido e a base (D ou B), separados por um espaço: ")

# Usar a função split() para separar os números e a base
numeros_base = entrada.split()
numero = numeros_base[0]
base = numeros_base[1].upper()

if base == "D":
    decimal = int(numero)
    binario_resultado = decimal_para_binario(decimal)
    print(f"O número decimal {decimal} em binário é: {binario_resultado}")
elif base == "B":
    binario = numero
    decimal_resultado = binario_para_decimal(binario)
    print(f"O número binário {binario} em decimal é: {decimal_resultado}")
else:
    print("Base inválida. Use 'D' para converter Decimal para Binário ou 'B' para converter binário para decimal.")
