# 🚀 Automações em Python - Portfólio

Bem-vindo ao meu repositório de automações! Aqui apresento soluções desenvolvidas para otimizar processos repetitivos e gestão de dados.

## 🛠️ Projetos Principais

### 2. Processador de Planilhas e Relatórios
Automação que lê dados de vendas, realiza cálculos financeiros (comissões e impostos) e gera relatórios individuais em Excel.
* **Tecnologias:** Python, Biblioteca `Pandas`.
* **Benefício:** Redução de erros humanos em cálculos e agilidade na geração de fechamentos mensais.

---
📫 **Contato para orçamentos e projetos:** [Seu e-mail ou link do LinkedIn/Workana]
import pandas as pd

# 1. Configurações
ARQUIVO_ENTRADA = "vendas_brutas.xlsx" # Planilha que o cliente te daria
ARQUIVO_SAIDA = "relatorio_final_vendedores.xlsx"

# 2. Carregamento (Aqui você mostra que sabe ler arquivos)
# Se não tiver o arquivo agora, use o seu método do dicionário que já testamos
try:
    tabela = pd.read_excel(ARQUIVO_ENTRADA)
except:
    # Caso o arquivo não exista, criamos os dados de teste para não dar erro
    dados = {
        'Produto': ['Teclado', 'Mouse', 'Monitor', 'Teclado', 'Mouse'],
        'Valor': [150, 80, 900, 150, 80],
        'Vendedor': ['Lukin', 'Lukin', 'Lukin', 'Joao', 'Joao']
    }
    tabela = pd.DataFrame(dados)

# 3. Processamento de Dados (Onde você gera valor)
tabela['Comissao'] = tabela['Valor'] * 0.10
tabela['Imposto'] = tabela['Valor'] * 0.05
tabela['Valor Final'] = tabela['Valor'] - tabela['Imposto']

# 4. Filtro por Vendedor
vendedores = tabela['Vendedor'].unique() # Pega os nomes únicos (Lukin, Joao)

for vendedor in vendedores:
    tabela_filtrada = tabela[tabela['Vendedor'] == vendedor]
    
    # Salva um arquivo separado para cada vendedor (Isso impressiona muito!)
    nome_saida = f"Relatorio_{vendedor}.xlsx"
    tabela_filtrada.to_excel(nome_saida, index=False)
    print(f"Relatório gerado para: {vendedor}")

print("\n--- Automação de Planilhas Concluída! ---")
