# Main diagonal = 2
# Secondary diagonal = 3
# Center = 4
# Outer Ring = 0
# Inner Ring = 1

while True:
    try:
        entrada = int(input())
        for i in range(entrada):
            for j in range(entrada):
                # Calcular
                result = 0

                if i == j:
                    result = 2
                
                if (i + j) + 1 == entrada:
                    result = 3

                if i >= int(entrada / 3) and j >= int(entrada / 3) and i < entrada - int(entrada / 3) and j < entrada - int(entrada / 3):
                    result = 1

                if int(entrada % 2) > 0 and i == int(entrada / 2) and j == int(entrada / 2):
                    result = 4
                
                # Imprimir
                print(str(result), end='')
            print()
        print()
    except EOFError:
        break