REMIX Brincadeira das 99 garrafas de cerveja
REMIX Exemplo usando BACKSLIDE, THRILLER, OTHERWISE e SING

HEEHEE "Começando a brincadeira das 99 garrafas!"
SING ""

BACKSLIDE garrafas FROM 99 TO 1
    THRILLER garrafas == 1
        SING "{garrafas} garrafa de cerveja na parede, {garrafas} garrafa de cerveja."
        SING "Pegue uma e passe adiante, nenhuma garrafa de cerveja na parede."
    OTHERWISE
        SING "{garrafas} garrafas de cerveja na parede, {garrafas} garrafas de cerveja."
        BILLIE restantes = garrafas - 1

        THRILLER restantes == 1
            SING "Pegue uma e passe adiante, {restantes} garrafa de cerveja na parede."
        OTHERWISE
            SING "Pegue uma e passe adiante, {restantes} garrafas de cerveja na parede."
        ENDTHRILLER
    ENDTHRILLER

    SING ""
ENDBACKSLIDE

SING "Nenhuma garrafa de cerveja na parede, nenhuma garrafa de cerveja."
SING "Vá ao mercado comprar mais, 99 garrafas de cerveja na parede!"
HEEHEE "Fim da brincadeira!"
