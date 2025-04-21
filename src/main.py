from rich import print
from time import sleep
from utils.screen import limpar_tela, aguardar_enter
from utils.constantes import OpcoesMenu
from modules.painel_minimalista import painel_minimalista

## - Mostra os créditos com algumas informções de contato!
def mostrar_creditos():
    """
    Exibe na tela informações de autoria e contato do desenvolvedor,
    além da versão atual do software.

    Esta função limpa a tela antes de apresentar os créditos e
    aguarda que o usuário pressione ENTER para retornar ao menu.
    """
    limpar_tela()
    print("[yellow]Feito por:[/]")
    print("""[red]
 ▄▄▄·  ▄▄▄·      ▄▄▌           • ▌ ▄ ·. ▄ •▄ .▄▄ · 
▐█ ▀█ ▐█ ▄█▪     ██•  ▪        ·██ ▐███▪█▌▄▌▪▐█ ▀. 
▄█▀▀█  ██▀· ▄█▀▄ ██▪   ▄█▀▄    ▐█ ▌▐▌▐█·▐▀▀▄·▄▀▀▀█▄
▐█ ▪▐▌▐█▪·•▐█▌.▐▌▐█▌▐▌▐█▌.▐▌   ██ ██▌▐█▌▐█.█▌▐█▄▪▐█
 ▀  ▀ .▀    ▀█▄▀▪.▀▀▀  ▀█▄▀▪ ▀ ▀▀  █▪▀▀▀·▀  ▀ ▀▀▀▀ 
    [/]""")
    print("\n[yellow]EM CASOS DE DUVIDAS, CONTATE-ME ABAIXO![/]\n")
    print("[black]―-[/]" * 15)
    print(
        "[purple]Discord:[/] [red]'apolo.mk7'[/]\n"
        "[blue]E-mail:[/] [cyan]'masterkey7even@gmail.com'[/]\n"
        "\n[white]Versão: 0.1.0![/]"
    )
    print("[black]―-[/]" * 15)
    aguardar_enter()

## - Exibe as opções do Menu Principal!
def exibir_menu():
    """
    Exibe visualmente o menu principal do programa, listando as
    opções disponíveis para o usuário.

    O menu é formatado usando a biblioteca Rich para uma saída
    visual mais estilizada e intuitiva.
    """
    limpar_tela()
    print("[yellow]========== MENU PRINCIPAL ==========[/]")
    print("[black]―-[/]" * 15)
    print(
        f"[{OpcoesMenu.OPCAO1.value}] - [black]Painel Minimalista[/]\n"
        f"[{OpcoesMenu.OPCAO2.value}] - [purple]Créditos[/]\n"
        f"[{OpcoesMenu.OPCAO0.value}] - [red]Sair![/]"
    )
    print("[black]―-[/]" * 15)

## - Menu Principal!
def main():
    """
    Loop principal do programa que controla o fluxo de interação
    com o usuário.

    Exibe o menu, processa a entrada do usuário e direciona para
    as funções correspondentes, lidando também com entradas inválidas.
    """
    while True:
        limpar_tela()
        exibir_menu()
        try:
            escolha = int(input("Digite uma das opções acima: "))
        except ValueError:
            limpar_tela()
            print(
                "[red]ERRO![/]\n"
                "[red]Você deixou vazio, ou digitou 'letras' ao invés de 'número'. Tente novamente![/]"
            )
            aguardar_enter()
            continue

        if escolha == OpcoesMenu.OPCAO1:
            limpar_tela()
            print("[black]Carregando.....[/]")
            sleep(OpcoesMenu.TEMPO_ESPERA)
            painel_minimalista()
        elif escolha == OpcoesMenu.OPCAO2:
            limpar_tela()
            print("[black]Carregando.....[/]")
            sleep(OpcoesMenu.TEMPO_ESPERA)
            mostrar_creditos()
        elif escolha == OpcoesMenu.OPCAO0:
            limpar_tela()
            print("[red]Saindo.....[/]")
            sleep(OpcoesMenu.TEMPO_ESPERA)
            limpar_tela()
            exit()
        else:
            limpar_tela()
            print(
                "[red]ERRO![/]\n"
                "[red]Você deixou vazio, ou digitou uma opção inválida(inexistente). Tente novamente![/]"
            )
            aguardar_enter()

## - Vai abrir o main.py apenas se for iniciado diretamente!
if __name__ == "__main__":
    main()