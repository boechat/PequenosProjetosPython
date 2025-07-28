import random

aleatorio = random.randint(0, 500)
print('Número aleatório gerado :', aleatorio)  

def jogo(numero, tentativas, aleatorio):
    tentativas += 1

    if numero == aleatorio:
        print('Você acertou!')
        print('Gastou', tentativas, 'tentativas')
        return True, tentativas
    elif numero < aleatorio:
        print('Quase lá! Seu número está baixo!')
    else:
        print('Não! Número está muito alto!')

    return False, tentativas

acertou = False
tentativas = 0

# Primeira Tentativa
numero = int(input('Vamos jogar! Digite o seu chute: '))
acertou, tentativas = jogo(numero, tentativas, aleatorio)

# Loop até acertar ou atingir 10 tentativas
while not acertou and tentativas < 10:
    escolha = input('Deseja tentar novamente? (S/N): ').strip().upper()

    if escolha.upper() == 'S' or escolha.isdigit():
        if escolha.isdigit():
            numero = int(escolha)
        else:
            numero = int(input('Digite seu novo chute: '))
        acertou, tentativas = jogo(numero, tentativas, aleatorio)
    elif escolha == 'N':
        print('Fim de jogo!')
        break
    else:
        print('Opção inválida. Digite S ou N.')

if not acertou:
    print('Você não conseguiu acertar em', tentativas,' tentativas. O número era:', aleatorio)
