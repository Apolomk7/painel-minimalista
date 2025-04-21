import os
import shutil
from datetime import datetime

def obter_nome_unico(caminho):
    """
    Gera um nome de arquivo único para evitar sobrescrita.

    Caso o arquivo de destino já exista, adiciona um sufixo numérico
    incremental ao nome base antes da extensão.

    Args:
        caminho (str): Caminho completo do arquivo a ser verificado.

    Returns:
        str: Caminho modificado com sufixo se necessário, garantindo que não exista colisão.
    """
    if not os.path.exists(caminho):
        return caminho

    base, ext = os.path.splitext(caminho)
    contador = 1

    while True:
        novo_caminho = f"{base}_{contador}{ext}"
        if not os.path.exists(novo_caminho):
            return novo_caminho
        contador += 1

def organizar_por_data(diretorio_base):
    """
    Organiza arquivos em subpastas por ano e mês de modificação.

    Percorre todos os arquivos no diretório base e os move para
    pastas nomeadas no formato 'YYYY-MM', baseadas na data de modificação
    de cada arquivo.

    Args:
        diretorio_base (str): Caminho do diretório onde os arquivos estão localizados.
    """
    with os.scandir(diretorio_base) as itens:
        for item in itens:
            # Obtém a data de modificação do arquivo
            data_mod = datetime.fromtimestamp(item.stat().st_mtime)
            ano = data_mod.year
            mes = data_mod.month

            # Cria o nome da pasta no formato: "YYYY-MM"
            nome_pasta = f"{ano}-{mes:02d}"
            caminho_pasta = os.path.join(diretorio_base, nome_pasta)

            # Cria a pasta se não existir
            if not os.path.exists(caminho_pasta):
                os.makedirs(caminho_pasta)

            # Move o arquivo para a nova pasta
            shutil.move(
                os.path.join(diretorio_base, item.name),
                os.path.join(caminho_pasta, item.name)
            )