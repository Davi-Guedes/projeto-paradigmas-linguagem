import sys
import os
import time

def traduzir_operadores(texto):
    texto = texto.replace(" BILLIE ", " = ")
    texto = texto.replace(" WHOS_BAD ", " == ")
    texto = texto.replace(" RUSBE ", " != ")
    return texto

def traduzir_jackson5(texto):
    """
    Traduz JACKSON5 para lista Python e os operadores da MoonLang.
    """
    texto = texto.replace("JACKSON5[", "[")
    texto = traduzir_operadores(texto)
    return texto

def traduzir_linha(linha, indentacao):
    linha = linha.strip()

    # Ignora linhas vazias
    if linha == "":
        return "", indentacao

    # Comentário
    # MoonLang: REMIX comentario
    # Python:   # comentario
    if linha.startswith("REMIX"):
        comentario = linha.replace("REMIX", "#", 1)
        return "    " * indentacao + comentario, indentacao

    # Toca o áudio heehee.wav e, opcionalmente, imprime conteúdo
    # MoonLang: HEEHEE
    # MoonLang: HEEHEE "Mensagem"
    if linha.startswith("HEEHEE"):
        conteudo = linha.replace("HEEHEE", "", 1).strip()
        conteudo = traduzir_jackson5(conteudo)

        if conteudo == "":
            codigo = "    " * indentacao + "tocar_heehee()"
            return codigo, indentacao

        if (
            conteudo.startswith('"')
            and conteudo.endswith('"')
            and "{" in conteudo
            and "}" in conteudo
        ):
            codigo = "    " * indentacao + "tocar_heehee()\n"
            codigo += "    " * indentacao + f"print(f{conteudo})"
        else:
            codigo = "    " * indentacao + "tocar_heehee()\n"
            codigo += "    " * indentacao + f"print({conteudo})"

        return codigo, indentacao

    # Imprime conteúdo no terminal
    # MoonLang: SING "Oi"
    # Python:   print("Oi")
    if linha.startswith("SING"):
        conteudo = linha.replace("SING", "", 1).strip()
        conteudo = traduzir_jackson5(conteudo)

        if (
            conteudo.startswith('"')
            and conteudo.endswith('"')
            and "{" in conteudo
            and "}" in conteudo
        ):
            codigo = "    " * indentacao + f"print(f{conteudo})"
        else:
            codigo = "    " * indentacao + f"print({conteudo})"

        return codigo, indentacao

    # Interrompe um laço
    # MoonLang: BEAT_IT
    # Python:   break
    #
    # A ideia vem da música "Beat It", como se fosse:
    # "sai fora", "para", "quebra o loop".
    #
    # IMPORTANTE:
    # Esse bloco precisa vir antes do comando BEAT,
    # porque BEAT_IT também começa com a palavra BEAT.
    if linha == "BEAT_IT":
        codigo = "break"
        return "    " * indentacao + codigo, indentacao

    # Continua para a próxima repetição do laço
    # MoonLang: DONT_STOP
    # Python:   continue
    #
    # A ideia vem de "Don't Stop", ou seja:
    # não para o programa, apenas pula para a próxima volta do loop.
    if linha == "DONT_STOP":
        codigo = "continue"
        return "    " * indentacao + codigo, indentacao

    # While
    # MoonLang: BEAT contador <= 5
    # Python:   while contador <= 5:
    if linha.startswith("BEAT"):
        condicao = linha.replace("BEAT", "", 1).strip()
        condicao = traduzir_jackson5(condicao)

        if condicao == "":
            raise SyntaxError("Uso correto: BEAT condicao")

        codigo = f"while {condicao}:"
        return "    " * indentacao + codigo, indentacao + 1

    # For crescente
    # MoonLang: MOONWALK i FROM 1 TO 5
    # Python:   for i in range(1, 5 + 1):
    if linha.startswith("MOONWALK"):
        partes = linha.split()

        if len(partes) != 6 or partes[2] != "FROM" or partes[4] != "TO":
            raise SyntaxError(
                "Uso correto: MOONWALK variavel FROM inicio TO fim"
            )

        variavel = partes[1]
        inicio = traduzir_jackson5(partes[3])
        fim = traduzir_jackson5(partes[5])

        codigo = f"for {variavel} in range({inicio}, {fim} + 1):"
        return "    " * indentacao + codigo, indentacao + 1

    # For decrescente
    # MoonLang: BACKSLIDE i FROM 5 TO 1
    # Python:   for i in range(5, 1 - 1, -1):
    if linha.startswith("BACKSLIDE"):
        partes = linha.split()

        if len(partes) != 6 or partes[2] != "FROM" or partes[4] != "TO":
            raise SyntaxError(
                "Uso correto: BACKSLIDE variavel FROM inicio TO fim"
            )

        variavel = partes[1]
        inicio = traduzir_jackson5(partes[3])
        fim = traduzir_jackson5(partes[5])

        codigo = f"for {variavel} in range({inicio}, {fim} - 1, -1):"
        return "    " * indentacao + codigo, indentacao + 1

    # Condicional if
    # MoonLang: THRILLER idade >= 18
    # Python:   if idade >= 18:
    if linha.startswith("THRILLER"):
        condicao = linha.replace("THRILLER", "", 1).strip()
        condicao = traduzir_jackson5(condicao)

        if condicao == "":
            raise SyntaxError("Uso correto: THRILLER condicao")

        codigo = f"if {condicao}:"
        return "    " * indentacao + codigo, indentacao + 1

    # Condicional else
    # MoonLang: OTHERWISE
    # Python:   else:
    if linha == "OTHERWISE":
        indentacao -= 1

        if indentacao < 0:
            raise SyntaxError("OTHERWISE usado fora de um THRILLER")

        codigo = "else:"
        return "    " * indentacao + codigo, indentacao + 1

    # Finalização dos blocos
    # Esses comandos não geram linha Python.
    # Eles apenas encerram a indentação do bloco atual.
    if linha in [
        "ENDMOONWALK",
        "ENDBACKSLIDE",
        "ENDTHRILLER",
        "ENDBEAT",
    ]:
        indentacao -= 1

        if indentacao < 0:
            raise SyntaxError(f"{linha} usado sem bloco correspondente")

        return "", indentacao

    # Novo operador BILLIE
    if " BILLIE " in linha:
        comando = traduzir_jackson5(linha)
        return "    " * indentacao + comando, indentacao


    # Erro caso o comando não pertença à MoonLang
    raise SyntaxError(f"Comando desconhecido: {linha}")


def traduzir_arquivo(entrada):
    # O arquivo de entrada deve ser um programa MoonLang
    if not entrada.endswith(".moon"):
        print("Erro: o arquivo de entrada deve ter extensão .moon")
        return

    # Verifica se o arquivo informado existe
    if not os.path.exists(entrada):
        print(f"Erro: arquivo não encontrado: {entrada}")
        return

    # O arquivo Python gerado terá o mesmo nome, trocando .moon por .py
    saida = entrada.replace(".moon", ".py")

    with open(entrada, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    codigo_python = []

    # Cabeçalho colocado automaticamente no arquivo Python gerado.
    # Ele permite que o comando HEEHEE toque o áudio.
    cabecalho = '''import os

try:
    import winsound
except ImportError:
    winsound = None


def tocar_heehee():
    arquivo = "heehee.wav"

    if winsound is not None and os.path.exists(arquivo):
        winsound.PlaySound(arquivo, winsound.SND_FILENAME)
'''

    codigo_python.append(cabecalho)

    indentacao = 0

    try:
        for numero_linha, linha in enumerate(linhas, start=1):
            codigo, indentacao = traduzir_linha(linha, indentacao)

            if codigo != "":
                codigo_python.append(codigo)

        if indentacao != 0:
            raise SyntaxError("Existe algum bloco aberto sem fechamento")

    except SyntaxError as erro:
        print(f"Erro de sintaxe na linha {numero_linha}: {erro}")
        return

    with open(saida, "w", encoding="utf-8") as arquivo:
        arquivo.write("\n".join(codigo_python))

    print(f"Arquivo traduzido com sucesso: {saida}")


def monitorar_arquivo(entrada):
    """
    Observa o arquivo .moon e gera novamente o .py
    sempre que o arquivo de origem for salvo.
    """

    if not entrada.endswith(".moon"):
        print("Erro: o arquivo de entrada deve ter extensão .moon")
        return

    if not os.path.exists(entrada):
        print(f"Erro: arquivo não encontrado: {entrada}")
        return

    ultima_modificacao = None

    print(f"Monitorando alterações em: {entrada}")
    print("Sempre que você salvar o arquivo .moon, o .py será atualizado.")
    print("Pressione Ctrl + C para encerrar o monitoramento.")

    try:
        while True:
            modificacao_atual = os.path.getmtime(entrada)

            if modificacao_atual != ultima_modificacao:
                ultima_modificacao = modificacao_atual
                traduzir_arquivo(entrada)

            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nMonitoramento encerrado.")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        traduzir_arquivo(sys.argv[1])

    elif len(sys.argv) == 3 and sys.argv[2] == "--watch":
        monitorar_arquivo(sys.argv[1])

    else:
        print("Uso correto:")
        print("py tradutor_moonlang.py arquivo.moon")
        print("py tradutor_moonlang.py arquivo.moon --watch")