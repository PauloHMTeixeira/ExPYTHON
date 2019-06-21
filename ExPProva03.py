#3 - Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta
#função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor
#mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem
#ser modificados para valores dentro da faixa de forma elegante.
def retangulo():
    print('+' + ('-' * x) + '+')
    for i in range(y):
        print('|' + (' ' * x) + '|')
    print('+' + ('-' * x) + '+')



x = int(input('Qual o tamanho do comprimento? '))
y = int(input('Qual o tamanho da altura? '))
retangulo()
