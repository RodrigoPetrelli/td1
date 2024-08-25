# td1
#Codigo do td1


#esse eh o codigo do primeiro td de natureza discreta

def processar_operacoes(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    total_operacoes = int(linhas[0].strip())
    posicao = 1

    for _ in range(total_operacoes):
        codigo_operacao = linhas[posicao].strip()
        conjunto_1 = set(map(str.strip,
                             linhas[posicao + 1].strip().split(',')))
        conjunto_2 = set(map(str.strip,
                             linhas[posicao + 2].strip().split(',')))

        if codigo_operacao == 'U':
            resultado = conjunto_1.union(conjunto_2)
            nome_operacao = "União"
        elif codigo_operacao == 'I':
            resultado = conjunto_1.intersection(conjunto_2)
            nome_operacao = "Interseção"
        elif codigo_operacao == 'D':
            resultado = conjunto_1.difference(conjunto_2)
            nome_operacao = "Diferença"
        elif codigo_operacao == 'C':
            resultado = {(a, b) for a in conjunto_1 for b in conjunto_2}
            nome_operacao = "Produto cartesiano"
        else:
            continue

        if codigo_operacao == 'C':
            resultado_formatado = '{' + ', '.join(f'({a}, {b})'
                                                  for a, b in resultado) + '}'
        else:
            resultado_formatado = '{' + ', '.join(sorted(resultado,
                                                         key=str)) + '}'

        print(
            f"{nome_operacao}: conjunto 1 {conjunto_1}, conjunto 2 {conjunto_2}. Resultado: {resultado_formatado}"
        )

        posicao += 3


if __name__ == "__main__":
    # coloque o arquivo
    processar_operacoes('teste.txt')

