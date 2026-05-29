# MoonLang🕺

MoonLang é uma linguagem de programação esotérica criada como projeto acadêmico da disciplina de Paradigmas de Programação do curso de Engenharia da Computação da Universidade Federal do Ceará.

A proposta da linguagem é transformar estruturas tradicionais de programação em comandos temáticos inspirados no universo artístico de Michael Jackson. Dessa forma, conceitos como variáveis, condicionais, laços de repetição, listas, comentários e comandos de controle de fluxo são representados por palavras relacionadas ao cantor, suas músicas, danças e expressões marcantes.

O projeto funciona como um tradutor de MoonLang para Python. Ou seja, o programador escreve um arquivo com extensão `.moon`, utilizando a sintaxe própria da MoonLang, e o interpretador/tradutor converte esse código para um arquivo `.py`, que pode ser executado normalmente pelo Python.

---

## Pré-requisitos

* Python 3 instalado.
* Nenhuma biblioteca externa é necessária.
* O áudio `heehee.wav` é opcional.
* Observação: o áudio usa `winsound`, então o som funciona principalmente no Windows. Em outros sistemas, o programa continua executando normalmente, mas pode não tocar o arquivo `.wav`.

---

## Ideia do projeto

O objetivo principal do trabalho é criar uma linguagem esotérica simples, criativa e funcional, utilizando como base os conceitos estudados em paradigmas de programação.

A MoonLang não busca ser uma linguagem de uso comercial ou profissional. Seu foco é didático e experimental, mostrando como uma linguagem pode possuir:

* palavras reservadas próprias;
* sintaxe personalizada;
* estruturas de decisão;
* estruturas de repetição;
* comandos de entrada e saída;
* listas;
* comandos de controle de fluxo;
* tradução para outra linguagem de programação.

O tema escolhido foi Michael Jackson, pois ele possui um universo visual e musical muito marcante. Termos como `MOONWALK`, `THRILLER`, `HEEHEE`, `BEAT_IT`, `DONT_STOP` e `JACKSON5` foram utilizados para representar estruturas conhecidas da programação de uma forma mais divertida e temática.

---

## Como a MoonLang funciona

A MoonLang utiliza arquivos com a extensão:

```text
.moon
```

O código escrito em MoonLang é lido pelo arquivo tradutor:

```text
tradutor_moonlang.py
```

Esse tradutor analisa cada linha do arquivo `.moon` e gera um arquivo Python equivalente, com extensão `.py`.

Por exemplo, um código MoonLang como:

```moon
SING "Olá, mundo!"
```

é traduzido para Python como:

```python
print("Olá, mundo!")
```

---

## Como executar um programa MoonLang

Primeiro, escreva seu programa em um arquivo `.moon`.

Exemplo:

```text
Teste_Linguagem.moon
```

Depois, execute o tradutor no terminal:

```bash
python tradutor_moonlang.py Teste_Linguagem.moon
```

Esse comando irá gerar um arquivo Python com o mesmo nome:

```text
Teste_Linguagem.py
```

Em seguida, execute o arquivo Python gerado:

```bash
python Teste_Linguagem.py
```

---

## Modo de monitoramento

O tradutor também possui um modo de monitoramento. Nesse modo, sempre que o arquivo `.moon` for salvo, o arquivo `.py` será gerado novamente automaticamente.

Para usar:

```bash
python tradutor_moonlang.py Teste_Linguagem.moon --watch
```

Esse modo é útil durante o desenvolvimento, pois permite editar o código MoonLang e atualizar automaticamente sua versão em Python.

---

## Tabela de comandos da MoonLang

| Comando MoonLang | Tradução para Python     | Função                                                         |
| ---------------- | ------------------------ | -------------------------------------------------------------- |
| `REMIX`          | `#`                      | Cria um comentário no código                                   |
| `SING`            | `print()`                | Imprime uma mensagem ou valor no terminal                      |
| `HEEHEE`         | `tocar_heehee()`         | Toca o áudio `heehee.wav` e pode imprimir uma mensagem         |
| `BILLIE`         | Comando Python direto    | Cria variáveis, atribuições ou executa comandos simples        |
| `BEAT`           | `while`                  | Cria um laço de repetição enquanto uma condição for verdadeira |
| `MOONWALK`       | `for` crescente          | Cria um laço de repetição crescente                            |
| `BACKSLIDE`      | `for` decrescente        | Cria um laço de repetição decrescente                          |
| `THRILLER`       | `if`                     | Cria uma estrutura condicional                                 |
| `OTHERWISE`      | `else`                   | Cria o bloco alternativo de uma condição                       |
| `JACKSON5[...]`  | `[...]`                  | Cria uma lista                                                 |
| `DONT_STOP`      | `continue`               | Pula a repetição atual e continua o laço                       |
| `BEAT_IT`        | `break`                  | Encerra o laço imediatamente                                   |
| `ENDMOONWALK`    | Fim do bloco `MOONWALK`  | Fecha um laço crescente                                        |
| `ENDBACKSLIDE`   | Fim do bloco `BACKSLIDE` | Fecha um laço decrescente                                      |
| `ENDTHRILLER`    | Fim do bloco `THRILLER`  | Fecha uma estrutura condicional                                |
| `ENDBEAT`        | Fim do bloco `BEAT`      | Fecha um laço `while`                                          |

---

## Exemplo completo em MoonLang

```moon
REMIX Teste das novas funções da MoonLang
REMIX JACKSON5 = lista
REMIX DONT_STOP = continue
REMIX BEAT_IT = break

HEEHEE "Iniciando o show da MoonLang!"

BILLIE integrantes = JACKSON5["Michael", "Janet", "Tito", "Jermaine", "Jackie"]

SING "Lista completa dos integrantes:"
SING integrantes

SING "Agora vamos chamar os integrantes para o palco..."

MOONWALK i FROM 0 TO 4

    THRILLER integrantes[i] == "Tito"
        SING "Tito foi pulado com DONT_STOP."
        DONT_STOP
    ENDTHRILLER

    THRILLER integrantes[i] == "Jermaine"
        SING "Jermaine apareceu. Encerrando o show com BEAT_IT."
        BEAT_IT
    ENDTHRILLER

    SING "No palco agora: {integrantes[i]}"

ENDMOONWALK

HEEHEE "Fim do teste!"
```

---

## Código Python gerado

O código acima é traduzido para Python da seguinte forma:

```python
import os

try:
    import winsound
except ImportError:
    winsound = None


def tocar_heehee():
    arquivo = "heehee.wav"

    if winsound is not None and os.path.exists(arquivo):
        winsound.PlaySound(arquivo, winsound.SND_FILENAME)


# Teste das novas funções da MoonLang
# JACKSON5 = lista
# DONT_STOP = continue
# BEAT_IT = break

tocar_heehee()
print("Iniciando o show da MoonLang!")

integrantes = ["Michael", "Janet", "Tito", "Jermaine", "Jackie"]

print("Lista completa dos integrantes:")
print(integrantes)

print("Agora vamos chamar os integrantes para o palco...")

for i in range(0, 4 + 1):

    if integrantes[i] == "Tito":
        print("Tito foi pulado com DONT_STOP.")
        continue

    if integrantes[i] == "Jermaine":
        print("Jermaine apareceu. Encerrando o show com BEAT_IT.")
        break

    print(f"No palco agora: {integrantes[i]}")

tocar_heehee()
print("Fim do teste!")
```

---

## Saída esperada

Ao executar o arquivo Python gerado, a saída esperada é:

```text
Iniciando o show da MoonLang!
Lista completa dos integrantes:
['Michael', 'Janet', 'Tito', 'Jermaine', 'Jackie']
Agora vamos chamar os integrantes para o palco...
No palco agora: Michael
No palco agora: Janet
Tito foi pulado com DONT_STOP.
Jermaine apareceu. Encerrando o show com BEAT_IT.
Fim do teste!
```

Além disso, o comando `HEEHEE` tenta tocar o arquivo `heehee.wav`, caso ele esteja presente na mesma pasta do projeto.

---

## Estrutura básica do projeto

```text
projeto-paradigmas-linguagem/
│
├── tradutor_moonlang.py
├── Teste_Linguagem.moon
├── Teste_Linguagem.py
├── heehee.wav
└── README.md
```

## Observações importantes

A MoonLang não deve ser executada diretamente pelo Python.

Ou seja, o comando abaixo está incorreto:

```bash
python Teste_Linguagem.moon
```

O correto é primeiro traduzir:

```bash
python tradutor_moonlang.py Teste_Linguagem.moon
```

E depois executar o Python gerado:

```bash
python Teste_Linguagem.py
```

Caso o arquivo `.moon` seja executado diretamente, o Python apresentará erro de sintaxe, pois comandos como `REMIX`, `SING`, `MOONWALK` e `THRILLER` pertencem à MoonLang, não ao Python.

---

## Autores

ANTONIO MATHEUS DA COSTA QUEIROZ - 565556
AUGUSTO RODRIGUES PAZ GREGORIO - 565690
DAVI GOMES ROCHA - 564686
DAVI MOURA GUEDES - 568251
JHENNIFER KAROLAYNE NASCIMENTO DA PENHA - 567369
MARCELO HENRIQUE TEIXEIRA DE SOUZA ALVES - 571393

Projeto desenvolvido para a disciplina de Paradigmas de Programação.

Tema da linguagem: Michael Jackson.

Nome da linguagem: MoonLang.
