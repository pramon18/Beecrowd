def countDigit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

entradas = []

entrada = int(input())

while entrada != 0:
    entradas.append(entrada)
    entrada = int(input())

for entry in entradas:
    result = 1
    justify = countDigit(2 ** ((entry-1) * 2))
    
    # Calcular metade superior a diagonal principal
    # depois transport para a parte inferior da diagonal secundária
    for i in range(entry):
        for j in range(entry):
            # Calcular
            # Metade superior da matriz
            # 2^(i+j)
            result = 2 ** (i+j)
            
            # Imprimir
            if j > 0:
                print(' ' + str(result).rjust(justify), end='')            
            else:
                print(str(result).rjust(justify), end='')

        print()
    print()