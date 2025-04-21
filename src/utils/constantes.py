from enum import Enum

## - Constantes Menu Principal
class OpcoesMenu(int, Enum):
    """
    Enum que define as opções disponíveis no Menu Principal.
    Também especifica o tempo de espera padrão para transições.
    """
    TEMPO_ESPERA = 2  ## - Tempo Definido para sleep() apenas em Menu Principal!
    OPCAO1 = 1  ## - Painel Minimalista
    OPCAO2 = 2  ## - Créditos
    OPCAO0 = 0  ## - Sair!

## - Constantes Painel Minimalista
class OpcoesPainel(int, Enum):
    """
    Enum que define as opções do Painel Minimalista.
    """
    TEMPO_ESPERA = 2  ## - Tempo Definido para sleep() apenas em Painel Minimalista
    OPCAO1 = 1  ## - Conversor de Moedas
    OPCAO2 = 2  ## - Gerador de Senhas
    OPCAO3 = 3  ## - Organizador de Arquivos
    OPCAO4 = 4  ## - Voltar ao Menu Principal!
    OPCAO0 = 0  ## - Sair!

## - Constantes Conversor de Moedas
class OpcoesConversor(int, Enum):
    """
    Enum que define as opções do Conversor de Moedas.
    """
    TEMPO_ESPERA = 2  ## - Tempo Definido para sleep() apenas em Conversor de Moedas
    OPCAO1 = 1  ## - Reais Brasileiros(R$) para Dólares(US$) [BRL/USD]
    OPCAO2 = 2  ## - Dólares(US$) para Reais Brasileiros(R$) [USD/BRL]
    OPCAO3 = 3  ## - Reais Brasileiros(R$) para Euros(€) [BRL/EUR]
    OPCAO4 = 4  ## - Euros(€) para Reais Brasileiros(R$) [EUR/BRL]
    OPCAO5 = 5  ## - Bitcoin(BTC) para Reais Brasileiros(R$) [BTC/BRL]
    OPCAO6 = 6  ## - Voltar!

## - Constantes Gerador de Senhas
class OpcoesSenhas(int, Enum):
    """
    Enum que define as opções de tipos de senhas no Gerador de Senhas.
    """
    TEMPO_ESPERA = 2  ## - Tempo Definido para sleep() apenas em Gerador de Senhas
    OPCAO1 = 1  ## - Gerar Senhas com Todos Caracteres
    OPCAO2 = 2  ## - Gerar Senhas com Letras + Números
    OPCAO3 = 3  ## - Gerar Senhas com Letras + Caracteres Especiais
    OPCAO4 = 4  ## - Gerar Senhas com Números + Caracteres Especiais
    OPCAO5 = 5  ## - Voltar!

## - Constantes das Opções Gerador de Senhas
class Opcoes1Senhas(int, Enum):
    """
    Enum que define quantidades fixas de caracteres para senhas com todos os caracteres.
    """
    OPCAO1 = 1  ## - 8 Caracteres
    OPCAO2 = 2  ## - 10 Caracteres
    OPCAO3 = 3  ## - 15 Caracteres
    OPCAO4 = 4  ## - 20 Caracteres
    OPCAO5 = 5  ## - 30 Caracteres
    OPCAO6 = 6  ## - 40 Caracteres
    OPCAO7 = 7  ## - Voltar!

## - Constantes das Opções Gerador de Senhas
class Opcoes2Senhas(int, Enum):
    """
    Enum que define quantidades fixas de caracteres para senhas com Letras e Números.
    """
    OPCAO1 = 1  ## - 8 Caracteres
    OPCAO2 = 2  ## - 10 Caracteres
    OPCAO3 = 3  ## - 15 Caracteres
    OPCAO4 = 4  ## - 20 Caracteres
    OPCAO5 = 5  ## - 30 Caracteres
    OPCAO6 = 6  ## - 40 Caracteres
    OPCAO7 = 7  ## - Voltar!

## - Constantes das Opções Gerador de Senhas
class Opcoes3Senhas(int, Enum):
    """
    Enum que define quantidades fixas de caracteres para senhas com Letras e Caracteres Especiais.
    """
    OPCAO1 = 1  ## - 8 Caracteres
    OPCAO2 = 2  ## - 10 Caracteres
    OPCAO3 = 3  ## - 15 Caracteres
    OPCAO4 = 4  ## - 20 Caracteres
    OPCAO5 = 5  ## - 30 Caracteres
    OPCAO6 = 6  ## - 40 Caracteres
    OPCAO7 = 7  ## - Voltar!

## - Constantes das Opções Gerador de Senhas
class Opcoes4Senhas(int, Enum):
    """
    Enum que define quantidades fixas de caracteres para senhas com Números e Caracteres Especiais.
    """
    OPCAO1 = 1  ## - 8 Caracteres
    OPCAO2 = 2  ## - 10 Caracteres
    OPCAO3 = 3  ## - 15 Caracteres
    OPCAO4 = 4  ## - 20 Caracteres
    OPCAO5 = 5  ## - 30 Caracteres
    OPCAO6 = 6  ## - 40 Caracteres
    OPCAO7 = 7  ## - Voltar!

## - Constantes Organizador de Arquivos
class OpcoesArquivos(int, Enum):
    """
    Enum que define as opções para o Organizador de Arquivos.
    """
    TEMPO_ESPERA = 2  ## - Tempo Definido para sleep() apenas no Organizador de Arquivos
    OPCAO1 = 1  ## - Organizar por tipo de arquivo
    OPCAO2 = 2  ## - Organizar por data
    OPCAO3 = 3  ## - Voltar!