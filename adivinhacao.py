# importação da biblioteca
import random

def mostrar_forca(erros):
    """Mostra o desenho da forca de acordo com o número de erros"""
    if erros == 0:
        print("   _______")
        print("   |     |")
        print("         |")
        print("         |")
        print("         |")
        print("         |")
        print("_________|_")
    elif erros == 1:
        print("   _______")
        print("   |     |")
        print("   O     |")
        print("         |")
        print("         |")
        print("         |")
        print("_________|_")
    elif erros == 2:
        print("   _______")
        print("   |     |")
        print("   O     |")
        print("   |     |")
        print("         |")
        print("         |")
        print("_________|_")
    elif erros == 3:
        print("   _______")
        print("   |     |")
        print("   O     |")
        print("  /|     |")
        print("         |")
        print("         |")
        print("_________|_")
    elif erros == 4:
        print("   _______")
        print("   |     |")
        print("   O     |")
        print("  /|\\    |")
        print("         |")
        print("         |")
        print("_________|_")
    elif erros == 5:
        print("   _______")
        print("   |     |")
        print("   O     |")
        print("  /|\\    |")
        print("  /      |")
        print("         |")
        print("_________|_")
    elif erros == 6:
        print("   _______")
        print("   |     |")
        print("   O     |")
        print("  /|\\    |")
        print("  / \\    |")
        print("         |")
        print("_________|_")

def jogar_adivinhacao():
    """Jogo de adivinhação de números"""
    print("\n" + "="*50)
    print("BEM-VINDO AO JOGO DA ADIVINHAÇÃO!")
    print("="*50)
   
    # Configurações do jogo
    tentativas = 1
    errou = True
    sorteio_max = 10
    tentativas_max = 3
    numero = random.randint(0, sorteio_max)
   
    print(f"\nTente adivinhar o número entre 0 e {sorteio_max}!")
    print(f"Você tem {tentativas_max} tentativas.\n")
   
    while tentativas <= tentativas_max:
        print("Tentativa:", tentativas)
        try:
            chute = int(input("Digite o seu chute (0 a 10): "))
           
            if chute < 0 or chute > 10:
                print("Por favor, digite um número entre 0 e 10!")
                continue
               
            if chute == numero:
                print("\nParabéns, você é o bonzão mesmo!")
                errou = False
                break
            else:
                if chute < numero:
                    print("Dica: O número é MAIOR!")
                else:
                    print("Dica: O número é MENOR!")
                print("Errou :c\n")
        except ValueError:
            print("Digite um número válido!\n")
            continue
           
        tentativas = tentativas + 1
   
    if errou == True:
        print(f"\nO número sorteado era: {numero}")  # mostra p quem errou
    print("### FIM DO JOGO ###\n")

def carregar_palavras_por_tema():
    """Menu para escolher tema e carregar palavras"""
    print("\n" + "="*50)
    print("ESCOLHA O TEMA DO JOGO")
    print("="*50)
    print("1 - cores")
    print("2 - instrumentos")
    print("3 - artes")
   
    while True:
        try:
            opcao = int(input("\nDigite o número do tema desejado: "))
           
            if opcao == 1:
                arquivo = "cores.txt"
                tema = "cores"
                break
            elif opcao == 2:
                arquivo = "instrumentos.txt"
                tema = "instrumentos"
                break
            elif opcao == 3:
                arquivo = "artes.txt"
                tema = "artes"
                break
            else:
                print("Opção inválida! Escolha 1, 2 ou 3.")
        except ValueError:
            print("Digite um número válido!")
   
    try:
        with open(arquivo, "r", encoding="utf-8") as file:
            palavras = [linha.strip().upper() for linha in file.readlines() if linha.strip()]
       
        if not palavras:
            print(f"O arquivo {arquivo} está vazio!")
            return None, None
           
        print(f"\nTema escolhido: {tema}")
        print(f"Total de palavras disponíveis: {len(palavras)}")
        return palavras, tema
       
    except FileNotFoundError:
        print(f"\nArquivo {arquivo} não encontrado!")
        print("Certifique-se de que o arquivo está na mesma pasta do programa.")
        return None, None

def jogar_forca():
    """Jogo da forca com tema escolhido pelo usuário"""
    print("\n" + "="*50)
    print("BEM-VINDO AO JOGO DA FORCA!")
    print("="*50)
   
    # Carrega as palavras do tema escolhido
    palavras, tema = carregar_palavras_por_tema()
   
    if not palavras:
        print("\nNão foi possível carregar as palavras. Voltando ao menu principal...")
        return
   
    # Sorteia uma palavra
    palavra = random.choice(palavras)
   
    # Configurações do jogo
    letras_acertadas = []
    for letra in palavra:
        letras_acertadas.append("_")
   
    acertou = False
    enforcou = False
    limite_tentativas = len(palavra) + 6
    erros = 0  # CONTROLE SOMENTE DOS ERROS
    letras_erradas = []
   
    def mostrar_letras_acertadas():
        for letra in letras_acertadas:
            print(letra, end=" ")
   
    print(f"\nTente adivinhar a palavra secreta!")
    print(f"Tema: {tema}")
    print(f"Dica: A palavra tem {len(palavra)} letras\n")
   
    while not acertou and not enforcou:
        # Mostrar o desenho da forca
        mostrar_forca(erros)
       
        # Mostrar o estado atual do jogo
        print("\nPalavra: ", end="")
        mostrar_letras_acertadas()
       
        if letras_erradas:
            print(f"\nLetras erradas: {', '.join(letras_erradas)}")
        else:
            print("\nLetras erradas: nenhuma")
       
        print(f"Erros: {erros}/{limite_tentativas}")
       
        # Receber o chute do usuário
        chute = input("\nDigite uma letra: ").strip().upper()
       
        # Validação do chute
        if len(chute) != 1 or not chute.isalpha():
            print("Por favor, digite apenas uma letra!")
            continue
       
        # Verifica se a letra já foi tentada
        if chute in letras_acertadas or chute in letras_erradas:
            print("Você já tentou esta letra!")
            continue
       
        # Verifica se o chute está na palavra
        acertou_letra = False
        indice = 0
        for letra in palavra:
            if chute == letra:
                letras_acertadas[indice] = letra
                acertou_letra = True
            indice = indice + 1
       
        if acertou_letra:
            print(f"\n✅ Boa! A letra '{chute}' existe na palavra!")
        else:
            print(f"\n❌ A letra '{chute}' não está na palavra!")
            letras_erradas.append(chute)
            # CORREÇÃO: Só incrementa os erros quando o usuário erra a letra
            erros = erros + 1
       
        # Verifica se o jogador se enforcou
        if erros >= limite_tentativas:
            print("\n" + "="*50)
            mostrar_forca(erros)
            print("\nVocê perdeu :(")
            print(f"A palavra era: {palavra}")
            enforcou = True
       
        # Verifica se o jogador acertou
        if letras_acertadas.count("_") == 0:
            print("\n" + "="*50)
            mostrar_forca(erros)
            print("\nParabéns, você acertou a palavra secreta!")
            print("Palavra: ", end="")
            mostrar_letras_acertadas()
            print()
            acertou = True
   
    print("\n### FIM DO JOGO DA FORCA ###\n")

def main():
    """Menu principal com laço infinito"""
    while True:
        print("="*50)
        print("MENU PRINCIPAL")
        print("="*50)
        print("1 - Jogo da Forca")
        print("2 - Jogo da Adivinhação")
        print("3 - Sair do Jogo")
        print("="*50)
       
        try:
            opcao = int(input("\nEscolha uma opção: "))
           
            if opcao == 1:
                jogar_forca()
            elif opcao == 2:
                jogar_adivinhacao()
            elif opcao == 3:
                print("\nObrigado por jogar! Até mais!")
                break
            else:
                print("\nOpção inválida! Escolha 1, 2 ou 3.")
        except ValueError:
            print("\nPor favor, digite um número válido!")
       
        # Aguarda o usuário pressionar ENTER para continuar
        input("\nPressione ENTER para voltar ao menu principal...")

# Executa o programa
if __name__ == "__main__":
    main()