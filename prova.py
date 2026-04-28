# COPIE E COLE ESTE ENUNCIADO NO TERMINAL EM UM ARQUIVO .py. Para executar no terminal use "python3 nome_arquivo.py"
# Use somente o Classroom e o GitHub. Uso do Google ou qualquer tipo de IA = zero!
# 1) (0,5 p) Crie variáveis para armazenar seu nome, nota da prova escrita, série e turma. Após isso, mostre no terminal uma mensagem personalizada se apresentando.
nome = "agnes"
nota_prova = 1
serie = 3
turma = "DSB"
print("ola meu nome é", nome, "minha nota na prova foi", nota_prova, "minha serie é", serie, "e minha turma é", turma, ".")

# 2) (0,5 p) Crie uma lista com 3 atividades que você gosta de fazer no final de semana.
atividades = ["conversar", "jogar", "caminhar"]
def exibir_atividades():
    print("atividades:")
    for atividade in atividades:
        print(atividades)

exibir_atividades()

# 3) (1,0 p) Crie uma condição que verifica se sua nota da prova é maior que a média 1,8.
if nota_prova > 1.8: 
    print("sua nota é maior que 1.8")
else:
    print("sua nota é menor que 1.8")

# 4) (1,0 p) Crie uma função mostra no terminal a quantidade de litros de água que devem ser consumidos diariamente por uma pessoa. Depois execute a função colocando um peso como parâmetro.
# Para calcular, siga a fórmula: qtd_litros = 0,035 * peso.
def qtd_litros(peso):
    qtd_litros = 0.035 * peso
    print("Você deve beber", qtd_litros, "litros.")

qtd_litros(50)
# 5) (1,0 p) Crie um código que verifica se "estudar" existe na lista criada da questão 2. Use o laço de repetição que preferir.
for atividade in atividades:
    if (atividade == "Estudar"):
        print("estudar esta na lista")
    else:
        print("estudar nao esta na lista")

# 6) (1,0 p) Crie um laço de repetição que conta de 1 a 128, mas ao invés de somar 1 no contador, multiplique-o por 2.
numero = 1 
while (numero<=250):
    print(numero)
    numero = numero * 2