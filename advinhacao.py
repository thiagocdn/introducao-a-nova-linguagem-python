print("****************************************")
print("*   Bem vindo ao jogo de advinhação!   *")
print("****************************************")

numero_secreto = 42

chute_usuario_str = input("Digite o seu número: ")
chute_usuario = int(chute_usuario_str)

print("Você digitou ", chute_usuario)

if (chute_usuario == numero_secreto):
    print("Você acertou!")
else:
    print("Você não acetou :(")
