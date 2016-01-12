Met GameCards.exe kun je zoveel spelkaarten maken als je wilt. De output is op dit moment nog een simpel txt-bestand.
Verder is het programma vrijwel generiek, dus bijna alle eigenschappen van de kaarten zijn heel makkelijk te wijzigen.
Er worden je een aantal vragen gesteld als je de applicatie draait. De meesten spreken voor zich, de anderen zal ik
hieronder uitleggen:

1. Welk type kaarten, karakter- ("character") of kraak- ("vault") kaarten
2. Hoeveel
3. Tussen welke waardes je de attributen van de kaarten wilt hebben. 
	De hoogte van de attributen zal dan per level kaarten verschillen (hierbij wordt uitgegaan van drie levels). 
	Voorbeeld: ik voer in 1 10. Dan krijgen de kaarten de volgende waardes:
	Level 1 kaarten: tussen 0 en 4
	Level 2 kaarten: tussen 3 en 8
	Level 3 kaarten: tussen 7 en 11
4. Wat is de cost/reward factor?
	Deze factor bepaalt met hoeveel de attributenhoogte vermenigvuldigd wordt om het loon (in het geval van karakters)
	of de buit (in het geval van kraakkaarten) te bepalen. In het voorbeelddocument heb ik een factor van 200 gebruikt
	voor loon en 300 voor de buit.
5. Wat is de noise factor?
	Dit geeft aan hoeveel het loon of de buit kan afwijken van de standaard vermenigvuldiging. Een noise van 100 
	betekent dus een maximale afwijking van 100.