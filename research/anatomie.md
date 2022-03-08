# Anatomie

Hoe representeren we een Wob-verzoek? Wat willen we opslaan?

## Geheel Wob-verzoek


| Veld               | Type    | Verplicht? | Omschrijving                                              | Voorbeeld                                                                                                                                  |
|--------------------|---------|------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ID                 | number     | Ja         | Uniek ID                                                  | 3928                                                                                                                                       |
| Titel              | string     | Ja         | Titel Wob-verzoek                                         | Besluit op Wob-verzoeken over samenwerkingsovereenkomsten Nederlandse overheid en het World Economic Forum (WOF)                           |
| Thema | string | Nee | Eventueel thema van het Wob-verzoek | Wob-verzoeken vrije tijd |
| Verantwoordelijken | string     | Ja         | Verantwoordelijke voor het behandelen van het Wob-verzoek | Ministerie van Buitenlandse Zaken                                                                                                          |
| Indiendatum        | date    | Ja         | Datum van indienen Wob-verzoek                            | 22-12-2021                                                                                                                                 |
| Besluitdatum       | date    | Ja         | Datum van reactie/besluit Wob-verzoek                     | 02-02-2022                                                                                                                                 |
| Beoordeling        | string     | Ja         | Beoordeling geheel Wob-verzoek                            | Deels openbaar |
| Verdaagd           | boolean     | Ja         | Geeft aan of het besluit verdaagd is (ja/nee)             | False |
| Beschrijving       | string     | Nee        | Beschrijving Wob-verzoek                                  | Besluit op een verzoek om informatie over de samenwerkingsovereenkomsten tussen de Nederlandse overheid en het World Economic Forum (WEF). |
| Documenten         | array   | Nee | Lijst met alle documenten. Elk document is een object. | -
| Intern volgnummer  | string/number | Nee        | Volgnummer voor intern gebruik                            | BUZA-129                                                                                                                                   |
| Verzoeker          | string     | Nee        | Naam verzoeker                                            | Follow the Money                                                                                                                           |
| Geografisch gebied | string     | Nee        | Naam geografisch gebied                                   | Den Haag                                                                                                                                   |
| BAG ID             | number     | Nee        | Basisregistratie Adressen en Gebouwen ID                  | 2389120312367                                                                                                                              |
| BGT ID             | number     | Nee        | Basisregistratie Grootschalige Topografie ID              | 3243134                                                                                                                                    |
| Longitude          | number   | Nee        | Oost-west positie                                         | 103.800670                                                                                                                                 |
| Latitude           | number   | Nee        | Noord-zuid positie                                        | 1.320660                                                                                                                                   |
| Postcodegebied     | string     | Nee        | Postcodenummers                                           | 3825                                                                                                                                       |
| Aantal vrijgegeven documenten | number | Nee | Aantal vrijgegeven documenten | 5 |

### Document (besluit, verzoek, inventaris, bijlage)

| Veld              | Type | Verplicht? | Omschrijving                                 | Voorbeeld                                                                                                                                                                                          |
|-------------------|------|------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Documentnummer    | number  | Ja         | Documentnummer van verzoek                   | 3                                                                                                                                                                                                  |
| Bestandsnaam      | string  | Ja         | Bestandsnaam                         | 2021-105+Besluit+Wob-verzoek++De+Vaandeldrager.pdf                                                                                                                                                             |
| Bestandstype      | string  | Ja         | Type bestand (pdf, zip, etc)                 | PDF                                                                                                                                                                                                |
| Type document     | string  | Ja         | Type document (keuze uit: bijlage, besluit, inventaris, verzoek) | Besluit                                                                                                                                                                                            |
| URL naar bestand | string  | Ja         | URL naar bestand                            | https://www.rijksoverheid.nl/documenten/wob-verzoeken/2022/02/25/besluit-wob-verzoek-schilderij-de-vaandeldager-over-adviezen-aankoop |
| Pagina's          | number  | Ja         | Aantal pagina's bestand                      | 3                                                                                                                                                                                                  |                                      |
| Woorden | number | Nee | Aantal woorden in bestand | 291 |
| Scan | boolean | Nee | Is het document ingescand? | False |
| Tekstpagina's | number | Nee | Aantal pagina's in bestand met tekst | 2 |
| Download datum | date | Nee | Gedownload op | 01-03-2022 |
| Taal                              | string      | Nee                                                             | Taal van het document                                                                  | Nederlands  |
| Grootte | string | Nee | Grootte van het bestand | 392 kB |

### Extra velden voor vrijgegeven document

| Veld                              | Type     | Verplicht?                                                     | Omschrijving                                                                           | Voorbeeld                                                                                                                                                                                          |
|-----------------------------------|----------|----------------------------------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Type vrijgegeven document                      | string      | Ja                                                             | Type vrijgegeven document | E-Mail | 
| Titel vrijgegeven document | string | Nee | Titel van het document, indien aanwezig | Gespreksverslag advocate restauranthouder |                                                                                                                                                                       
| Beoordeling                       | string      | Ja                                                             | Beoordeling van het document (deels openbaar, openbaar, niet openbaar, reeds openbaar) | Openbaar                                                                                                                                                                                           |
| Weigeringsgronden                 | array | Ja (enkel bij beoordeling 'deels openbaar' en 'niet openbaar') | Vindplaats weigeringsgronden bij niet geheel openbaar document                         | 10.1.b; 10.2.e                                                                                                                                                                                     |
| Vindplaats reeds openbare stukken | string      | Ja (enkel bij beoordeling 'reeds openbaar')                    | Vindplaats (URL) van reeds openbare documenten                                               | https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/07/besluit-op-wob-verzoek-over-openbaarmaking-van-dossier-hoe-werkt-szw/wob-besluit+hoe+werkt+SZW+dossier.pdf |
| Afzender                          | string      | Nee                                                             | Afzender bijlage                                                                       | Ministerie van Buitenlandse Zaken                                                                                                                                                                  |
| Ontvanger                         | string      | Nee                                                             | Ontvanger bijlage                                                                      | World Economic Forum                                                                                                                                                                               |
| Datum                             | date     | Ja                                                             | Datum gecreëerd                                                                        | 19-03-2019                                                                                                                                                                                         |                                                                                                                                                                                       |
| Toelichting                       | string      | Nee                                                            | Eventuele toelichtingen                                                                | Document verstuurd door medewerker BuZa namens minister                                                                                                                                            |

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
    "besluit": "Deels openbaar",
    "verdaagd": false,
    "documenten": [
        {
            "type": "Verzoek",
            "document_nr": 0,
        }
        {
            "type": "Besluit",
            "document_nr": 1,
            "bestandsnaam": "Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
            "url": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
        },
        {
            "type": "Inventarislijst",
            "document_nr": 2,
            "bestandsnaam": "Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
            "url": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf"
        },
        {
            "type": "Bijlage",
            "document_nr": 3,
            "type_bijlage": "nota",
            "naam": "Decision for the Food System Initiative",
            "beoordeling": "Deels openbaar",
            "weigeringsgrond": [
                "10.2.e",
                "10.2.g"
            ],
            "datum": "19-03-2019",
            "url": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Bijlagen+bijj+Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
            "paginas": 7,
            "taal": "Engels"
        },
        {
            "type": "Bijlage",
            "document_nr": 4,
            "type_bijlage": "overeenkomst",
            "naam": "Samenwerkingsovereenkomst Tropical Forest Alliance phase 3",
            "beoordeling": "Deels openbaar",
            "weigeringsgrond": [
                "10.2.e"
            ],
            "datum": "24-06-2021",
            "url": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Bijlagen+bijj+Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
            "paginas": 7,
            "taal": "Nederlands"
        },
        {
            "type": "Bijlage",
            "document_nr": 5,
            "type_bijlage": "nota",
            "naam": "Grant decision Sustainable Investment Policy and Practice",
            "beoordeling": "Deels openbaar",
            "weigeringsgrond": [
                "10.2.e",
                "10.2.g"
            ],
            "datum": "28-07-2020",
            "url": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Bijlagen+2+bij+Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF+%282%29.pdf",
            "paginas": 5,
            "taal": "Engels"
        },
        {
            "type": "Bijlage",
            "document_nr": 6,
            "type_bijlage": "nota",
            "naam": "Extended grant decision Sustainable Investment Policy and Practice",
            "beoordeling": "Deels openbaar",
            "weigeringsgrond": [
                "10.2.e"
            ],
            "datum": "24-06-2021",
            "url": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Bijlagen+2+bij+Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF+%282%29.pdf",
            "paginas": 12,
            "taal": "Engels"
        }
    ]
}
```

Voorbeeld op basis van https://www.utrecht.nl/bestuur-en-organisatie/publicaties/openbaar-gemaakte-informatie-na-wob-verzoeken/wob-verzoek/2021-0790-wob-besluit-betreft-demonstratie-waku-waku/

```json
{
    "id": "UT-201",
    "titel": "2021-0790 Wob-besluit betreft demonstratie Waku Waku",
    "verantwoordelijk": "Gemeente Utrecht",
    "datum_ingediend": "07-10-2021",
    "datum_besluit": "01-02-2022",
    "beschrijving": "De burgemeester heeft op 2 februari 2022 beslist op een Wob-verzoek van een inwoner. In het Wob-verzoek wordt verzocht om alle documenten in het bezit van de gemeente die betrekking hebben op de demonstraties bij Waku Waku. Tevens wordt er verzocht om alle processtukken van de voorlopige voorziening, waaronder de dagvaarding, bezwaarschrift, verweerschriften, pleitnota's van beide partijen en het proces-verbaal van de politie waar in de zaak naar verwezen wordt.",
    "besluit": "Deels openbaar",
    "verdaagd": true,
    "thema": "Wob-verzoeken vrije tijd",
    "geografisch_gebied": "Utrecht",
    "documenten": [
        {
            "document_nr": 1,
            "bestandsnaam": "Wob-verzoek.pdf",
            "bestandstype": "PDF",
            "documenttype": "Verzoek",
            "url": "https://www.utrecht.nl/fileadmin/uploads/documenten/7.extern/wob/2021/2021-0790_Waku_Waku/Wob-verzoek.pdf",
            "paginas": 3,
            "download_datum": "03-03-2022",
            "scan": true
        },
        {
            "document_nr": 2,
            "bestandsnaam": "Wob-besluit.pdf",
            "bestandstype": "PDF",
            "documenttype": "Besluit",
            "url": "https://www.utrecht.nl/fileadmin/uploads/documenten/7.extern/wob/2021/2021-0790_Waku_Waku/Wob-besluit.pdf",
            "paginas": 5,
            "download_datum": "03-03-2022"
        },
        {
            "document_nr": 3,
            "bestandsnaam": "20211019170012_ Gespreksverslag advocate van restauranthouder1.pdf",
            "bestandstype": "PDF",
            "documenttype": "Gespreksverslag",
            "titel": "Gespreksverslag advocate restauranthouder",
            "url": "https://www.utrecht.nl/fileadmin/uploads/documenten/7.extern/wob/2021/2021-0790_Waku_Waku/Bijlagen.pdf",
            "paginas": 3,
            "download_datum": "03-03-2022",
            "type_vrijgegeven_document": "E-Mail",
            "beoordeling": "Deels openbaar",
            "weigeringsgrond": [
                "10.2.e"
            ],
            "datum": "29-09-2021"
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



