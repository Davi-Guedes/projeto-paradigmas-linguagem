REMIX Teste das novas funções da MoonLang
REMIX JACKSON5 = lista
REMIX DONT_STOP = continue
REMIX BEAT_IT = break

BILLIE import time

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

BILLIE time.sleep(3)

HEEHEE "Fim do teste!"