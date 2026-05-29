REMIX Sistema de Treinamento de Dobras do Avatar
HEEHEE "Iniciando o treinamento do Avatar Aang!"

dobras BILLIE JACKSON5["Agua", "Terra", "Fogo", "Ar", "Energia"]

SING "O Avatar esta dominando os elementos da lista..."

MOONWALK i FROM 0 TO 4
    THRILLER dobras[i] WHOS_BAD "Fogo"
        SING "Alerta: Ataque da Nacao do Fogo! O treinamento foi interrompido."
        BEAT_IT
    ENDTHRILLER
    
    THRILLER dobras[i] WHOS_BAD "Terra"
        SING "Dobra de Terra dominada! Toph ficaria orgulhosa."
        DONT_STOP
    ENDTHRILLER
    
    SING "Elemento dominado com sucesso: {dobras[i]}"
ENDMOONWALK

HEEHEE "Fim do treinamento de hoje. Appa, Yip Yip!"