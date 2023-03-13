while True:
    try:
        entrada = int(input())
        print('vai ter copa!') if entrada == 0 else print('vai ter duas!')
    except EOFError:
        break