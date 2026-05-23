import sys
import os

def traduzir_linha(linha, indentacao):
    linha = linha.strip()

    if linha == "":
        return "", indentacao

    if linha.startswith("REMIX"):
        comentario = linha.replace("REMIX", "#", 1)
        return "    " * indentacao + comentario, indentacao

    if linha.startswith("HEEHEE"):
        conteudo = linha.replace("HEEHEE", "", 1).strip()

        if conteudo.startswith('"') and conteudo.endswith('"') and "{" in conteudo and "}" in conteudo:
            codigo = "    " * indentacao + "tocar_heehee()\n"
            codigo += "    " * indentacao + f"print(f{conteudo})"
        else:
            codigo = "    " * indentacao + "tocar_heehee()\n"
            codigo += "    " * indentacao + f"print({conteudo})"

        return codigo, indentacao

    if linha.startswith("SAY"):
        conteudo = linha.replace("SAY", "", 1).strip()

        if conteudo.startswith('"') and conteudo.endswith('"') and "{" in conteudo and "}" in conteudo:
            codigo = "    " * indentacao + f"print(f{conteudo})"
        else:
            codigo = "    " * indentacao + f"print({conteudo})"

        return codigo, indentacao

    if linha.startswith("BILLIE"):
        comando = linha.replace("BILLIE", "", 1).strip()
        return "    " * indentacao + comando, indentacao

    if linha.startswith("BEAT"):
        comando = linha.replace("BEAT", "", 1).strip()
        return "    " * indentacao + comando, indentacao

    if linha.startswith("MOONWALK"):
        partes = linha.split()

        variavel = partes[1]
        inicio = partes[3]
        fim = partes[5]

        codigo = f"for {variavel} in range({inicio}, {fim} + 1):"
        return "    " * indentacao + codigo, indentacao + 1

    if linha.startswith("BACKSLIDE"):
        partes = linha.split()

        variavel = partes[1]
        inicio = partes[3]
        fim = partes[5]

        codigo = f"for {variavel} in range({inicio}, {fim} - 1, -1):"
        return "    " * indentacao + codigo, indentacao + 1

    if linha.startswith("THRILLER"):
        condicao = linha.replace("THRILLER", "", 1).strip()
        codigo = f"if {condicao}:"
        return "    " * indentacao + codigo, indentacao + 1

    if linha in ["ENDMOONWALK", "ENDBACKSLIDE", "ENDTHRILLER"]:
        indentacao -= 1
        return "", indentacao

    raise SyntaxError(f"Comando desconhecido: {linha}")


def traduzir_arquivo(entrada):
    if not entrada.endswith(".moon"):
        print("Erro: o arquivo de entrada deve ter extensão .moon")
        return

    saida = entrada.replace(".moon", ".py")

    with open(entrada, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    codigo_python = []

    cabecalho = '''
import os
import winsound

def tocar_heehee():
    arquivo = "heehee.wav"

    if os.path.exists(arquivo):
        winsound.PlaySound(arquivo, winsound.SND_FILENAME)
'''

    codigo_python.append(cabecalho)

    indentacao = 0

    for linha in linhas:
        codigo, indentacao = traduzir_linha(linha, indentacao)

        if codigo != "":
            codigo_python.append(codigo)

    with open(saida, "w", encoding="utf-8") as arquivo:
        arquivo.write("\n".join(codigo_python))

    print(f"Arquivo traduzido com sucesso: {saida}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso correto:")
        print("py tradutor_moonlang.py arquivo.moon")
    else:
        traduzir_arquivo(sys.argv[1])