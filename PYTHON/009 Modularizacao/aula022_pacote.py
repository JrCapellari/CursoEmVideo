from uteis_pacote import numeros


num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print(f'{num}! = {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')
