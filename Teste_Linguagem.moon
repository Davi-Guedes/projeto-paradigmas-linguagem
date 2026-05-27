REMIX 99 garrafas

BILLIE contador = 99

BEAT contador != 0
    THRILLER contador == 1
        SAY "{contador} garrafa"
    OTHERWISE
        SAY "{contador} garrafas"
    ENDTHRILLER

    BILLIE contador -= 1
ENDBEAT

SAY "Sem garrafas"