print("****************************************")
print("*   Bem vindo ao jogo de advinhação!   *")
print("****************************************")

numero_secreto = 42

chute_usuario_str = input("Digite o seu número: ")
chute_usuario = int(chute_usuario_str)

print("Você digitou ", chute_usuario)

acertou = chute_usuario == numero_secreto
maior = chute_usuario > numero_secreto

if(acertou):
    print("Você acertou!")
else:
    if(maior):
        print("Você errou! O seu chute foi maior que o número secreto!")
    else:
        print("Você errou! O seu chute foi menor que o número secreto!")

print("\nFim do jogo!")
