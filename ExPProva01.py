#1 - A série de Fibonacci é definida pela expressão seguinte:

# 0 if n = 0
# 1 if n = 1
# F(n - 1) + F(n-2)

#Defina uma função serie_fibonacci que recebe um número inteiro n maior ou igual a 2 e
#devolve a lista com os n primeiros elementos da série de fibonacci. A sua função deve testar se
#o seu argumento é um inteiro maior ou igual a 2.
#>>> serie_fibonnaci(10)
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]#
x = int(input(''))


def serie_fibonacci():
    lista_fibonnaci = [0, 1]
    j = len(lista_fibonnaci)
    i = 2
    while j < x:
        lista_fibonnaci.append(lista_fibonnaci[i - 1] + lista_fibonnaci[i - 2])
        i += 1
        j += 1
    print(lista_fibonnaci)



while x < 2:
    print('Diga um número maior que 2! ')
    break
while x >= 2:
    serie_fibonacci()
    break