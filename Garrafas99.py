import os

try:
    import winsound
except ImportError:
    winsound = None


def tocar_heehee():
    arquivo = "heehee.wav"

    if winsound is not None and os.path.exists(arquivo):
        winsound.PlaySound(arquivo, winsound.SND_FILENAME)

# Brincadeira das 99 garrafas de cerveja
# Exemplo usando BACKSLIDE, THRILLER, OTHERWISE, BILLIE, WHOS_BAD, RUSBE e SING
tocar_heehee()
print("Começando a brincadeira das 99 garrafas!")
print("")
for garrafas in range(99, 1 - 1, -1):
    if garrafas == 1:
        print(f"{garrafas} garrafa de cerveja na parede, {garrafas} garrafa de cerveja.")
        print("Pegue uma e passe adiante, nenhuma garrafa de cerveja na parede.")
    else:
        print(f"{garrafas} garrafas de cerveja na parede, {garrafas} garrafas de cerveja.")
        restantes = garrafas - 1
        if restantes == 1:
            print(f"Pegue uma e passe adiante, {restantes} garrafa de cerveja na parede.")
        else:
            print(f"Pegue uma e passe adiante, {restantes} garrafas de cerveja na parede.")
    print("")
print("Nenhuma garrafa de cerveja na parede, nenhuma garrafa de cerveja.")
print("Vá ao mercado comprar mais, 99 garrafas de cerveja na parede!")
tocar_heehee()
print("Fim da brincadeira!")