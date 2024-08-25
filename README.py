# td1
#Codigo do td1


#esse eh o codigo do primeiro td de natureza discreta

def ler_conjuntos(linhas, posicao):
    conjunto_1 = set(map(str.strip, linhas[posicao + 1].split(',')))
    conjunto_2 = set(map(str.strip, linhas[posicao + 2].split(',')))
    return conjunto_1, conjunto_2

def realizar_operacao(codigo, conjunto_1, conjunto_2):
    operacoes = {
        'U': (conjunto_1.union(conjunto_2), "União"),
        'I': (conjunto_1.intersection(conjunto_2), "Interseção"),
        'D': (conjunto_1.difference(conjunto_2), "Diferença"),
        'C': ({(a, b) for a in conjunto_1 for b in conjunto_2}, "Produto cartesiano")
    }
    return operacoes.get(codigo, (None, None))

def formatar_resultado(codigo, resultado):
    if codigo == 'C':
        return '{' + ', '.join(f'({a}, {b})' for a, b in resultado) + '}'
    return '{' + ', '.join(sorted(resultado, key=str)) + '}'

def processar_operacoes(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    total_operacoes = int(linhas[0].strip())

    for i in range(total_operacoes):
        posicao = 1 + i * 3
        codigo_operacao = linhas[posicao].strip()
        conjunto_1, conjunto_2 = ler_conjuntos(linhas, posicao)
        resultado, nome_operacao = realizar_operacao(codigo_operacao, conjunto_1, conjunto_2)
        
        if resultado is not None:
            resultado_formatado = formatar_resultado(codigo_operacao, resultado)
            print(f"{nome_operacao}: conjunto 1 {conjunto_1}, conjunto 2 {conjunto_2}. Resultado: {resultado_formatado}")

if __name__ == "__main__":
    #colocar o arquivo
    processar_operacoes('teste.txt')

