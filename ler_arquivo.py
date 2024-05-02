def ler_arquivo(nome_arquivo):
    lista = []
    with open(nome_arquivo, "r") as arquivo_aberto:
        for number in arquivo_aberto:
            lista.append(number.strip())
    return lista