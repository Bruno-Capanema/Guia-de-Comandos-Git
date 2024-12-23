# Lista de comandos do Git para iniciantes e suas descrições
comandos_git = {
    "git init": "Inicializa um novo repositório Git no diretório atual.",
    "git clone": "Clona um repositório existente de um servidor remoto.",
    "git status": "Exibe o estado atual do repositório (arquivos modificados, não rastreados, etc.).",
    "git add": "Adiciona arquivos ao índice (stage), preparando-os para o commit.",
    "git commit": "Registra as mudanças adicionadas com uma mensagem de commit.",
    "git push": "Envia os commits locais para o repositório remoto.",
    "git pull": "Atualiza o repositório local com mudanças do remoto.",
    "git branch": "Gerencia ramos (branches) no repositório.",
    "git checkout": "Alterna entre branches ou restaura arquivos no repositório.",
    "git merge": "Funde um branch com o branch atual.",
    "git log": "Mostra o histórico de commits do repositório.",
    "git remote": "Gerencia conexões com repositórios remotos.",
    "git diff": "Mostra diferenças entre arquivos e commits.",
    "git reset": "Reverte mudanças no índice ou no repositório.",
    "git rm": "Remove arquivos do índice e do repositório."
}

# Apresentação inicial
print("Bem-vindo ao Guia de Comandos Git!")
print("Digite o número correspondente ao comando que deseja saber mais ou 'sair' para encerrar.\n")

# Loop principal
while True:
    # Exibe a lista de comandos com índice para escolha
    print("Comandos disponíveis:")
    for i, comando in enumerate(comandos_git.keys(), start=1):
        print(f"{i}. {comando}")
    
    # Recebe a entrada do usuário
    escolha = input("\nEscolha um número ou digite 'sair': ").strip()
    
    # Verifica se o usuário quer sair
    if escolha.lower() == "sair":
        print("Obrigado por usar o Guia de Comandos Git! Até mais!")
        break

    # Verifica se a entrada é válida
    if escolha.isdigit():
        indice = int(escolha) - 1
        if 0 <= indice < len(comandos_git):
            comando_selecionado = list(comandos_git.keys())[indice]
            print(f"\n{comando_selecionado}: {comandos_git[comando_selecionado]}\n")
        else:
            print("Número inválido! Tente novamente.\n")
    else:
        print("Entrada inválida! Digite um número ou 'sair'.\n")
