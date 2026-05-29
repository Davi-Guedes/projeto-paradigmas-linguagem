import os

try:
    import winsound
except ImportError:
    winsound = None


def tocar_heehee():
    arquivo = "heehee.wav"

    if winsound is not None and os.path.exists(arquivo):
        winsound.PlaySound(arquivo, winsound.SND_FILENAME)


# na linguagem eh possivel printar na tela de duas formas
# primeiro pelo HEEHEE, no qual sera acompanhado pelo grito classico do rei do pop
# segundo pelo SING, no qual sera um print normal

tocar_heehee()
print("Hello world")
print("Hello world")