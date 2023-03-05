entradas = []

entrada = int(input())

while entrada != 0:
    entradas.append(entrada)
    entrada = int(input())

for entry in entradas:
    matrix = [ [0]*entry for i in range(entry)]

    # Calcular metade superior a diagonal principal
    # depois transport para a parte inferior da diagonal secundária
    for i in range(entry):
        for j in range(entry):
            # Metade superior da matriz
            if (i + j <= entry - 1):
                if(min(i,j) == 0):
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = min(i,j) + 1
            else:
                matrix[i][j] = matrix[(entry-1)-j][(entry-1)-i]

    # Imprimir
    for i in range(entry):
        for j in range(entry):
            if j > 0:
                print('   ' + str(matrix[i][j]), end='')            
            else:
                print('  ' + str(matrix[i][j]), end='')
        print()
    print(' ')
    #print(entry)

