def leiaint(n):
    while True:
        try:
            num = int(input(n))
        except(ValueError, TypeError):
            print('\33[31mERRO: Digite apenas numeros inteiros\33[m')
            continue
        except(KeyboardInterrupt):
            print('\nPrograma parou')
            return 0
        else:
            return num


def linha(tam=42):
    return '-' * tam


def head(txt):
    print(linha())
    print(txt.center(42).upper())
    print(linha())


def menu(lista):
    head('menu principal'.upper())
    c = 1
    for item in lista:
        print(f'\33[33m{c}\33[m - \33[34m{item}\33[m')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc
