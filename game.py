import random

vocabulario = ['caneta', 'lapis', 'cadeira', 'copo', 'sofa', 'mesa', 'xicara', 'colher', 'computador', 'oculos', 'celular', 'travesseiro', 'sapato', 'borracha', 'livro', 'escova', 'pente', 'jarro', 'faca', 'garfo', 'prato', 'panela', 'televisao', 'caderno', 'batom', 'boneca', 'bola', 'cama', 'luminaria', 'anel', 'abacate', 'cereja', 'morango', 'banana', 'pera', 'uva', 'pinha', 'tangerina', 'melancia', 'umbu', 'mamao', 'laranja', 'guarana', 'limão', 'maracuja', 'goiaba', 'caju', 'roma', 'jaca', 'damasco', 'framboesa', 'kiwi', 'lima', 'melao', 'pitanga', 'groselia', 'acerola', 'figo', 'pitanga', 'manga', 'cachorro', 'gato', 'foca', 'morsa', 'hiena', 'baleia', 'golfinho', 'tigre', 'guepardo', 'leopardo', 'onça', 'lince', 'jaguatirica', 'ariranha', 'lontra', 'quati', 'cobra', 'marsupiais', 'lula', 'caracol', 'gaivota', 'jiboia', 'sucuri', 'sapo', 'rã', 'aranha']
animais = ['cachorro', 'gato', 'foca', 'morsa', 'hiena', 'baleia', 'golfinho', 'tigre', 'guepardo', 'leopardo', 'onça', 'lince', 'jaguatirica', 'ariranha', 'lontra', 'quati', 'cobra', 'marsupiais', 'lula', 'caracol', 'gaivota', 'jiboia', 'sucuri', 'sapo', 'rã', 'aranha']
frutas = ['abacate', 'cereja', 'morango', 'banana', 'pera', 'uva', 'pinha', 'tangerina', 'melancia', 'umbu', 'mamao', 'laranja', 'guarana', 'limão', 'maracuja', 'goiaba', 'caju', 'roma', 'jaca', 'damasco', 'framboesa', 'kiwi', 'lima']
objetos = ['caneta', 'lapis', 'cadeira', 'copo', 'sofa', 'mesa', 'xicara', 'colher', 'computador', 'oculos', 'celular', 'travesseiro', 'sapato', 'borracha', 'livro', 'escova', 'pente', 'jarro', 'faca', 'garfo', 'prato', 'panela', 'televisao', 'caderno', 'batom', 'boneca', 'bola', 'cama', 'luminaria', 'anel']
restart_config = ['s', 'n']
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
palavras_sorteada = []
tentativas = []
resposta = []
chances = 7
vit1 = 0
der1 = 0
vit2 = 0
der2 = 0
multiplayer = 0
def bemvindo():    
    print("*")
    print("Bem vindo ao jogo da Forca!")
    print("*")
bemvindo()

def carrega_palavra1():
    palavra_secreta = random.choice(vocabulario)
    palavras_sorteada.append(palavra_secreta)
    return palavra_secreta
def carrega_palavra2():
    palavra_secreta = random.choice(animais)
    palavras_sorteada.append(palavra_secreta)
    return palavra_secreta
def carrega_palavra3():
    palavra_secreta = random.choice(frutas)
    palavras_sorteada.append(palavra_secreta)
    return palavra_secreta
def carrega_palavra4():
    palavra_secreta = random.choice(objetos)
    palavras_sorteada.append(palavra_secreta)
    return palavra_secreta
def victory():
    print("Você venceu o jogo, parabéns")
    print("       _      ")
    print("      '.=====.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         .' '.        ")
    print("        '-------'       ")
    
def lost():
    print("Suas chances acabaram, você perdeu!")
    print("A palavra era {}".format(palavra))
    print("    _         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \___/           ")

multi = str(input('Para jogar multiplayer digite:\nS para sim\nN para sou um pouco antisocial então não\n')).lower()
if multi == 's':
    pass
elif multi == 'n':
    pass
else:
    multi = str(input('Para jogar multiplayer digite:\nS para sim\nN para sou um pouco antisocial então não\n')).lower()
tema = int(input('Qual será o tema do jogo? Digite:\n1 para aleatório\n2 para animais\n3 para frutas\n4 para objetos.\n'))
restart = 0

while True:
    if tema == 1:
        if restart == 0:
            carrega_palavra1()
            del tentativas[:]
            chances = 7
            restart += 1      
            palavra = palavras_sorteada[0]
            resposta = list(palavra)
            palavras_sorteada.pop(0)
    elif tema == 2:
        if restart == 0:
            carrega_palavra2()
            del tentativas[:]
            chances = 7
            restart += 1      
            palavra = palavras_sorteada[0]
            resposta = list(palavra)
            palavras_sorteada.pop(0)
    elif tema == 3:
        if restart == 0:
            carrega_palavra3()
            del tentativas[:]
            chances = 7
            restart += 1      
            palavra = palavras_sorteada[0]
            resposta = list(palavra)
            palavras_sorteada.pop(0)
    if tema == 4:
        if restart == 0:
            carrega_palavra4()
            del tentativas[:]
            chances = 7
            restart += 1      
            palavra = palavras_sorteada[0]
            resposta = list(palavra)
            palavras_sorteada.pop(0)
        
    print('Tentativas:', tentativas)
    print('Chances:', chances)
       
    for letras in palavra:
        if letras in tentativas:
            print(letras, end=' ')
        else:
            print('_', end=' ')
            
    
    def desenha_forca():
        print("  _     ")
        print(" |/      |    ")
        if(chances == 6):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if(chances == 5):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if(chances == 4):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if(chances == 3):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if(chances == 2):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if(chances == 1):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")
 
        if (chances == 0):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

            print(" |            ")
            print("|__         ")
            print()
    
    if multi == 'n':
        print('\nVocê está com {0} vitórias e {1} derrotas'.format(vit1, der1))
    if multi == 's':
        print('\nO jogador 1 está com {0} vitórias e {1} derrotas\nO jogador 2 está com {2} vitórias e {3} derrotas'.format(vit1, der1, vit2, der2))
    chute = str(input('\nDigite uma letra ou escreva "SAIR" para sair do jogo\n')).lower()
    if chute == 'sair':
        break
        vit = 0
        der = 0
    elif chute not in alfabeto:
        print("Parece que você não sabe o que UMA letra é, tente de novo\n")
    while chute not in alfabeto or len(chute) > 1:
        chute = str(input('\nDigite uma letra ou escreva "SAIR" para sair do jogo\n')).lower()
        if chute == 'sair':
            vit = 0
            der = 0
            break
    if chute in tentativas:
        print("Você já chutou essa letra, o alzheimer ta forte\n")
    elif chute in palavra:
        print("Parabéns, essa letra aparece na palavra secreta\n")
        tentativas.append(chute)
    else:
        print("Essa letra não faz parte da palavra secreta\n")
        chances -= 1
        desenha_forca()
        tentativas.append(chute)  
    if len(tentativas) == 6:
        palpite = str(input('Quer chutar a palavra? isso é um ultimato\nS para sim\nN para não\n')).lower()
        if palpite == 's':
            palpite_true = str(input('Chute a palavra:\n'))
            if palpite_true == palavra:
                victory()
                if multi == 'n':
                    vit1 += 1
                elif multi == 's':
                    multiplayer = str(input('Esta é a rodada do jogador 1 ou jogador 2? Digite:\n1 para jogador 1\n2 para jogador 2\n'))
                    if multiplayer == '1':
                        vit1 +=1
                    if multiplayer == '2':
                        vit2 +=1
                loop = str(input('Quer jogar de novo? Digite:\nS para sim\nN para não\n')).lower()
                while loop not in restart_config:
                    loop = str(input('Eu não sei ler mentes! Digite:\nS para sim\nN para não\n')).lower()
                    if loop == 's':
                        restart = 0     
                    elif loop == 'n':
                        if multi == 'n':
                            print('\nVocê está com {0} vitórias e {1} derrotas'.format(vit1, der1))
                        elif multi == 's':
                            print('\nO jogador 1 terminou o jogo com {0} vitórias e {1} derrotas\nO jogador 2 terminou o jogo com {2} vitórias e {3} derrotas'.format(vit1, der1, vit2, der2))
                            if vit1 > vit2 or der1 < der2:
                                print('O jogador 1 venceu o jogador 2')
                            else:
                                print('O jogador 2 venceu o jogador 1')
                                vit1 = 0
                                der1 = 0
                                vit2 = 0
                                der2 = 0
                                break
            else:
                print('Eu te dei a chance, você errou e será penalizado\n')
                chances -= 1
        if palpite == 'n':
            print('Então tá, boa sorte')
            pass
    if chances == 0:
        lost()
        if multi == 'n':
            der1 += 1
        elif multi == 's':
            multiplayer = str(input('Esta é a rodada do jogador 1 ou jogador 2? Digite:\n1 para jogador 1\n2 para jogador 2\n'))
            if multiplayer == '1':
                der1 +=1
            if multiplayer == '2':
                der2 +=1
        loop = str(input('Quer jogar de novo? Digite:\nS para sim\nN para não\n')).lower()
        while loop not in restart_config:
            loop = str(input('Eu não sei ler mentes! Digite:\nS para sim\nN para não\n')).lower()
        if loop == 's':
            restart = 0     
        elif loop == 'n':
            if multi == 'n':
                print('\nVocê está com {0} vitórias e {1} derrotas'.format(vit1, der1))
            elif multi == 's':
                print('\nO jogador 1 terminou o jogo com {0} vitórias e {1} derrotas\nO jogador 2 terminou o jogo com {2} vitórias e {3} derrotas'.format(vit1, der1, vit2, der2))
                if vit1 > vit2 or der1 < der2:
                    print('O jogador 1 venceu o jogador 2')
                else:
                    print('O jogador 2 venceu o jogador 1')
                vit1 = 0
                der1 = 0
                vit2 = 0
                der2 = 0
                break
    elif set(palavra).issubset(set(tentativas)):
        victory()
        if multi == 'n':
            vit1 += 1
        elif multi == 's':
            multiplayer = str(input('Esta é a rodada do jogador 1 ou jogador 2? Digite:\n1 para jogador 1\n2 para jogador 2\n'))
            if multiplayer == '1':
                vit1 +=1
            if multiplayer == '2':
                vit2 +=1
        loop = str(input('Quer jogar de novo? Digite:\nS para sim\nN para não\n')).lower()
        while loop not in restart_config:
            loop = str(input('Eu não sei ler mentes! Digite:\nS para sim\nN para não\n')).lower()
        if loop == 's':
            restart = 0     
        elif loop == 'n':
            if multi == 'n':
                print('\nVocê está com {0} vitórias e {1} derrotas'.format(vit1, der1))
            elif multi == 's':
                print('\nO jogador 1 terminou o jogo com {0} vitórias e {1} derrotas\nO jogador 2 terminou o jogo com {2} vitórias e {3} derrotas'.format(vit1, der1, vit2, der2))
                if vit1 > vit2 or der1 < der2:
                    print('O jogador 1 venceu o jogador 2')
                else:
                    print('O jogador 2 venceu o jogador 1')
                vit1 = 0
                der1 = 0
                vit2 = 0
                der2 = 0
                break
