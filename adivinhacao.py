# Jogo de adivinhação - com níveis de dificuldade e dicas
# sem usar try/except

import random

print("=== Jogo de Adivinhação ===")
print("Escolha o nível de dificuldade:")
print("1 - Fácil   (número de 0 a 10,  6 tentativas)")
print("2 - Médio   (número de 0 a 50,  5 tentativas)")
print("3 - Difícil (número de 0 a 100, 4 tentativas)")

opcao = 0
while opcao not in [1, 2, 3]:
    entrada = input("\nDigite 1, 2 ou 3: ")
    if entrada == "1":
        opcao = 1
    elif entrada == "2":
        opcao = 2
    elif entrada == "3":
        opcao = 3
    else:
        print("Opção inválida. Digite 1, 2 ou 3.")

# Configura as variáveis de acordo com a dificuldade
if opcao == 1:
    sorteio_max = 10
    tentativas_max = 6
    nivel = "Fácil"
elif opcao == 2:
    sorteio_max = 50
    tentativas_max = 5
    nivel = "Médio"
else:
    sorteio_max = 100
    tentativas_max = 4
    nivel = "Difícil"

# Sorteia o número secreto
numero = random.randint(0, sorteio_max)

print("\n" + "="*30)# Jogo de adivinhação - com níveis de dificuldade e dicas
# sem usar try/except

import random

print("=== Jogo de Adivinhação ===")
print("Escolha o nível de dificuldade:")
print("1 - Fácil   (número de 0 a 10,  6 tentativas)")
print("2 - Médio   (número de 0 a 50,  5 tentativas)")
print("3 - Difícil (número de 0 a 100, 4 tentativas)")

opcao = 0
while opcao not in [1, 2, 3]:
    entrada = input("\nDigite 1, 2 ou 3: ")
    if entrada == "1":
        opcao = 1
    elif entrada == "2":
        opcao = 2
    elif entrada == "3":
        opcao = 3
    else:
        print("Opção inválida. Digite 1, 2 ou 3.")

# Configura as variáveis de acordo com a dificuldade
if opcao == 1:
    sorteio_max = 10
    tentativas_max = 6
    nivel = "Fácil"
elif opcao == 2:
    sorteio_max = 50
    tentativas_max = 5
    nivel = "Médio"
else:
    sorteio_max = 100
print(f"Nível: {nivel}")
print(f"Tente adivinhar o número de 0 até {sorteio_max}")
print(f"Você tem {tentativas_max} tentativas")
print("="*30 + "\n")

tentativas = 1
acertou = False

while tentativas <= tentativas_max:
    print(f"Tentativa {tentativas} de {tentativas_max}")
    
    chute = int(input("Seu chute: "))
    
    # verifica se o chute está dentro do intervalo possível
    if chute < 0 or chute > sorteio_max:
        print(f"O número está entre 0 e {sorteio_max}. Tente novamente.")
        continue

    if chute == numero:
        print("\nPARABÉNS! Você acertou!")
        print(f"Você é muito bom mesmo! Acertou em {tentativas} tentativa(s)")
        acertou = True
        break
    
    else:
        print("Errou!")
        
        # Dicas
        if chute < numero:
            print("Dica: o número secreto é MAIOR")
        else:
            print("Dica: o número secreto é MENOR")
        
        print("-" * 25)

    tentativas += 1

# Resultado final
if not acertou:
    print("\nSuas tentativas acabaram...")
    print(f"O número secreto era: {numero}")

print("\n### FIM DO JOGO ###")