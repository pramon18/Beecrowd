entradas = []

entrada = int(input())

while entrada != 0:
    entradas.append(entrada)
    entrada = int(input())

for entry in entradas:
    result = 1
    # Calcular metade superior a diagonal principal
    # depois transport para a parte inferior da diagonal secundária
    for i in range(entry):
        for j in range(entry):
            # Calcular
            # Metade superior da matriz
            if (i + j <= entry - 1):
                if(min(i,j) == 0):
                    result = 1
                else:
                    result = min(i,j) + 1
            else:
                result = min((entry-1)-j, (entry-1)-i) + 1
            
            # Imprimir
            if j > 0:
                print(' {:>3s}'.format(str(result)), end='')            
            else:
                print('{:>3s}'.format(str(result)), end='')

        print()
    print()