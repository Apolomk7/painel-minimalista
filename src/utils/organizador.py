import os
import shutil  ## - Módulos para operações com arquivos (mover, copiar, etc...)
from pathlib import Path  ## - Fornece uma maneira mais fácil de trabalhar com caminhos de arquivos

## - Dicionário de extensões e pastas correspondentes
EXTENSOES_PASTAS = {
    # Documentos
    ".pdf": "PDFs",
    ".doc": "Documentos",
    ".docx": "Documentos",
    ".txt": "Textos",
    ".xls": "Planilhas",
    ".xlsx": "Planilhas",
    ".ppt": "Apresentações",
    ".pptx": "Apresentações",

    # Imagens
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".png": "Imagens",
    ".gif": "Imagens",
    ".bmp": "Imagens",
    ".svg": "Imagens",

    # Áudio e Vídeo
    ".mp3": "Musicas",
    ".wav": "Musicas",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    # Arquivos compactados
    ".zip": "Compactados",
    ".rar": "Compactados",
    ".7z": "Compactados",

    # Programação
    ".py": "Codigos Python",
    ".js": "Codigos JavaScript",
    ".html": "Codigos HTML",
    ".css": "Codigos CSS",
    ".json": "Dados JSON",
    ".csv": "Dados CSV",

    # Outros
    ".exe": "Executaveis",
    ".msi": "Executaveis"
}

def criar_pasta(diretorio_base):
    """
    Cria todas as pastas necessárias no diretório base, conforme definidas
    no dicionário EXTENSOES_PASTAS, se elas ainda não existirem.

    Args:
        diretorio_base (str): Caminho do diretório que será organizado.
    """
    # Obtém todos os nomes de pastas únicos do dicionário
    pastas_necessarias = set(EXTENSOES_PASTAS.values())

    for pasta in pastas_necessarias:
        caminho_pasta = os.path.join(diretorio_base, pasta)

        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)
            print(f"Pasta criada: {caminho_pasta}")

def organizar_arquivos(diretorio_base):
    """
    Organiza os arquivos presentes no diretório base movendo-os para
    subpastas nomeadas de acordo com suas extensões, conforme definido
    no dicionário EXTENSOES_PASTAS.

    Args:
        diretorio_base (str): Caminho do diretório que será organizado.
    """
    criar_pasta(diretorio_base)

    with os.scandir(diretorio_base) as itens:
        for item in itens:
            # Ignora diretórios, processa apenas arquivos
            if item.is_file():
                extensao = Path(item.name).suffix.lower()

                if extensao in EXTENSOES_PASTAS:
                    pasta_destino = EXTENSOES_PASTAS[extensao]
                    caminho_destino = os.path.join(diretorio_base, pasta_destino, item.name)
                    caminho_atual = os.path.join(diretorio_base, item.name)

                    try:
                        shutil.move(caminho_atual, caminho_destino)
                        print(f"Arquivo movido: {item.name} -> {pasta_destino}/")
                    except Exception as e:
                        print(f"Erro ao mover {item.name}: {e}")
                else:
                    # Caso a extensão não seja reconhecida, exibe aviso.
                    print(f"Extensão não reconhecida: {item.name} (extensão: {extensao})")