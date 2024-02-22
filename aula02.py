# https://github.com/shiftkey/desktop/releases/tag/release-3.3.8-linux2
# Fazer a instalação de repositório do GitHub

print("Bem-vindo à Aula de PROGRAMAÇÃO BACK END")
print("Nesta aula02 vamos aprender funcionalidade do GitHub")

# Inicializa uma lista vazia para armazenar as variáveis
ListadeAlunos = []

# Loop para armazenar variáveis
for i in range(20):  # Função de geração de lista
    Nomes = input("Digite o seu Nome {}: ".format(i + 1))
    ListadeAlunos.append(Nomes)  # append Anexa as Variaveis na lista
    if Nomes.lower() == "fim":
        break

# Imprime os nomes dos alunos armazenados, um por linha
print("Lista de Alunos Presentes:")
for aluno in ListadeAlunos:
    print(aluno)
