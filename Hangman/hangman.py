#Projeto simples Forca 07/06/2021

import art
import random

#Introdução:
print('\n         BEM VINDO AO JOGO DA FORCA - BOA SORTE !! \n')

#Lista de palavras e escolhendo uma plavra da lista aleatória:
palavras = ['cobra', 'barata', 'sapato', 'brinco', 'taturana', 'zebra', 'chocolate',
              'pokemon', 'dado', 'escola', 'trabalho', 'rua', 'asfalto', 'triste', 'alegre',
              'bravo', 'azul', 'amor', 'vermelhor', 'amarelo', 'violeta', 'zangado', 'vaca', 'tatu',
            'computador', 'escrivaninha', 'saco', 'motocicleta', 'chuteira', 'futebol', 'basket',
            'paralelepipedo', 'ansioso', 'tremendo', 'orgulho']
palavra_escolhida = random.choice(palavras)

#Testando o código:
print(f'A plavra chave é: {palavra_escolhida}')

#Criando blanks:
blanks = []
for letras in palavra_escolhida:
    blanks += '_'

#Iniciando o jogo:
fim_de_jogo = False
vidas = 6

while not fim_de_jogo:
    user_input = input('Escolha uma letra: ').lower()

    #Lógica de escolha de letras
    if user_input in blanks:
        print('\nVocê já escolheu essa letra, escolha uma outra !\n')
    else:
        #Verificação da letra escolhida com a plavra escolhida.
        for posicao in range(len(palavra_escolhida)):
            if palavra_escolhida[posicao] == user_input:
                blanks[posicao] = user_input

        #Checando se usuário está escolheu errado:
        if user_input not in palavra_escolhida:
            vidas -= 1
            print('A palavra não possui essa letra\n')
            if vidas == 0:
                fim_de_jogo = True
                print('\nQUE PENA, você perdeu, tente outra vez !')

        #Juntando as letras para se tornar uma string.
        print(f"{' '.join(blanks)}")

        #Checando para ver se ainda existe "_" em blanks.
        if "_" not in blanks:
            fim_de_jogo = True
            print('\nPARABÉNS, você acertou todas as letras !!')

        #Mostrando a arte:
        print(art.stages[vidas])