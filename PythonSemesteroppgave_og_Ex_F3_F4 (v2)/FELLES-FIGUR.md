# Felles prisfigur

Start skrivebordsprogrammet med `python Semester26.py`. Det åpner det vanlige
Matplotlib-vinduet med boligvalg, pris per m², stolpediagram og klikkbart kart.

Endre stolpefarger, arealene i diagrammet, gjennomsnittslinjen eller kartmerket i
`prisfigur.py`. `Semester26.py` bestemmer hvordan kontrollene og aksene plasseres
i skrivebordsvinduet, og håndterer museklikk og valg. `Semester26_Model.py` trener
prismodellen og beregner prisen.

## Hva er forskjellen fra den tidligste skolekoden i dette repoet?

- **`6374a84`** hadde allerede boligvalg, klikkbart kart og stolper for
  50, 100, 150 og 200 m². Stolpene og kartmarkøren var blå.
- **`ea23cb2` og `0cfec9b`** hadde allerede oppdatert kartet, lagt til
  standardfarger og endret presentasjonen. Versjonen rett før denne endringen
  hadde rød sirkel med hvit kant, stiplet gjennomsnittslinje og en egen
  prisetikett. Den sammenlignet også polynomgrad 1, 2 og 3 på valideringsdata.
- **Denne endringen** flytter kode for pris per m², diagram og kart til
  `prisfigur.py`. Skrivebordsprogrammet bruker den modulen med samme utseende
  og samme kontroller som før. Modell, øvingsdata og kartfil er uendret.

Den separate nettsideprototypen bruker samme figurmodul til å lage et PNG-bilde
på serveren. På nettsiden sender HTML-skjemaet valg og kartkoordinater til
Python. Denne repoendringen gjør modulen tilgjengelig for begge bruksområder.
Nettsideprototypen må kobles til den separat.

I Gruppe blir `Semester26.py` og `Semester26_Model.py` vist som
`prisberegner.py` og `prismodell.py`. Git-synken justerer modellimporten og
beholder navnet `prisfigur.py`.
