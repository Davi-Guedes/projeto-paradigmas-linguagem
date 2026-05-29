import os
import time

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

time.sleep(0.7)

tocar_heehee()
print("Fim do teste!")