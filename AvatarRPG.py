import os

try:
    import winsound
except ImportError:
    winsound = None


def tocar_heehee():
    arquivo = "heehee.wav"

    if winsound is not None and os.path.exists(arquivo):
        winsound.PlaySound(arquivo, winsound.SND_FILENAME)

# Sistema de Treinamento de Dobras do Avatar
tocar_heehee()
print("Iniciando o treinamento do Avatar Aang!")
dobras = ["Agua", "Terra", "Fogo", "Ar", "Energia"]
print("O Avatar esta dominando os elementos da lista...")
for i in range(0, 4 + 1):
    if dobras[i] == "Fogo":
        print("Alerta: Ataque da Nacao do Fogo! O treinamento foi interrompido.")
        break
    if dobras[i] == "Terra":
        print("Dobra de Terra dominada! Toph ficaria orgulhosa.")
        continue
    print(f"Elemento dominado com sucesso: {dobras[i]}")
tocar_heehee()
print("Fim do treinamento de hoje. Appa, Yip Yip!")