# ESB draft Fair Wob dossiers

___
* marx
* 2022-04-28

_________

## Titel: WOB dossiers voldoen niet aan FAIR data principes

*Maik Larooij, Maarten de Rijke, Jaap Kamps, Maarten Marx*


Recent onderzoek van Openstate [REF] keek naar de *tijd* die nodig is om een Wob besluit te nemen, en maakte een schatting van de kosten per pagina. 
Wij kijken hier naar de *kwaliteit* van de gepubliceerde Wob besluiten, inclusief de vrijgegeven documenten.
We kijken bewust niet naar de inhoud van de stukken en dus niet naar de vraag of de informatiebehoefte gesteld in het Wob verzoek wel adequaat is beantwoord. De kwaliteit wordt beoordeeld op basis van de 4 FAIR principes van open data en  voor overheidsinformatie in het bijzonder. Deze zeggen dat data vindbaar, archiveerbaar, uitwisselbaar en herbruikbaar moet zijn.

**TODO: Waarom past dit in ESB?** Paragraaf economie, verwijs naar EU daytasct Feb 22.

We willen dus de volgende onderzoeksvraag beantwoorden:

>Hoe staat het met de *FAIRness* van de door de Nederlandse overheid gepubliceerde Wob dossiers?
 
We zullen zien dat dat niet best gesteld is, maar we laten ook zien dat deze situatie heel eenvoudig, tegen vrijwel nihile kosten, en met een enorm potentieel aan opbrengsten omgedraaid kan worden.

De 4 principes zijn nogal abstract en niet eenvoudig te operationaliseren. Daarom beantwoorden we de vraag via een gedachtenexperiment. We stellen ons voor dat we een zoekmachine, een gespecialiseerde Google, voor Wob dossiers gaan maken. 
Vanzelfsprekend spelen de 4 principes dan een grote rol. 
Om de werking concreet te maken geven we een voorbeeld.

Stel een gebruiker wil de exacte zin hebben die Minister de Jonge schreef over Sywert van Lienden en plassen in de tent. Na een zoekvraag "sywert inside" hoop zij dan een antwoord te krijgen op de volgende Google-achtige manier: [bron](https://www.volkskrant.nl/kijkverder/v/2022/hoe-hugo-de-jonge-zich-actief-bemoeide-met-de-mondkapjesdeal-van-sywert-van-lienden~v497075/)

<pre>
Onderdeel van: [WOB verzoek Volkskrant Mei 2021, mondkapjesdeal, Min. Financien.](url) 
Whatsapp bericht
afzender: Hugo de Jonge
datum: 2020-04-12


*Je kunt die Sywert beter inside pissing out hebben dan outside pissing in. Met een klein beetje verdraagzaamheid moet dat lukken. Hoop echt dat het lukt.*
</pre>



#### Een zoekmachine voor Wob dossiers
De Wob dossiers worden steeds beter beschikbaar gemaakt, zeker door de centrale overheid, dus we kunnen aannemen dat we die allemaal netjes hebben.  Om een zoekmachine te maken moeten die dossiers wel aan de volgende 3 basisvoorwaarden voldoen:

1. *De logische informatie-eenheid komt overeen met de technische bestandseenheid.* Google leidt je naar een Wikipedia pagina, net naar de hele Wikipedia. Als je verwijst naar een citaat uit de Bijbel, doe je dat zo precies mogelijk. Het technische formaat van Wikipedia, elk lemma is een eigen HTML pagina, en van de Bijbel, elke zin heeft een unieke code vergelijkbaar met een URL, maakt dit mogelijk.
2. *De woorden in de documenten zijn als woorden leesbaar door een computer.* Een situatie waarin dit niet het geval is is wanneer men met Control F zoekt naar een woord in een PDF file en niks vindt terwijl dat woord toch duidelijk op het scherm staat.
3. *Per informatiedrager is een zekere minimale hoeveelheid metadata aanwezig.* Documenten vindbaar op Google hebben een titel, meestal een datum, een adres (de URL) en nog veel meer metadata die de zoekmachine gebruikt.

We gaan deze voorwaarden nu stuk voor stuk langs.

1. *Vrijgegeven Wob documenten voldoen in overgrote meerderheid niet aan de eerste voorwaarde.* De essentie van een Wob verzoek is dat het vraagt om de *documenten* over een bepaald onderwerp. Het Wob dossier bestaat in de regel uit 3 *PDF files*, het besluit, de inventarislijst, en een PDF met daarin alle vrijgegeven documenten achter elkaar geplakt, zonder voor de computer leesbare grenzen. Alle door openstate bekeken Wob dossiers hebben deze vorm, en vrijwel ook alle dossiers vindbaar op het web die gepubliceerd zijn door lagere overheden. De gemeente Amsterdam en de provincie Gelderland vormen twee uitzonderingen. Zij plaatsen de verzameling documenten op een heel logische wijze in een zip bestand.
2. Veel van de Wob documenten zijn *scans* van een print. De meeste scanners staan standaard zo ingesteld dat ze *optische karakter herkenning* toepassen en niet alleen een foto maken maar de tekst ook voor een computer leesbaar maken. Bij de wob documenten gaat dit heel vaak net goed.
**Data tabellen van Maik. Over opentate corpus en over wobcovid corpus.**
3. De boven genoemde inventarislijst die bij bijna elke Wob dossier zit is een tabel of spreadsheet met op elke rij een document, en per kolom specifieke  metadata zoals de titel, het soort document (mail, whatsappje, kamerstuk, etc), hoe het is vrijgegeven, etc, etc. Dit klinkt ideaal, en dat zou het ook zijn als 1) die inventarislijsten als een excel of csv bestand werden vrijgegeven en niet als een uitgeprinte en weer ingescande tabel, en 2) waarbij elke Wob producent consequent dezelfde namen voor de kolommen zou gebruiken, en ook consequent is in het benoemen van de waardes in de cellen, en 3) als alle Wob producenten dat zo ongeveer zo'n beetje op dezelfde manier zouden doen. Jammer genoeg is dat niet het geval. **data van maik**


Dit gedachtenexperiment laat zien dat het opzeten van zo'n zoekmachine, waarmee we de Wob dossiers dus op een uniforme wijze *archiveren*, *vindbaar* maken, en daardoor *herbruikbaar* en via hun metadata *uitwisselbaar* een enorm lastig karwei is, puur omdat de data op zo'n onhandige manier wordt aangeleverd.
Gelukkig kan het ook anders.

#### Hoe Wob dossiers FAIR te maken?

Het lijkt erop dat Wob ambtenaren hun Wob dossiers prachtig FAIR op hun eigen schijf hebben staan, maar dat er in de laatste publicatiestap iets misgaat. Want wat is er nou eigenlijk nodig om die dossiers FAIR te publiceren? De documenten *digitaal*  (en dus machine leesbaar) in een (zip) mapje, en de metadata op een uniforme wijze in een spreadsheet, liefst met hyperlinks naar de losse documenten. 

Het lastigste hier is dat er heel veel Wob ambtenaren zijn met ieder hun eigen werkwijze. Dus die uniforme metadata zijn een coordinatieprobleem. Wij hebben dat simpel opgelost door  gratis software waarmee men heel handig een Wob dossier opbouwt en automatisch uniform en FAIR publiceert. **screenshot allicht**
Wob ambtenaren gebruiken al software voor hun dossiers, vooral om semi-automatisch persoonsgegevens te herkennen en die zwart te lakken. Het is niet nodig om hiervoor documenten te printen en in te scannen.

#### Wat zijn de opbrengsten?

De kosten om de dossiers FAIR te publiceren zijn verwaarloosbaar. De opbrengsten kunnen erg hoog zijn. 
Berenschot adviseert om Wob documenten netjes op te slaan en voor de Wob ambtenaar vindbaar te maken zodat ze *herbruikbaar* zijn voor een nieuw Wob verzoek (en dus niet weer opnieuw geanonimiseerd hoeven te worden). **REF, MAIK heb jij die nog?** Prachtig natuurlijk, maar de winst lijkt in het niet te vallen bij de winst die te behalen is als *burgers eenvoudig en goed in gepubliceerde Wob dossiers kunnen zoeken* en hun vraag beantwoord zien zonder hem (opnieuw) te hoeven stellen. 

Daarnaast kunnen onderzoekscollectieven  als *Follow The MOney* een hoop geld en vooral frustratie  *besparen*. Zij zijn een groot deel van hun tijd kwijt met het *reverse-engineeren* van de Wob dossiers, waarbij precies de 3 bovengenoemde voorwaarden het struikelblok vormen voor het opbouwen net een net digitaal dossier door zo'n journalist of collectief. 

Tenslotte zijn de opbrengsten van open data en standaarden in potentie immens, zoals ook aangestipt in de EU Data Act. Denk maar eens aan het open email protocol SMTP, dat ervoor zorgt dat   emails verstuurd vanuit elke provider keurig aankomen bij welke provider dan ook. Via het *prefential attachment* effect zorgt het open maken van data en kennis ook voor verdere uniformering en daarmee uitwissel- en herbruik-baarheid, iets dat we nu zien bij de open Kennis Graaf versies (WikiData, DBPedia) van Wikipedia. 


**TODO: samenvattende zin/uitsmijter**

