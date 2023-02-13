from visual import visual_dict
import random

def escolhe_palavra_secreta():
    with open("palavras.txt", encoding='utf8') as arquivo:
        txt = arquivo.readlines()
        lista_palavras = [palavra.replace("\n", "").upper() for palavra in txt]
    return random.choice(lista_palavras)


def iniciar_jogo():
    palavra_secreta = escolhe_palavra_secreta()
    letras_palavra_secreta = set(palavra_secreta)
    palpites = set()
    acertos = set()
    tentativas = 7

    while len(letras_palavra_secreta) > 0 and tentativas > 0:

        print("Descubra a palavra secreta!")

        painel = [letra if letra in acertos else "_" for letra in palavra_secreta]
        print(" ".join(painel))

        print(f"Tentativas: {tentativas}")

        if len(palpites) > 0:
            print(f"Letras já escolhidas: {' '.join(palpites)}")

        palpite = input("Escolha uma letra: ").upper()

        if palpite in palpites:
            print("Você já escolheu essa letra antes! Escolha outra!")
        elif palpite in letras_palavra_secreta:
            acertos.add(palpite)
            letras_palavra_secreta.remove(palpite)
        else:
            print(f"A palavra secreta não contém a letra {palpite}!")
            tentativas -= 1
            print(visual_dict[tentativas])

        palpites.add(palpite)

    if tentativas == 0:
        print(f"Você perdeu! A palavra secreta era: {palavra_secreta}!")
    else:
        print(f"Parabéns! Você acertou a palavra secreta: {palavra_secreta}!")

iniciar_jogo()

    