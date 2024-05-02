import pandas as pd

# Dados vazios
dados = {
    'Nº do teste': [1],
    'Estrutura': [''],
    'Descrição': [''],
    'Tipo de Teste': [''],
    'Arranjo': [None],
    'Tempo Ordenação (s)': [None],
    'Memória Ordenação (KB)': [None],
    'Memória Inicial Ordenação (bytes)' : [None],
    'Memória Final Ordenação (bytes)' : [None],
    'Tempo (s)': [None],
    'Memória (KB)': [None],
    'Comparações': [None],
    'Memória Inicial (KB)': [None],
    'Memória Final (KB)': [None]
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Exibir DataFrame
print(df)
# Salvar DataFrame como Excel
nome_arquivo_excel = 'dados_teste.xlsx'
df.to_excel(nome_arquivo_excel, index=False)

print(f"DataFrame salvo como arquivo Excel: {nome_arquivo_excel}")
