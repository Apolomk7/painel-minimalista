import requests
from datetime import datetime
from time import sleep
from rich import print
from utils.screen import limpar_tela, aguardar_enter
from utils.constantes import OpcoesConversor

def BTCBRL():
    """
    Converte valores de Bitcoin (BTC) para Reais Brasileiros (BRL).
    Obtém a cotação em tempo real através da API AwesomeAPI.
    """
    link = "https://economia.awesomeapi.com.br/json/last/BTC-BRL"
    pegar = requests.get(link)
    resultado = pegar.json()
    formatado = float(resultado["BTCBRL"]["bid"])
    data_api = resultado["BTCBRL"]["create_date"]
    data_objeto = datetime.strptime(data_api, "%Y-%m-%d %H:%M:%S")
    data_br = data_objeto.strftime("%d/%m/%Y %H:%M:%S")

    while True:
        limpar_tela()
        print("[black]Você selecionou converter [green]Bitcoin(BTC)[/] para [green]Reais Brasileiros(R$)[/][/]\n")
        print(
            f"\n[yellow]Cotação:[/] [black]Atualmente [green]1 Bitcoin(BTC)[/] equivale a [green]{formatado:.2f} Reais Brasileiros(R$)[/][/]\n"
            f"[red]Última atualização em:[/] [cyan]{data_br}[/]"
        )
        print("\n[white]Digite abaixo um valor em [green]Bitcoin(BTC)[/] para realizar a conversão![/]")
        try:
            valor_texto = input("Valor: BTC ")
            if "." in valor_texto:
                valor = float(valor_texto)
            else:
                valor = int(valor_texto)

            limpar_tela()
            conversao = valor * formatado
            print(f"[black]O valor em [green]Bitcoin(BTC)[/] escolhido é: [green]BTC {valor}[/]")
            print(f"\n[yellow]O resultado da conversão é:[/] [green]{conversao:.2f} Reais Brasileiros(R$)[/]")
            aguardar_enter()
            break

        except ValueError:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou 'letras' ao invés de 'número'. Tente novamente![/]")
            aguardar_enter()

def EURBRL():
    """
    Converte valores de Euro (EUR) para Reais Brasileiros (BRL).
    Obtém a cotação em tempo real através da API AwesomeAPI.
    """
    link = "https://economia.awesomeapi.com.br/json/last/EUR-BRL"
    pegar = requests.get(link)
    resultado = pegar.json()
    formatado = float(resultado["EURBRL"]["bid"])
    data_api = resultado["EURBRL"]["create_date"]
    data_objeto = datetime.strptime(data_api, "%Y-%m-%d %H:%M:%S")
    data_br = data_objeto.strftime("%d/%m/%Y %H:%M:%S")

    while True:
        limpar_tela()
        print("[black]Você selecionou converter [green]Euros(€)[/] para [green]Reais Brasileiros(R$)[/][/]\n")
        print(
            f"\n[yellow]Cotação:[/] [black]Atualmente [green]1 Euro(€)[/] equivale a [green]{formatado:.2f} Reais Brasileiros(R$)[/][/]\n"
            f"[red]Última atualização em:[/] [cyan]{data_br}[/]"
        )
        print("\n[white]Digite abaixo um valor em [green]Euros(€)[/] para realizar a conversão![/]")
        try:
            valor_texto = input("Valor: € ")
            if "." in valor_texto:
                valor = float(valor_texto)
            else:
                valor = int(valor_texto)

            limpar_tela()
            conversao = valor * formatado
            print(f"[black]O valor em [green]Euros(€)[/] escolhido é: [green]€ {valor}[/]")
            print(f"\n[yellow]O resultado da conversão é:[/] [green]{conversao:.2f} Reais Brasileiros(R$)[/]")
            aguardar_enter()
            break

        except ValueError:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou 'letras' ao invés de 'número'. Tente novamente![/]")
            aguardar_enter()

def BRLEUR():
    """
    Converte valores de Reais Brasileiros (BRL) para Euro (EUR).
    Obtém a cotação em tempo real através da API AwesomeAPI.
    """
    link = "https://economia.awesomeapi.com.br/json/last/BRL-EUR"
    pegar = requests.get(link)
    resultado = pegar.json()
    formatado = float(resultado["BRLEUR"]["bid"])
    data_api = resultado["BRLEUR"]["create_date"]
    data_objeto = datetime.strptime(data_api, "%Y-%m-%d %H:%M:%S")
    data_br = data_objeto.strftime("%d/%m/%Y %H:%M:%S")

    while True:
        limpar_tela()
        print("[black]Você selecionou converter [green]Reais Brasileiros(R$)[/] para [green]Euros(€)[/][/]\n")
        print(
            f"\n[yellow]Cotação:[/] [black]Atualmente [green]1 Real Brasileiro(R$)[/] equivale a [green]{formatado:.2f} Euros(€)[/][/]\n"
            f"[red]Última atualização em:[/] [cyan]{data_br}[/]"
        )
        print("\n[white]Digite abaixo um valor em [green]Reais Brasileiros(R$)[/] para realizar a conversão![/]")
        try:
            valor_texto = input("Valor: R$ ")
            if "." in valor_texto:
                valor = float(valor_texto)
            else:
                valor = int(valor_texto)

            limpar_tela()
            conversao = valor * formatado
            print(f"[black]O valor em [green]Reais Brasileiros(R$)[/] escolhido é: [green]R$ {valor}[/]")
            print(f"\n[yellow]O resultado da conversão é:[/] [green]{conversao:.2f} Euros(€)[/]")
            aguardar_enter()
            break

        except ValueError:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou 'letras' ao invés de 'número'. Tente novamente![/]")
            aguardar_enter()

def USDBRL():
    """
    Converte valores de Dólar Americano (USD) para Reais Brasileiros (BRL).
    Obtém a cotação em tempo real através da API AwesomeAPI.
    """
    link = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    pegar = requests.get(link)
    resultado = pegar.json()
    formatado = float(resultado["USDBRL"]["bid"])
    data_api = resultado["USDBRL"]["create_date"]
    data_objeto = datetime.strptime(data_api, "%Y-%m-%d %H:%M:%S")
    data_br = data_objeto.strftime("%d/%m/%Y %H:%M:%S")

    while True:
        limpar_tela()
        print("[black]Você selecionou converter [green]Dólares(US$)[/] para [green]Reais Brasileiros(R$)[/][/]\n")
        print(
            f"\n[yellow]Cotação:[/] [black]Atualmente [green]1 Dólar(US$)[/] equivale a [green]{formatado:.2f} Reais Brasileiros(R$)[/][/]\n"
            f"[red]Última atualização em:[/] [cyan]{data_br}[/]"
        )
        print("\n[white]Digite abaixo um valor em [green]Dólares(US$)[/] para realizar a conversão![/]")
        try:
            valor_texto = input("Valor: US$ ")
            if "." in valor_texto:
                valor = float(valor_texto)
            else:
                valor = int(valor_texto)

            limpar_tela()
            conversao = valor * formatado
            print(f"[black]O valor em [green]Dólares(US$)[/] escolhido é: [green]US$ {valor}[/]")
            print(f"\n[yellow]O resultado da conversão é:[/] [green]{conversao:.2f} Reais Brasileiros(R$)[/]")
            aguardar_enter()
            break

        except ValueError:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou 'letras' ao invés de 'número'. Tente novamente![/]")
            aguardar_enter()

def BRLUSD():
    """
    Converte valores de Reais Brasileiros (BRL) para Dólar Americano (USD).
    Obtém a cotação em tempo real através da API AwesomeAPI.
    """
    link = "https://economia.awesomeapi.com.br/json/last/BRL-USD"
    pegar = requests.get(link)
    resultado = pegar.json()
    formatado = float(resultado["BRLUSD"]["bid"])
    data_api = resultado["BRLUSD"]["create_date"]
    data_objeto = datetime.strptime(data_api, "%Y-%m-%d %H:%M:%S")
    data_br = data_objeto.strftime("%d/%m/%Y %H:%M:%S")

    while True:
        limpar_tela()
        print("[black]Você selecionou converter [green]Reais Brasileiros(R$)[/] para [green]Dólares(US$)[/][/]\n")
        print(
            f"\n[yellow]Cotação:[/] [black]Atualmente [green]1 Real Brasileiro(R$)[/] equivale a [green]{formatado:.2f} Dólares(US$)[/][/]\n"
            f"[red]Última atualização em:[/] [cyan]{data_br}[/]"
        )
        print("\n[white]Digite abaixo um valor em [green]Reais Brasileiros(R$)[/] para realizar a conversão![/]")
        try:
            valor_texto = input("Valor: R$ ")
            if "." in valor_texto:
                valor = float(valor_texto)
            else:
                valor = int(valor_texto)

            limpar_tela()
            conversao = valor * formatado
            print(f"[black]O valor em [green]Reais(R$)[/] escolhido é: [green]R$ {valor}[/]")
            print(f"\n[yellow]O resultado da conversão é:[/] [green]{conversao:.2f} Dólares(US$)[/]")
            aguardar_enter()
            break

        except ValueError:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou 'letras' ao invés de 'número'. Tente novamente![/]")
            aguardar_enter()

def exibir_menu():
    """
    Exibe o menu principal do conversor de moedas.
    Mostra as opções de conversão disponíveis com formatação Rich.
    """
    limpar_tela()
    print("[yellow]========== CONVERSOR DE MOEDAS ==========[/]")
    print("[black]―-[/]" * 35)
    print(
        f"[{OpcoesConversor.OPCAO1.value}] - [black][green]Reais Brasileiros(R$)[/] para [green]Dólares(US$)[/][/] - [yellow][BRL/USD][/]\n"
        f"[{OpcoesConversor.OPCAO2.value}] - [black][green]Dólares(US$)[/] para [green]Reais Brasileiros(R$)[/][/] - [yellow][USD/BRL][/]")

    print("[black]―-[/]" * 35)
    print(
        f"[{OpcoesConversor.OPCAO3.value}] - [black][green]Reais Brasileiros(R$)[/] para [green]Euros(€)[/][/] - [yellow][BRL/EUR][/]\n"
        f"[{OpcoesConversor.OPCAO4.value}] - [black][green]Euros(€)[/] para [green]Reais Brasileiros(R$)[/][/] - [yellow][EUR/BRL][/]")

    print("[black]―-[/]" * 35)
    print(f"[{OpcoesConversor.OPCAO5.value}] - [black][green]Bitcoin(BTC)[/] para [green]Reais Brasileiros(R$)[/][/] - [yellow][BTC/BRL][/]")

    print("[black]―-[/]" * 35)
    print(f"[{OpcoesConversor.OPCAO6.value}] - [purple]Voltar![/]")
    print("[black]―-[/]" * 35)

def conversor_moedas():
    """
    Loop principal que exibe o menu de conversão de moedas
    e direciona para as funções específicas com base na escolha do usuário.
    """
    while True:
        exibir_menu()
        try:
            escolha = int(input("Digite uma das opções acima: "))
        except ValueError:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou 'letras' ao invés de 'número'. Tente novamente![/]")
            aguardar_enter()
            continue

        if escolha == OpcoesConversor.OPCAO1:
            BRLUSD()
        elif escolha == OpcoesConversor.OPCAO2:
            USDBRL()
        elif escolha == OpcoesConversor.OPCAO3:
            BRLEUR()
        elif escolha == OpcoesConversor.OPCAO4:
            EURBRL()
        elif escolha == OpcoesConversor.OPCAO5:
            BTCBRL()
        elif escolha == OpcoesConversor.OPCAO6:
            limpar_tela()
            print("[black]Voltando.....[/]")
            sleep(OpcoesConversor.TEMPO_ESPERA)
            break
        else:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou uma opção inválida(inexistente). Tente novamente![/]")
            aguardar_enter()