#Os alunos de uma turma foram muito mal em uma prova. O professor resolveu, então
#considerar a maior nota como o 10.0 e transformar as demais notas em relação a esta nota da
#seguinte maneira:

#nota do aluno * 10/ maior nota

#Faça uma função que receba a lista de notas dos alunos, calcule a nova nota dos alunos
#mostrando as notas antigas e as novas na tela.
#Exemplo:
#Notas originais: 3.0 4.0 5.0 6.0 3.0
#Maior nota: 6.0
#Saída:
#1 3.0 5.0 (3*10)/6
#2 4.0 6.6
#3 5.0 8.3
#4 6.0 10.0
#5 3.0 5.0

lista = []
lista2 = []
while True:
    x = float(input('Diga a nota dos alunos: (Digite 11 para parar) '))
    lista.append(x)
    if x > 10:
        lista.remove(11)
        break
def nota_nova():
    alta = max(lista)
    i = 0
    while i < len(lista):
        lista2.append((lista[i] * 10) / alta)
        i += 1
    print(lista2)
nota_nova()
