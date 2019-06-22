#4 - Escreva uma função mutacoes para computar todas as palavras geradas por uma mutação
#em uma determinada palavra. Uma mutação é definida como inserção de um caractere,
#exclusão de um caractere, substituição de um caractere ou inversão de 2 caracteres
#consecutivos em uma string. Por simplicidade, considere apenas as letras de a a z.
#>>> words = mutate('hello')
#>>> 'helo' in words
#True
#>>> 'cello' in words
#True
#>>> 'helol' in words
#True

def mutate(palavra):
    word = []
    palavra = palavra.lower()
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # Adicionar um caractere
    for i in range(len(palavra)+1):
        for l in letras:
            word.append(palavra[:i] + l + palavra[i:])
    # Tirar um caractere
    for i in range(len(palavra)):
        for l in letras:
            word.append(palavra[:i] + palavra[(i+1):])
    # Exclusão de um caractere
    for i in range(len(palavra)):
        for l in letras:
            word.append(palavra[:i] + palavra[(i+1):])
    print(word)

mutate(input('Diga uma palavra para ser mutada: '))
