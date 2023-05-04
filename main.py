import random

# lista de palavras para o jogo
palavras = ['abacaxi', 'banana', 'melancia', 'laranja', 'limao']

# escolhe uma palavra aleatória da lista
palavra = random.choice(palavras)

# cria uma string com um underline (_) para cada letra da palavra
palavra_secreta = '_' * len(palavra)

# lista de letras erradas
letras_erradas = []

# número de tentativas
tentativas = 6

while True:
    # palavra secreta com as letras já descobertas
    print(palavra_secreta)
    
    # imprime as letras erradas
    print(f'Letras erradas: {letras_erradas}')

    # tentativas restantes
    print(f'Tentativas restantes: {tentativas}')
    
    # pede ao jogador para digitar uma letra
    letra = input('Digite uma letra: ').lower()
    
    # verifica se a letra já foi tentada antes
    if letra in letras_erradas or letra in palavra_secreta:
        print('Você já tentou essa letra antes. Tente outra.')
        continue
    
    # verifica se a letra está na palavra secreta
    if letra in palavra:
        # substitui os underscores (_) pela letra na posição correta
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_secreta = palavra_secreta[:i] + letra + palavra_secreta[i+1:]
        
        # verifica se o jogador ganhou o jogo
        if palavra_secreta == palavra:
            print('Parabéns! Você ganhou o jogo!')
            break
    else:
        # adiciona a letra à lista de letras erradas e diminui o número de tentativas
        letras_erradas.append(letra)

        tentativas -= 1
        
        # verifica se o jogador perdeu o jogo
        if tentativas == 0:
            print('Você perdeu! A palavra era', palavra)
            break
