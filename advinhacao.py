print("****************************************")
print("*   Bem vindo ao jogo de advinhação!   *")
print("****************************************")

numero_secreto = 42
numero_total_tentativas = 3
rodada = 1


while rodada <= numero_total_tentativas:
    print("Tentativa {} de {}".format(rodada, numero_total_tentativas))
    chute_usuario_str = input("Digite o seu número: ")
    chute_usuario = int(chute_usuario_str)

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

    rodada += 1


print("\nFim do jogo!")
