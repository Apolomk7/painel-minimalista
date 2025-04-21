from rich import print
from time import sleep
from utils.screen import limpar_tela, aguardar_enter
from utils.constantes import OpcoesArquivos
from utils.organizador import *
from utils.organizador2 import *

def exibir_menu():
    """
    Exibe o menu do Organizador de Arquivos.

    Este menu permite ao usuário escolher entre organizar arquivos
    por tipo, organizar por data, ou retornar ao menu anterior.
    As opções são estilizadas com a biblioteca Rich para melhor visualização.
    """
    limpar_tela()
    print("[yellow]========== ORGANIZADOR DE ARQUIVOS ==========[/]")
    print("[black]―-[/]" * 15)
    print(
        f"{[OpcoesArquivos.OPCAO1.value]} - [black]Organizar por tipo de arquivo[/]\n"
        f"{[OpcoesArquivos.OPCAO2.value]} - [black]Organizar por data[/]\n"
        f"{[OpcoesArquivos.OPCAO3.value]} - [purple]Voltar![/]"
    )
    print("[black]―-[/]" * 15)

def organizador_arquivos():
    """
    Controla o fluxo de organização de arquivos baseado nas opções do usuário.

    - Permite organizar arquivos por tipo ou por data.
    - Realiza validações de diretório antes de aplicar as operações.
    - Apresenta mensagens informativas e tratativas de erro
      para entradas inválidas.
    """
    while True:
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

        if escolha == OpcoesArquivos.OPCAO1:
            limpar_tela()
            diretorio1 = input("Digite o caminho do diretório: ").strip()
            if not os.path.isdir(diretorio1):
                limpar_tela()
                print(
                    "[red]ERRO![/]\n"
                    "[red]Diretório inválido!"
                )
                aguardar_enter()
                continue
            print("[yellow]Organizando Arquivos...[/]")
            sleep(OpcoesArquivos.TEMPO_ESPERA)
            organizar_arquivos(diretorio1)
            print("[green]Arquivos Organizados![/]")
            aguardar_enter()
        elif escolha == OpcoesArquivos.OPCAO2:
            limpar_tela()
            diretorio2 = input("Digite o caminho do diretorio: ").strip()
            if not os.path.isdir(diretorio2):
                limpar_tela()
                print(
                    "[red]ERRO![/]\n"
                    "[red]Diretório inválido!"
                )
                aguardar_enter()
                continue
            print("[yellow]Organizando Arquivos...[/]")
            sleep(OpcoesArquivos.TEMPO_ESPERA)
            organizar_por_data(diretorio2)
        elif escolha == OpcoesArquivos.OPCAO3:
            limpar_tela()
            print("[black]Voltando.....[/]")
            sleep(OpcoesArquivos.TEMPO_ESPERA)
            break
        else:
            limpar_tela()
            print(
                "[red]ERRO![/]\n"
                "[red]Você deixou vazio, ou digitou uma opção inválida(inexistente). Tente novamente![/]"
            )
            aguardar_enter()