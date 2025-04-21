import os

## - Limpará a tela do terminal, funciona no Windows e Linux!
def limpar_tela():
    """
    Limpa a tela do terminal de forma compatível com sistemas Windows e Linux.

    Usa o comando 'cls' para Windows e 'clear' para sistemas Unix-like.
    Ideal para manter a interface limpa e organizada durante a execução.
    """
    os.system("cls" if os.name == "nt" else "clear")

## - Pausa o código com input até o usuario pressionar Enter!
def aguardar_enter():
    """
    Pausa a execução do programa até que o usuário pressione Enter.

    Útil para aguardar interação manual antes de prosseguir,
    funcionando como ponto de controle durante a navegação.
    """
    input("\nPressione Enter para continuar...")
