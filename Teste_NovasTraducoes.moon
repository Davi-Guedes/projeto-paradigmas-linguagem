REMIX Teste das novas funções da MoonLang
REMIX JACKSON5 = lista
REMIX DONT_STOP = continue
REMIX BEAT_IT = break

HEEHEE "Iniciando o show da MoonLang!"

BILLIE integrantes = JACKSON5["Michael", "Janet", "Tito", "Jermaine", "Jackie"]

SAY "Lista completa dos integrantes:"
SAY integrantes

SAY "Agora vamos chamar os integrantes para o palco..."

MOONWALK i FROM 0 TO 4

    THRILLER integrantes[i] == "Tito"
        SAY "Tito foi pulado com DONT_STOP."
        DONT_STOP
    ENDTHRILLER

    THRILLER integrantes[i] == "Jermaine"
        SAY "Jermaine apareceu. Encerrando o show com BEAT_IT."
        BEAT_IT
    ENDTHRILLER

    SAY "No palco agora: {integrantes[i]}"

ENDMOONWALK

HEEHEE "Fim do teste!"

