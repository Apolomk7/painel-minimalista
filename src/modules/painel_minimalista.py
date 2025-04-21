from rich import print
from time import sleep
from utils.screen import limpar_tela, aguardar_enter
from utils.constantes import OpcoesPainel
from modules.conversor_moedas import conversor_moedas
from modules.gerador_senhas import gerador_senhas
from modules.organizador_arquivos import organizador_arquivos

def exibir_menu():
    """
    Exibe o menu principal do Painel Minimalista, listando as
    ferramentas disponíveis para o usuário.

    O menu inclui opções de conversão de moedas, geração de senhas,
    organização de arquivos, retorno ao menu anterior e saída do sistema.
    Utiliza a biblioteca Rich para exibição visual aprimorada.
    """
    limpar_tela()
    print("[yellow]========== PAINEL MINIMALISTA ==========[/]")
    print("[black]―-[/]" * 15)
    print(
        f"[{OpcoesPainel.OPCAO1.value}] - [black]Conversor de Moedas[/]\n"
        f"[{OpcoesPainel.OPCAO2.value}] - [black]Gerador de Senhas[/]\n"
        f"[{OpcoesPainel.OPCAO3.value}] - [black]Organizador de Arquivos[/]\n"
        f"[{OpcoesPainel.OPCAO4.value}] - [purple]Voltar ao Menu Principal![/]\n"
        f"[{OpcoesPainel.OPCAO0.value}] - [red]Sair![/]"
    )
    print("[black]―-[/]" * 15)

def painel_minimalista():
    """
    Controla o fluxo de interação com o usuário dentro do Painel Minimalista.

    Exibe o menu e aguarda a escolha do usuário, redirecionando para as
    ferramentas específicas de acordo com a opção selecionada.
    Implementa também tratamento de exceções para entradas inválidas.
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

        if escolha == OpcoesPainel.OPCAO1:
            limpar_tela()
            print("[black]Carregando.....[/]")
            sleep(OpcoesPainel.TEMPO_ESPERA)
            conversor_moedas()
        elif escolha == OpcoesPainel.OPCAO2:
            limpar_tela()
            print("[black]Carregando.....[/]")
            sleep(OpcoesPainel.TEMPO_ESPERA)
            gerador_senhas()
        elif escolha == OpcoesPainel.OPCAO3:
            limpar_tela()
            print("[black]Carregando.....[/]")
            sleep(OpcoesPainel.TEMPO_ESPERA)
            organizador_arquivos()
        elif escolha == OpcoesPainel.OPCAO4:
            limpar_tela()
            print("[black]Voltando.....[/]")
            sleep(OpcoesPainel.TEMPO_ESPERA)
            break
        elif escolha == OpcoesPainel.OPCAO0:
            limpar_tela()
            print("[red]Saindo.....[/]")
            sleep(OpcoesPainel.TEMPO_ESPERA)
            limpar_tela()
            exit()
        else:
            limpar_tela()
            print(
                "[red]ERRO![/]\n"
                "[red]Você deixou vazio, ou digitou uma opção inválida(inexistente). Tente novamente![/]"
            )
            aguardar_enter()