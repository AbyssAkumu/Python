import os
import shutil

# 1. Definição do local que será organizado
# O 'r' antes das aspas serve para o Windows não se confundir com as barras \
caminho = r"C:\Users\Lukin\Downloads"

# 2. Pegar a lista de tudo que está dentro da pasta
arquivos = os.listdir(caminho)

# 3. Dicionário de Regras (Fácil de adicionar novos tipos depois)
locais = {
    ".pdf": "Documentos",
    ".png": "Imagens",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",
    ".xlsx": "Planilhas",
    ".csv": "Planilhas",
    ".docx": "Textos",
    ".mp4": "Videos",
    ".zip": "Compactados"
}

# 4. O Loop que processa cada arquivo
for arquivo in arquivos:
    # Separa o nome da extensão (ex: 'aula' e '.pdf')
    nome, extensao = os.path.splitext(arquivo)
    
    # Converte a extensão para minúsculo (evita erro se for .PDF em vez de .pdf)
    extensao = extensao.lower()

    # Verifica se a extensão está no nosso dicionário de regras
    if extensao in locais:
        # Define o nome da pasta de destino com base no dicionário
        pasta_nome = locais[extensao]
        pasta_destino = os.path.join(caminho, pasta_nome)

        # Se a pasta ainda não existir, o robô cria ela agora
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
            print(f"Pasta {pasta_nome} criada com sucesso!")

        # Define o caminho antigo e o novo caminho do arquivo
        caminho_antigo = os.path.join(caminho, arquivo)
        caminho_novo = os.path.join(pasta_destino, arquivo)

        # Tenta mover o arquivo
        try:
            shutil.move(caminho_antigo, caminho_novo)
            print(f"Movido: {arquivo} -> {pasta_nome}")
        except Exception as e:
            print(f"Erro ao mover {arquivo}: {e}")

print("\n--- Automação Finalizada com Sucesso! ---")