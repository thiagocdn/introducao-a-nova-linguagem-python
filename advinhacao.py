import random

print("****************************************")
print("*   Bem vindo ao jogo de advinhação!   *")
print("****************************************")

numero_secreto = random.randrange(1, 101)
numero_total_tentativas = 20


for rodada in range(1, numero_total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, numero_total_tentativas))
    chute_usuario_str = input("Digite um número entre 1 e 100: ")
    chute_usuario = int(chute_usuario_str)

    if(chute_usuario < 1 or chute_usuario > 100):
        print("Você deve escolher um número entre 1 e 100")
        continue

    acertou = chute_usuario == numero_secreto
    maior = chute_usuario > numero_secreto

    if(acertou):
        print("Você acertou em", rodada, "tentativa(s)")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto!")
        else:
            print("Você errou! O seu chute foi menor que o número secreto!")


print("\nFim do jogo!")
