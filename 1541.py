entradas = [int(x) for x in input().split()]

while entradas[0] != 0:
    # A, B, C

    x = ((entradas[0] * entradas[1]) * 100) / entradas[2]

    print(int(x**(1/2)))
    entradas = [int(x) for x in input().split()]