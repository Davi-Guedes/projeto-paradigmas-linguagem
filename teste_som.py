import os
import winsound

print("Testando som...")

if os.path.exists("heehee.wav"):
    print("Arquivo encontrado!")
    winsound.PlaySound("heehee.wav", winsound.SND_FILENAME)
    print("Som tocado!")
else:
    print("Arquivo heehee.wav não encontrado.")

    # matheus é viado