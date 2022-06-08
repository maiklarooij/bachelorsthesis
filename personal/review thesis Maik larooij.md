# review thesis Maik larooij

___

* marx
* 2022-06-08
* draft versie 6 Juni
___

* Sterke introductie die het onderwerp wob/woo goed introduceert en ook al de problemen ermee goed, en goed gedocumenteerd aanstipt. Mooi en logisch uitmondend in 3 goede onderzoeksvragen. Dit is echt heel sterke informatiekunde.
* Heldere indeling met 2 goede achtergrond en methoden secties voordat we heel goed gestructureerd aan de 3 vragen in 3 hoofdstukken beginnen.
* probleem analyse/hfd 4. Heel sterk met dit simpele voorbeeld uitgewerkt. Verdere aanpak om de problemnen op te lossen ook goed gestructuteerd.
* Hfd 5 is helder, sterk, en goed gemotiveerd en netjes in json en met die schema taal uitgewerkt. Goed ook de provenance van alle attributen uit het schema. 
* Hfd 6 behoeft nog wat opschoning
* Conclsusie en discussie in orde.

### Tips voor maik

1. Hoofdletters in je referenties gaan niet goed. Makkelijk op te lossen door {} om de text te zetten.
2. Niet alle citaties zijn klikbaar lijn 171 bijv. Links naar figuren ook niet l202-203, ook niet bij l223 sectie verwijzingen. Dit is toch niet hardcoded? `\ref` en `\label` heerlijk!
3. Gebruik je wel de figure environment? Doen hoor. Zorg dat Fig 2.4.1 bovenaaan de pagina komt met `[t]`. Op at probleem 2 lijkt bij het figgur te horen, of je verliest het. 
4. Ik mis in Fig 2.4.1 eigenlijk de stap van het FAIR maken van data.  Je zou de stap 5 nu met stap 4 kunnen samenvoegn, en dan van stap 5 het fair maken van al bestaande of nieuwe data kunnen maken. Of is dit iets uit de literatuur?  Sowieso moety je dat allicht in de caption aangeven (iets als "op basis van [cite]")
   * Maar misschien bedoel je dit wel expliciet zo, en komt  dat pas in of na stap 8. Ik zou dat dan wel noemen! In stap 6 zit dan hopelijk het maken van (een paar) voorbeelden (zopals jij met je zonneweide gedaan hebt).
* Hfd 4 probleem 1: ik zou je mooie tabel met "bewijs" obvefr de slechtheid er allicht nog inzetten hoor. Het was toch een hoop werk, nu sneeuw dat wat omnder.
* Tabel 4.1.1 2 sterretjes gaan mis. Ik zou die percentages zonder getal achter de komma geven. 


### 4.1

Ik raakte wat in de war. Ik stekl voor om vlak voor Probleem 1, de 3 gevonden problemen op te sommen, en te zeggen dat je die gevonden hebt. En dan echt met een subsubsection ze te behandelen. 

begin dabn telkens duidelijk met de informatiebehoefte, zoals je bij Probleem 1 doet. Bij probleem 2 vond ik dfat al een stuk onduidelijker. 

Probleem 2: 
* Noem de informatiebehoefte, en dan de "zoekstrategie" waarbij de zoeker dit in de inventarislijsten gaat opzoeken. 
* Die zoekstrategie doe jij dan eigenlijk zo goed en zo kwaad als het kan na.
* l359 "ambigu" is niet het juiste woord:  vervang door \emph{niet eenduidig, consequent en gestandaardiseerd. Het is dus vaak gissen wat er bedoelt wordt.} 
* l363 toegankelijk --> mogelijk
* l375 "te herkennen" kan weg lijkt me. Maar waarom dan niet gewoon "Identieke informatie wordt niet op dezelfde  wijze weergegeven."
* 378-382: weer gewoon op de eerdere manier. Stel een jurist wil uitzoeken welke weigereingsgronden hoe vaak ingezet worden.
* l398-405 Maak een nieuw kopje Conclusies. Dit si heel sterk! 
* "niet doorzoekbare pdf formaat" ??? je bedoelt volgens mij dat er geen woorden in staan, of dat niet alle woorden die in de oorspronkelijke documenten staan ook machine leesbaar zijn.


## hfd 5

* l439 *kennisrepresentatie* haal kennis weg 
* l445 "hoeven" misschien ipv kunnen
* * l461-463 kan weg. Beter "De vorm van de wob dossiers kan het best gevat worden in een semi gestruvtureerd data fomaat."
* Ik heb Peter Buneman heel vaak ontmoet. Echt een geweldige kerel. Zo'n echte heel nette Engelsman. 
* l514-516 dit heet wel het FTM schema maar is NIET door "onze FTM" ontwikkeld. 
* Ik mis eigenlijk hier de weigeringsgronden, omdat dat voorbeeld zo in je hoofd blijft zitten. 
* Ik zou afsluiten met een verwijzing naar het hele schema in de appendix.  
* Tabel 5.3.1 is toch niet volledig??? Ik mis veel attributen met heldere waardes zoals bodyText dat een string moet zijn, en weigeringsgronden.

## Hfd 6

* tabel 6.1 "die de doorzoekbaarheid verhoogt." --> die de machine lees- en interpreteerbaar-heid waarborgt.
* Tabel 6.1. Ik vind dit eigenlijk een onvoldoende evaluatie. De tabel is wel waar, maar erg onvolledig en dart zal zo blijven.
* Ik denk dat je hier juist je zonneweide voorbeeld kan doen en dat als evaluatie opvoeren. Dat het dus **kan** en **lukt** en eigenlijk **helemaal niet moeijlijk of veel extra werk is** , is jouw evaluatie.
* Daarnaast kan je prima in een bullet list de laatste kolom van Tabel 6.1 noemen. Maar per FAIR principe heb je vaak meer gedaan dan je aangeeft. Probeer alle dingen die je gedaan hebt onder 1 of meerdre van de FAIR kopjes te zetten.
* Overigens mis ik eigenlijk wel wat uitgebreiders over de OCR/ongescanned. Ik denk dat je hier best een regel kunt opstellen die zegt dat het bodytext attribuut (of hoe het ook heet) alle woorden bevat (in de gebruikelijke leesvolgorde) die in het document voorkomen. 
    * En dan kan je in een voetnoot wat gaan mieren dat dit lastig te checken is, en niet formeel in de JSON schema is op te voeren, maar dit is wel cruciaal. 
    * Zeg dan ook dat je dit attribuut direct kan  gebruiken om een zoekindex en Google achtig zoeksysteem te maken (eigenlijk zonder de PDFs nog te hoeven bekijken).
    * Je kan aangeven dat dit attribuut in de woofairify tool wordt ingevuld door "de tekst uit de PDF te halen, vergelijkbaar met Control A, Control C, Control V. Een echte volledige automatische formele check van de eis is natuurlijk niet mogelijk. 
* l703, ik zou meteen een hyperlink naar het voorbeeld op het web geven.
* l725, en dus ook bodyText! 
* De links tussen 6.3.1 en 6.3.2 kloppen al niet, dus dat is wel heel beschamend! 
* De identifiers zijn vast niet uniek, de filenamen komen niet overeen.
* Ik denk dat je in je tool moet zprgen voor een **klikbare** csv/inventarislijst, zodat de PDF uit de uitgepakte zipmap opent. 
* l770 "van de mappen en documenten"
