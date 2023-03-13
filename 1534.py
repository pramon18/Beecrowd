while True:
    try:
        entrada = int(input())
        
        for i in range(entrada):
            for j in range(entrada):
                # Calcular
                # Diagonal principal = 1
                # Diagonal secundária = 2
                # Outros locais = 3
                result = 3

                if (i == j):
                    result = 1
                
                if (i + j) + 1 == entrada:
                    result = 2
                
                # Imprimir
                print(str(result), end='') 
            print()       
    except EOFError:
        break    