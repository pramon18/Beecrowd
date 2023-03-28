# Main diagonal = 2
# Secondary diagonal = 3
# Center = 4
# Outer Ring = 0
# Inner Ring = 1

entradas = []

entrada = int(input())

while entrada != 0:
    entradas.append(entrada)
    entrada = int(input())

for entry in entradas:
    for i in range(entry):
        for j in range(entry):
            # Calcular
            result = 0

            if i == j:
                result = 2
            
            if (i + j) + 1 == entry:
                result = 3

            if int(entry%2) > 0 and i == int(entry/2) and j == int(entry/2):
                result = 4
            
            # Imprimir
            print(str(result), end='')
        print()
    print()