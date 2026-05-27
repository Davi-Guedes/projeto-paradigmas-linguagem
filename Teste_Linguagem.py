import os

try:
    import winsound
except ImportError:
    winsound = None


def tocar_heehee():
    arquivo = "heehee.wav"

    if winsound is not None and os.path.exists(arquivo):
        winsound.PlaySound(arquivo, winsound.SND_FILENAME)

# 99 garrafas
contador = 99
while contador != 0:
    if contador == 1:
        print(f"{contador} garrafa")
    else:
        print(f"{contador} garrafas")
    contador -= 1
print("Sem garrafas")