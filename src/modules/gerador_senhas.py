import numpy as np
import string as st
from rich import print
from time import sleep
from utils.screen import limpar_tela, aguardar_enter
from utils.constantes import OpcoesSenhas, Opcoes1Senhas, Opcoes2Senhas, Opcoes3Senhas, Opcoes4Senhas

def numero_especial():
    """
    Gera senhas compostas exclusivamente por números e caracteres especiais.
    Permite ao usuário escolher o tamanho da senha e exibe o resultado.
    """
    numeros = st.digits
    especial = st.punctuation
    numeros_especial = numeros + especial
    numesp8 = np.random.choice(list(numeros_especial), 8)
    numesp10 = np.random.choice(list(numeros_especial), 10)
    numesp15 = np.random.choice(list(numeros_especial), 15)
    numesp20 = np.random.choice(list(numeros_especial), 20)
    numesp30 = np.random.choice(list(numeros_especial), 30)
    numesp40 = np.random.choice(list(numeros_especial), 40)

    while True:
        limpar_tela()
        print(
            "[yellow]========== NUMEROS + ESPECIAIS ==========[/]\n"
            "\n[yellow]Escolha a quantidade de Caracteres abaixo![/]"
        )
        print("[black]―-[/]" * 20)
        print(
            f"{[Opcoes4Senhas.OPCAO1.value]} - [green]8 Caracteres[/]\n"
            f"{[Opcoes4Senhas.OPCAO2.value]} - [green]10 Caracteres[/]\n"
            f"{[Opcoes4Senhas.OPCAO3.value]} - [green]15 Caracteres[/]\n"
            f"{[Opcoes4Senhas.OPCAO4.value]} - [green]20 Caracteres[/]\n"
            f"{[Opcoes4Senhas.OPCAO5.value]} - [green]30 Caracteres[/]\n"
            f"{[Opcoes4Senhas.OPCAO6.value]} - [green]40 Caracteres[/]"
        )
        print("[black]―-[/]" * 20)
        print(f"{[Opcoes4Senhas.OPCAO7.value]} - [purple]Voltar![/]")
        print("[black]―-[/]" * 20)
        try:
            escolha = int(input("Digite uma das opções acima: "))
        except ValueError:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou 'letras' ao invés de 'número'. Tente novamente![/]")
            aguardar_enter()
            continue

        if escolha == Opcoes4Senhas.OPCAO1:
            limpar_tela()
            print("[black]Você selecionou 8 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(numesp8))
            aguardar_enter()
        elif escolha == Opcoes4Senhas.OPCAO2:
            limpar_tela()
            print("[black]Você selecionou 10 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(numesp10))
            aguardar_enter()
        elif escolha == Opcoes4Senhas.OPCAO3:
            limpar_tela()
            print("[black]Você selecionou 15 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(numesp15))
            aguardar_enter()
        elif escolha == Opcoes4Senhas.OPCAO4:
            limpar_tela()
            print("[black]Você selecionou 20 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(numesp20))
            aguardar_enter()
        elif escolha == Opcoes4Senhas.OPCAO5:
            limpar_tela()
            print("[black]Você selecionou 30 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(numesp30))
            aguardar_enter()
        elif escolha == Opcoes4Senhas.OPCAO6:
            limpar_tela()
            print("[black]Você selecionou 40 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(numesp40))
            aguardar_enter()
        elif escolha == Opcoes4Senhas.OPCAO7:
            limpar_tela()
            print("[black]Voltando.....[/]")
            sleep(OpcoesSenhas.TEMPO_ESPERA)
            break
        else:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou uma opção inválida(inexistente). Tente novamente![/]")
            aguardar_enter()

def letras_especial():
    """
    Gera senhas compostas por letras e caracteres especiais.
    O usuário escolhe o tamanho e o programa exibe a senha aleatória.
    """
    letras = st.ascii_letters
    especial = st.punctuation
    letras_especial = letras + especial
    letraesp8 = np.random.choice(list(letras_especial), 8)
    letraesp10 = np.random.choice(list(letras_especial), 10)
    letraesp15 = np.random.choice(list(letras_especial), 15)
    letraesp20 = np.random.choice(list(letras_especial), 20)
    letraesp30 = np.random.choice(list(letras_especial), 30)
    letraesp40 = np.random.choice(list(letras_especial), 40)

    while True:
        limpar_tela()
        print("[yellow]========== LETRAS + ESPECIAIS ==========[/]\n[yellow]Escolha a quantidade de Caracteres abaixo![/]")
        print("[black]―-[/]" * 20)
        print(
            f"{[Opcoes3Senhas.OPCAO1.value]} - [green]8 Caracteres[/]\n"
            f"{[Opcoes3Senhas.OPCAO2.value]} - [green]10 Caracteres[/]\n"
            f"{[Opcoes3Senhas.OPCAO3.value]} - [green]15 Caracteres[/]\n"
            f"{[Opcoes3Senhas.OPCAO4.value]} - [green]20 Caracteres[/]\n"
            f"{[Opcoes3Senhas.OPCAO5.value]} - [green]30 Caracteres[/]\n"
            f"{[Opcoes3Senhas.OPCAO6.value]} - [green]40 Caracteres[/]"
        )
        print("[black]―-[/]" * 20)
        print(f"{[Opcoes3Senhas.OPCAO7.value]} - [purple]Voltar![/]")
        print("[black]―-[/]" * 20)

        try:
            escolha = int(input("Digite uma das opções acima: "))
        except ValueError:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou 'letras' ao invés de 'número'. Tente novamente![/]")
            aguardar_enter()
            continue

        if escolha == Opcoes3Senhas.OPCAO1:
            limpar_tela()
            print("[black]Você selecionou 8 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(letraesp8))
            aguardar_enter()
        elif escolha == Opcoes3Senhas.OPCAO2:
            limpar_tela()
            print("[black]Você selecionou 10 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(letraesp10))
            aguardar_enter()
        elif escolha == Opcoes3Senhas.OPCAO3:
            limpar_tela()
            print("[black]Você selecionou 15 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(letraesp15))
            aguardar_enter()
        elif escolha == Opcoes3Senhas.OPCAO4:
            limpar_tela()
            print("[black]Você selecionou 20 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(letraesp20))
            aguardar_enter()
        elif escolha == Opcoes3Senhas.OPCAO5:
            limpar_tela()
            print("[black]Você selecionou 30 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(letraesp30))
            aguardar_enter()
        elif escolha == Opcoes3Senhas.OPCAO6:
            limpar_tela()
            print("[black]Você selecionou 40 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(letraesp40))
            aguardar_enter()
        elif escolha == Opcoes3Senhas.OPCAO7:
            limpar_tela()
            print("[black]Voltando.....[/]")
            sleep(OpcoesSenhas.TEMPO_ESPERA)
            break
        else:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou uma opção inválida(inexistente). Tente novamente![/]")
            aguardar_enter()
            
def letras_comnumeros():
    """
    Gera senhas compostas por letras (maiúsculas e minúsculas) e números.
    O usuário escolhe o tamanho e o programa exibe a senha gerada.
    """
    letras = st.ascii_letters
    numeros = st.digits
    letrasnumeros = letras + numeros
    letranum8 = np.random.choice(list(letrasnumeros), 8)
    letranum10 = np.random.choice(list(letrasnumeros), 10)
    letranum15 = np.random.choice(list(letrasnumeros), 15)
    letranum20 = np.random.choice(list(letrasnumeros), 20)
    letranum30 = np.random.choice(list(letrasnumeros), 30)
    letranum40 = np.random.choice(list(letrasnumeros), 40)

    while True:
        limpar_tela()
        print("[yellow]========== LETRAS + NUMEROS ==========[/]\n[yellow]Escolha a quantidade de Caracteres abaixo![/]")
        print("[black]―-[/]" * 20)
        print(
            f"{[Opcoes2Senhas.OPCAO1.value]} - [green]8 Caracteres[/]\n"
            f"{[Opcoes2Senhas.OPCAO2.value]} - [green]10 Caracteres[/]\n"
            f"{[Opcoes2Senhas.OPCAO3.value]} - [green]15 Caracteres[/]\n"
            f"{[Opcoes2Senhas.OPCAO4.value]} - [green]20 Caracteres[/]\n"
            f"{[Opcoes2Senhas.OPCAO5.value]} - [green]30 Caracteres[/]\n"
            f"{[Opcoes2Senhas.OPCAO6.value]} - [green]40 Caracteres[/]"
        )
        print("[black]―-[/]" * 20)
        print(f"{[Opcoes2Senhas.OPCAO7.value]} - [purple]Voltar![/]")
        print("[black]―-[/]" * 20)

        try:
            escolha = int(input("Digite uma das opções acima: "))
        except ValueError:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou 'letras' ao invés de 'número'. Tente novamente![/]")
            aguardar_enter()
            continue

        if escolha == Opcoes2Senhas.OPCAO1:
            limpar_tela()
            print("[black]Você selecionou 8 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(letranum8))
            aguardar_enter()
        elif escolha == Opcoes2Senhas.OPCAO2:
            limpar_tela()
            print("[black]Você selecionou 10 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(letranum10))
            aguardar_enter()
        elif escolha == Opcoes2Senhas.OPCAO3:
            limpar_tela()
            print("[black]Você selecionou 15 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(letranum15))
            aguardar_enter()
        elif escolha == Opcoes2Senhas.OPCAO4:
            limpar_tela()
            print("[black]Você selecionou 20 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(letranum20))
            aguardar_enter()
        elif escolha == Opcoes2Senhas.OPCAO5:
            limpar_tela()
            print("[black]Você selecionou 30 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(letranum30))
            aguardar_enter()
        elif escolha == Opcoes2Senhas.OPCAO6:
            limpar_tela()
            print("[black]Você selecionou 40 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(letranum40))
            aguardar_enter()
        elif escolha == Opcoes2Senhas.OPCAO7:
            limpar_tela()
            print("[black]Voltando.....[/]")
            sleep(OpcoesSenhas.TEMPO_ESPERA)
            break
        else:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou uma opção inválida(inexistente). Tente novamente![/]")
            aguardar_enter()

def todos_caracteres():
    """
    Gera senhas completas com letras, números e caracteres especiais.
    Permite ao usuário escolher o tamanho da senha e apresenta o resultado.
    """
    letras = st.ascii_letters
    numeros = st.digits
    especial = st.punctuation
    algarismos = letras + numeros + especial
    todos8 = np.random.choice(list(algarismos), 8)
    todos10 = np.random.choice(list(algarismos), 10)
    todos15 = np.random.choice(list(algarismos), 15)
    todos20 = np.random.choice(list(algarismos), 20)
    todos30 = np.random.choice(list(algarismos), 30)
    todos40 = np.random.choice(list(algarismos), 40)

    while True:
        limpar_tela()
        print("[yellow]========== TODOS CARACTERES ==========[/]\n[yellow]Escolha a quantidade de Caracteres abaixo![/]")
        print("[black]―-[/]" * 20)
        print(
            f"{[Opcoes1Senhas.OPCAO1.value]} - [green]8 Caracteres[/]\n"
            f"{[Opcoes1Senhas.OPCAO2.value]} - [green]10 Caracteres[/]\n"
            f"{[Opcoes1Senhas.OPCAO3.value]} - [green]15 Caracteres[/]\n"
            f"{[Opcoes1Senhas.OPCAO4.value]} - [green]20 Caracteres[/]\n"
            f"{[Opcoes1Senhas.OPCAO5.value]} - [green]30 Caracteres[/]\n"
            f"{[Opcoes1Senhas.OPCAO6.value]} - [green]40 Caracteres[/]"
        )
        print("[black]―-[/]" * 20)
        print(f"{[Opcoes1Senhas.OPCAO7.value]} - [purple]Voltar![/]")
        print("[black]―-[/]" * 20)

        try:
            escolha = int(input("Digite uma das opções acima: "))
        except ValueError:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou 'letras' ao invés de 'número'. Tente novamente![/]")
            aguardar_enter()
            continue

        if escolha == Opcoes1Senhas.OPCAO1:
            limpar_tela()
            print("[black]Você selecionou 8 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(todos8))
            aguardar_enter()
        elif escolha == Opcoes1Senhas.OPCAO2:
            limpar_tela()
            print("[black]Você selecionou 10 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(todos10))
            aguardar_enter()
        elif escolha == Opcoes1Senhas.OPCAO3:
            limpar_tela()
            print("[black]Você selecionou 15 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(todos15))
            aguardar_enter()
        elif escolha == Opcoes1Senhas.OPCAO4:
            limpar_tela()
            print("[black]Você selecionou 20 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(todos20))
            aguardar_enter()
        elif escolha == Opcoes1Senhas.OPCAO5:
            limpar_tela()
            print("[black]Você selecionou 30 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(todos30))
            aguardar_enter()
        elif escolha == Opcoes1Senhas.OPCAO6:
            limpar_tela()
            print("[black]Você selecionou 40 Caracteres![/]\n\n[green]Senha Gerada![/]")
            print("".join(todos40))
            aguardar_enter()
        elif escolha == Opcoes1Senhas.OPCAO7:
            limpar_tela()
            print("[black]Voltando.....[/]")
            sleep(OpcoesSenhas.TEMPO_ESPERA)
            break
        else:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou uma opção inválida(inexistente). Tente novamente![/]")
            aguardar_enter()

def exibir_menu():
    """
    Exibe o menu principal do gerador de senhas, listando todas as categorias disponíveis.
    """
    limpar_tela()
    print("[yellow]========== GERADOR DE SENHAS ==========[/]")
    print("[black]―-[/]" * 25)
    print(
        f"{[OpcoesSenhas.OPCAO1.value]} - [green]Gerar Senhas com Todos Caracteres[/]\n"
        f"{[OpcoesSenhas.OPCAO2.value]} - [green]Gerar Senhas com Letras + Números[/]\n"
        f"{[OpcoesSenhas.OPCAO3.value]} - [green]Gerar Senhas com Letras + Caracteres Especiais[/]\n"
        f"{[OpcoesSenhas.OPCAO4.value]} - [green]Gerar Senhas com Números + Caracteres Especiais[/]"
    )
    print("[black]―-[/]" * 25)
    print(f"{[OpcoesSenhas.OPCAO5.value]} - [purple]Voltar![/]")
    print("[black]―-[/]" * 25)

def gerador_senhas():
    """
    Loop principal do gerador de senhas.
    Direciona o usuário para os tipos de senha que deseja gerar.
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

        if escolha == OpcoesSenhas.OPCAO1:
            todos_caracteres()
        elif escolha == OpcoesSenhas.OPCAO2:
            letras_comnumeros()
        elif escolha == OpcoesSenhas.OPCAO3:
            letras_especial()
        elif escolha == OpcoesSenhas.OPCAO4:
            numero_especial()
        elif escolha == OpcoesSenhas.OPCAO5:
            limpar_tela()
            print("[black]Voltando.....[/]")
            sleep(OpcoesSenhas.TEMPO_ESPERA)
            break
        else:
            limpar_tela()
            print("[red]ERRO![/]\n[red]Você deixou vazio, ou digitou uma opção inválida(inexistente). Tente novamente![/]")
            aguardar_enter()