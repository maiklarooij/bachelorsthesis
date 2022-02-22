# Anatomie

Hoe representeren we een Wob-verzoek? Wat willen we opslaan?

## Geheel Wob-verzoek


| Veld               | Type    | Verplicht? | Omschrijving                                              | Voorbeeld                                                                                                                                  |
|--------------------|---------|------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ID                 | int     | Ja         | Uniek ID                                                  | 3928                                                                                                                                       |
| Titel              | str     | Ja         | Titel Wob-verzoek                                         | Besluit op Wob-verzoeken over samenwerkingsovereenkomsten Nederlandse overheid en het World Economic Forum (WOF)                           |
| Verantwoordelijken | str     | Ja         | Verantwoordelijke voor het behandelen van het Wob-verzoek | Ministerie van Buitenlandse Zaken                                                                                                          |
| Indiendatum        | date    | Ja         | Datum van indienen Wob-verzoek                            | 22-12-2021                                                                                                                                 |
| Besluitdatum       | date    | Ja         | Datum van reactie/besluit Wob-verzoek                     | 02-02-2022                                                                                                                                 |
| Beschrijving       | str     | Nee        | Beschrijving Wob-verzoek                                  | Besluit op een verzoek om informatie over de samenwerkingsovereenkomsten tussen de Nederlandse overheid en het World Economic Forum (WEF). |
| Intern volgnummer  | str/int | Nee        | Volgnummer voor intern gebruik                            | BUZA-129                                                                                                                                   |
| Verzoeker          | str     | Nee        | Naam verzoeker                                            | Follow the Money                                                                                                                           |
| Geografisch gebied | str     | Nee        | Naam geografisch gebied                                   | Den Haag                                                                                                                                   |
| BAG ID             | int     | Nee        | Basisregistratie Adressen en Gebouwen ID                  | 2389120312367                                                                                                                              |
| BGT ID             | int     | Nee        | Basisregistratie Grootschalige Topografie ID              | 3243134                                                                                                                                    |
| Longitude          | float   | Nee        | Oost-west positie                                         | 103.800670                                                                                                                                 |
| Latitude           | float   | Nee        | Noord-zuid positie                                        | 1.320660                                                                                                                                   |
| Postcodegebied     | str     | Nee        | Postcodenummers                                           | 3825                                                                                                                                       |

### Besluit document (verplicht)

| Veld              | Type | Verplicht? | Omschrijving                                                                         | Voorbeeld                                                                                                                                                                                                                                                                   |
|-------------------|------|------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Documentnummer    | int  | Ja         | Documentnummer van verzoek                                                           | 1                                                                                                                                                                                                                                                                           |
| Bestandsnaam      | str  | Ja         | Bestandsnaam besluitdocument                                                         | Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf                                                                                                                                                                                                        |
| Link naar bestand | str  | Ja         | Link naar bestand besluitsdocument                                                   | https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf |
| Beoordeling           | str  | Ja         | Besluit gehele Wob-verzoek (openbaar, deels openbaar, niet openbaar, reeds openbaar) | Deels openbaar                                                                                                                                                                                                                                                              |
| Verdaagd          | str  | Ja         | 'Ja' als besluit is verdaagd, 'Nee' als dit niet het geval is                        | Nee                                                                                                                                                                                                                                                                         |

### Inventaris document (optioneel)

| Veld              | Type | Verplicht? | Omschrijving                         | Voorbeeld                                                                                                                                                                                                                                                                   |
|-------------------|------|------------|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Documentnummer    | int  | Ja         | Documentnummer van verzoek           | 2                                                                                                                                                                                                                                                                           |
| Bestandsnaam      | str  | Ja         | Bestandsnaam inventarisdocument      | Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf                                                                                                                                                                                                        |
| Link naar bestand | str  | Ja         | Link naar bestand inventarisdocument | https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf |

### Bijlage document(en)

| Veld                              | Type     | Verplicht?                                                     | Omschrijving                                                                           | Voorbeeld                                                                                                                                                     |                                       |
|-----------------------------------|----------|----------------------------------------------------------------|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Documentnummer                    | int      | Ja                                                             | Documentnummer van verzoek                                                             | 3                                                                                                                                                             |                                       |
| Bestandsnaam                      | str      | Ja                                                             | Bestandsnaam bijlage                                                                   | wob-besluit+hoe+werkt+SZW+dossier.pdf                                                                                                                         |                                       |
| Link naar bestand                 | str      | Ja                                                             | Link naar bijlage                                                                      | https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/07/besluit-op-wob-verzoek-over-openbaarmaking-van-dossier-hoe-werkt-szw/ | wob-besluit+hoe+werkt+SZW+dossier.pdf |
| Type                              | str      | Ja                                                             | Type bijlage                                                                           | E-Mail                                                                                                                                                        |                                       |
| Beoordeling                       | str      | Ja                                                             | Beoordeling van het document (deels openbaar, openbaar, niet openbaar, reeds openbaar) | Openbaar                                                                                                                                                      |                                       |
| Weigeringsgronden                 | list/str | Ja (enkel bij beoordeling 'deels openbaar' en 'niet openbaar') | Vindplaats weigeringsgronden bij niet geheel openbaar document                         | 10.1.b; 10.2.e                                                                                                                                                |                                       |
| Vindplaats reeds openbare stukken | str      | Ja (enkel bij beoordeling 'reeds openbaar')                    | Vindplaats van reeds openbare documenten                                               | https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/07/besluit-op-wob-verzoek-over-openbaarmaking-van-dossier-hoe-werkt-szw/ | wob-besluit+hoe+werkt+SZW+dossier.pdf |
| Afzender                          | str      | Ja                                                             | Afzender bijlage                                                                       | Ministerie van Buitenlandse Zaken                                                                                                                             |                                       |
| Ontvanger                         | str      | Ja                                                             | Ontvanger bijlage                                                                      | World Economic Forum                                                                                                                                          |                                       |
| Datum                             | date     | Ja                                                             | Datum gecreëerd                                                                        | 19-03-2019                                                                                                                                                    |                                       |
| Taal                              | str      | Ja                                                             | Taal van het document                                                                  | Nederlands                                                                                                                                                    |                                       |
| Aantal pagina's                   | int      | Ja                                                             | Aantal pagina's van het document                                                       | 12                                                                                                                                                            |                                       |
| Toelichting                       | str      | Nee                                                            | Eventuele toelichtingen                                                                | Document verstuurd door medewerker BuZa namens minister                                                                                                       |                                       |

## Formaat

Er moet een uniforme standaard komen. Toch is het lastig om dit op een 'structured' manier op te slaan. Er is namelijk vooraf niet altijd vastgesteld hoeveel bijlagen een document heeft, of er überhaupt bijlagen zijn en of alle velden zijn ingevuld. Het lijkt het beste om de Wobs op een 'semi-gestructureerde' manier op te slaan. Dit is een datatype die wat vaste kenmerken heeft, maar niet één vaste structuur heeft. Op deze manier kunnen er makkelijk metadata en tags worden opgeslagen, die het vervolgens makkelijker moeten maken om de Wobs te kunnen doorzoeken. 

Bekende semi-gestructureerde datatypen zijn XML en JSON. Beide zijn 'human-readable'. JSON heeft een dict-structuur met keys en values. Dit maakt het makkelijk om de data vervolgens weer te verwerken in een programmeertaal zoals Python of Javascript. Nieuwe databases als MongoDB gebruiken zelfs JSON als formaat. 

Waarom JSON over XML?

- JSON is echt een formaat om data op te slaan, terwijl XML eigenlijk een markup language is
- Minder groot, dus ook sneller verwerkt en uitgewisseld
- Makkelijk te gebruiken met allerlei programmeertalen, sneller te parsen dan XML
- JSON is over het algemeen beter leesbaar voor mensen dan XML, omdat XML soms vol staat met allerlei tags
- Geen validatie nodig (hier is XML sterk in)

## json voorbeeld

Voorbeeld op basis van https://www.rijksoverheid.nl/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof. In dit voorbeeld mist een inventarislijst.

```json
{
    "id": "BZ-123",
    "titel": "Besluit op Wob-verzoeken over samenwerkingsovereenkomsten Nederlandse overheid en het World Economic Forum (WOF)",
    "verantwoordelijk": "Ministerie van Buitenlandse Zaken",
    "datum_ingediend": "22-12-2021",
    "datum_besluit": "02-02-2022",
    "beschrijving": "Besluit op een verzoek om informatie over de samenwerkingsovereenkomsten tussen  de Nederlandse overheid en het World Economic Forum. Het verzoek is gedaan op basis van de Wet openbaarheid van bestuur (Wob).",
    "besluit": {
        "document_nr": 1,
        "bestandsnaam": "Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
        "link": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
        "besluit": "Deels openbaar",
        "verdaagd": "Nee"
    },
    "inventarislijst": {
        "document_nr": 2,
        "bestandsnaam": "Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
        "link": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf"
    },
    "bijlagen": [
        {
            "document_nr": 3,
            "type": "nota",
            "naam": "Decision for the Food System Initiative",
            "beoordeling": "Deels openbaar",
            "weigeringsgrond": [
                "10.2.e",
                "10.2.g"
            ],
            "datum": "19-03-2019",
            "link": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Bijlagen+bijj+Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
            "paginas": 7,
            "taal": "Engels"
        },
        {
            "document_nr": 4,
            "type": "overeenkomst",
            "naam": "Samenwerkingsovereenkomst Tropical Forest Alliance phase 3",
            "beoordeling": "Deels openbaar",
            "weigeringsgrond": [
                "10.2.e"
            ],
            "datum": "24-06-2021",
            "link": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Bijlagen+bijj+Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
            "paginas": 7,
            "taal": "Nederlands"
        },
        {
            "document_nr": 5,
            "type": "nota",
            "naam": "Grant decision Sustainable Investment Policy and Practice",
            "beoordeling": "Deels openbaar",
            "weigeringsgrond": [
                "10.2.e",
                "10.2.g"
            ],
            "datum": "28-07-2020",
            "link": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Bijlagen+2+bij+Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF+%282%29.pdf",
            "paginas": 5,
            "taal": "Engels"
        },
        {
            "document_nr": 6,
            "type": "nota",
            "naam": "Extended grant decision Sustainable Investment Policy and Practice",
            "beoordeling": "Deels openbaar",
            "weigeringsgrond": [
                "10.2.e"
            ],
            "datum": "24-06-2021",
            "link": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Bijlagen+2+bij+Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF+%282%29.pdf",
            "paginas": 12,
            "taal": "Engels"
        }
    ]
}
```

Voorbeeld op basis van https://www.rijksoverheid.nl/documenten/wob-verzoeken/2022/02/07/besluit-op-wob-verzoek-over-openbaarmaking-van-dossier-hoe-werkt-szw

```json
{
    "id": "SZW-293",
    "titel": "Besluit op Wob-verzoek over openbaarmaking van dossier 'Hoe werkt SZW'",
    "verantwoordelijk": "Ministerie van Sociale Zaken en Werkgelegenheid",
    "internid": "Wob-2910",
    "datum_ingediend": "14-01-2021",
    "datum_besluit": "07-02-2022",
    "beschrijving": "Besluit op Wob-verzoek over openbaarmaking van dossier 'Hoe werkt SZW', waarnaar wordt verwezen op pagina 4 van het Introductiedossier SZW (december 2021). Het verzoek is gedaan op basis van de Wet openbaarheid van bestuur (Wob).",
    "besluit": {
        "document_nr": 1,
        "bestandsnaam": "wob-besluit+hoe+werkt+SZW+dossier.pdf",
        "link": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/07/besluit-op-wob-verzoek-over-openbaarmaking-van-dossier-hoe-werkt-szw/      wob-besluit+hoe+werkt+SZW+dossier.pdf",
        "besluit": "Openbaar",
        "verdaagd": "Nee"
    },
    "bijlagen": [
        {
            "document_nr": 2,
            "type": "dossier",
            "naam": "Dossier 'Hoe werkt SZW'",
            "beoordeling": "Deels openbaar",
            "weigeringsgrond": [
                "10.2.e"
            ],
            "datum": "01-12-2021",
            "link": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/07/besluit-op-wob-verzoek-over-openbaarmaking-van-dossier-hoe-werkt-szw/Hoe+werkt+SZW+dossier.pdf",
            "paginas": 32,
            "taal": "Nederlands"
        }
    ]
}
```

## Openstate rapport velden

Verschil is dat zij alleen een WOB verzoek proberen op te slaan, mijn onderzoek heeft ook verschillende velden voor de gelinkte documenten.

Verplichte velden: ID, Behandelend bestuursorgaan, Eerste ontvanger informatieverzoek,
Thema, Titel, Ontvangstdatum, Besluitdatum, URL naar informatieverzoek, URL naar
besluit of reactiebrief.

Niet verplichte velden: Intern volgnummer, Subthema, Aanvullende Thema,
Omschrijving, Verzoeker, Status, Verschoonbare termijnoverschrijding, URL naar
inventarisatielijst, URL naar bijlagen, Titel voor URL naar bijlage, Geografisch gebied, BAG
ID, BGT ID, Longitude, Latitude, N; Postcodegebied.

## Handige onderzoeken

Abiteboul, S. (1997, January). Querying semi-structured data. In International Conference on Database Theory (pp. 1-18). Springer, Berlin, Heidelberg. https://apps.dtic.mil/sti/pdfs/ADA428473.pdf



