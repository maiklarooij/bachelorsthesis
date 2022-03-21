# Anatomie

Hoe representeren we een Wob-verzoek? Wat willen we opslaan?

## Geheel Wob-verzoek


| Veld               | Engels | Type    | Verplicht? | Omschrijving                                              | Voorbeeld                                                                                                                                  |
|--------------------|---------|-------|------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| verzoek_id      | request_id |  number     | Ja         | Uniek ID                                                  | 3928                                                                                                                                       |
| titel | title  | string     | Ja         | Titel Wob-verzoek                                         | Besluit op Wob-verzoeken over samenwerkingsovereenkomsten Nederlandse overheid en het World Economic Forum (WOF)                           |
| thema | theme | string | Nee | Eventueel thema van het Wob-verzoek | Wob-verzoeken vrije tijd |
| verantwoordelijk | responsible | string     | Ja         | Verantwoordelijke voor het behandelen van het Wob-verzoek | Ministerie van Buitenlandse Zaken                                                                                                          |
| datum_ingediend | file_date | date    | Ja         | Datum van indienen Wob-verzoek                            | 22-12-2021                                                                                                                                 |
| datum_besluit | response_date  | date    | Ja         | Datum van reactie/besluit Wob-verzoek                     | 02-02-2022                                                                                                                                 |
| beoordeling   | valuation     | string     | Ja         | Beoordeling geheel Wob-verzoek                            | Deels openbaar |
| verdaagd | adjourned      | boolean     | Ja         | Geeft aan of het besluit verdaagd is (ja/nee)             | False |
| beschrijving | description       | string     | Nee        | Beschrijving Wob-verzoek                                  | Besluit op een verzoek om informatie over de samenwerkingsovereenkomsten tussen de Nederlandse overheid en het World Economic Forum (WEF). |
| documenten         | documenten | array   | Nee | Lijst met alle documenten. Elk document is een object. | -
| intern_id  | internal_id | string/number | Nee        | Volgnummer voor intern gebruik                            | BUZA-129                                                                                                                                   |
| verzoeker | requester     | string     | Nee        | Naam verzoeker                                            | Follow the Money                                                                                                                           |
| geografisch_gebied | geographical_area | string     | Nee        | Naam geografisch gebied                                   | Den Haag                                                                                                                                   |
| bag_id             | bag_id | number     | Nee        | Basisregistratie Adressen en Gebouwen ID                  | 2389120312367                                                                                                                              |
| bgt_id | bgt_id           | number     | Nee        | Basisregistratie Grootschalige Topografie ID              | 3243134                                                                                                                                    |
| longitude  | longitude   | number   | Nee        | Oost-west positie                                         | 103.800670                                                                                                                                 |
| latitude    | latitude       | number   | Nee        | Noord-zuid positie                                        | 1.320660                                                                                                                                   |
| postcodegebied     | zipcode_area | string     | Nee        | Postcodenummers                                           | 3825                                                                                                                                       |
| aantal_documenten | number_documents | number | Nee | Aantal vrijgegeven documenten | 5 |

### Document (besluit, verzoek, inventaris, bijlage)

| Veld              | Engels | Type | Verplicht? | Omschrijving                                 | Voorbeeld                                                                                                                                                                                          |
|-------------------|----------|------|------------|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| document_id | document_id    | number  | Ja         | Uniek Document ID                 | 3                                                                                                                                                                                                  |
| bestandsnaam      | filename | string  | Ja         | Bestandsnaam                         | 2021-105+Besluit+Wob-verzoek++De+Vaandeldrager.pdf                                                                                                                                                             |
| bestandstype      | filetype | string  | Ja         | Type bestand (pdf, zip, etc)                 | PDF                                                                                                                                                                                                |
| documenttype     | document_type | string  | Ja         | Type document (keuze uit: bijlage, besluit, inventaris, verzoek) | Besluit                                                                                                                                                                                            |
| url | url | string  | Ja         | URL naar bestand                            | https://www.rijksoverheid.nl/documenten/wob-verzoeken/2022/02/25/besluit-wob-verzoek-schilderij-de-vaandeldager-over-adviezen-aankoop |
| aantal_paginas          | number_pages | number  | Ja         | Aantal pagina's bestand                      | 3                                                                                                                                                                                                  |                                      |
| aantal_woorden | number_words | number | Nee | Aantal woorden in bestand | 291 |
| scan | scan | boolean | Nee | Is het document ingescand? | False |
| aantal_tekstpaginas | number_textpages | number | Nee | Aantal pagina's in bestand met tekst | 2 |
| download_datum | download_date |  date | Nee | Gedownload op | 01-03-2022 |
| taal | language |                              | string      | Nee                                                             | Taal van het document                                                                  | Nederlands  |
| grootte | size | string | Nee | Grootte van het bestand | 392 kB |

### Extra velden voor vrijgegeven document

| Veld            | Engels         | Type     | Verplicht?                                                     | Omschrijving                                                                           | Voorbeeld                                                                                                                                                                                          |
|-----------------------------------|-----------|----------|----------------------------------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| bijlagetype   | annex_type                      | string      | Ja                                                             | Type vrijgegeven document | E-Mail | 
| titel | title | string | Nee | Titel van het document, indien aanwezig | Gespreksverslag advocate restauranthouder |                                                                                                                                                                       
| beoordeling | valuation |                       | string      | Ja                                                             | Beoordeling van het document (deels openbaar, openbaar, niet openbaar, reeds openbaar) | Openbaar                                                                                                                                                                                           |
| weigeringsgrond | ground_of_refusal      | array | Ja (enkel bij beoordeling 'deels openbaar' en 'niet openbaar') | Vindplaats weigeringsgronden bij niet geheel openbaar document                         | 10.1.b; 10.2.e                                                                                                                                                                                     |
| vindplaats_reeds_openbaar | already_public_location string      | Ja (enkel bij beoordeling 'reeds openbaar')                    | Vindplaats (URL) van reeds openbare documenten                                               | https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/07/besluit-op-wob-verzoek-over-openbaarmaking-van-dossier-hoe-werkt-szw/wob-besluit+hoe+werkt+SZW+dossier.pdf |
| afzender | originator          | string      | Nee                                                             | Afzender bijlage                                                                       | Ministerie van Buitenlandse Zaken                                                                                                                                                                  |
| ontvanger | recipient      |    | string      | Nee                                                             | Ontvanger bijlage                                                                      | World Economic Forum                                                                                                                                                                               |
| datum  | date |                           | date     | Ja                                                             | Datum gecreëerd                                                                        | 19-03-2019                                                                                                                                                                                         |                                                                                                                                                                                       |
| toelichting | commentary            | string      | Nee                                                            | Eventuele toelichtingen                                                                | Document verstuurd door medewerker BuZa namens minister                                                                                                                                            |

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
    "wob_id": "BZ123",
    "titel": "Besluit op Wob-verzoeken over samenwerkingsovereenkomsten Nederlandse overheid en het World Economic Forum (WOF)",
    "verantwoordelijk": "Ministerie van Buitenlandse Zaken",
    "datum_ingediend": "22-12-2021",
    "datum_besluit": "02-02-2022",
    "beschrijving": "Besluit op een verzoek om informatie over de samenwerkingsovereenkomsten tussen  de Nederlandse overheid en het World Economic Forum. Het verzoek is gedaan op basis van de Wet openbaarheid van bestuur (Wob).",
    "besluit": "Deels openbaar",
    "verdaagd": false,
    "aantal_documenten": 6,
    "documenten": [
        {
            "documenttype": "Besluit",
            "document_id": "BZ123-1",
            "bestandsnaam": "Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
            "bestandstype": "pdf",
            "url": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
            "grootte": "395 kB"
        },
        {
            "documenttype": "Inventarislijst",
            "document_id": "BZ123-2",
            "bestandsnaam": "Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
            "url": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
            "bestandstype": "pdf",
            "grootte": "201 kB"
        },
        {
            "documenttype": "Bijlage",
            "document_id": "BZ123-3",
            "type_bijlage": "nota",
            "naam": "Decision for the Food System Initiative",
            "beoordeling": "Deels openbaar",
            "weigeringsgrond": [
                "10.2.e",
                "10.2.g"
            ],
            "datum": "19-03-2019",
            "url": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Bijlagen+bijj+Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
            "bestandstype": "pdf",
            "paginas": 7,
            "taal": "Engels"
        },
        {
            "documenttype": "Bijlage",
            "document_id": "BZ123-4",
            "type_bijlage": "overeenkomst",
            "naam": "Samenwerkingsovereenkomst Tropical Forest Alliance phase 3",
            "beoordeling": "Deels openbaar",
            "weigeringsgrond": [
                "10.2.e"
            ],
            "datum": "24-06-2021",
            "url": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Bijlagen+bijj+Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF.pdf",
            "bestandstype": "pdf",
            "paginas": 7,
            "taal": "Nederlands",
            "grootte": "1,1 MB"
        },
        {
            "documenttype": "Bijlage",
            "document_id": "BZ123-5",
            "type_bijlage": "nota",
            "naam": "Grant decision Sustainable Investment Policy and Practice",
            "beoordeling": "Deels openbaar",
            "weigeringsgrond": [
                "10.2.e",
                "10.2.g"
            ],
            "datum": "28-07-2020",
            "url": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Bijlagen+2+bij+Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF+%282%29.pdf",
            "bestandstype": "pdf",
            "paginas": 5,
            "taal": "Engels"
        },
        {
            "documenttype": "Bijlage",
            "document_id": "BZ123-6",
            "type_bijlage": "nota",
            "naam": "Extended grant decision Sustainable Investment Policy and Practice",
            "beoordeling": "Deels openbaar",
            "weigeringsgrond": [
                "10.2.e"
            ],
            "datum": "24-06-2021",
            "url": "https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/02/besluit-op-wob-verzoeken-over-samenwerkingsovereenkomsten-nederlandse-overheid-en-het-world-economic-forum-wof/Bijlagen+2+bij+Wob-verzoeken+samenwerkingsovereenkomsten+met+NL+overheid+en+WOF+%282%29.pdf",
            "bestandstype": "pdf",
            "paginas": 12,
            "taal": "Engels"
        }
    ]
}
```

Voorbeeld op basis van https://www.utrecht.nl/bestuur-en-organisatie/publicaties/openbaar-gemaakte-informatie-na-wob-verzoeken/wob-verzoek/2021-0790-wob-besluit-betreft-demonstratie-waku-waku/

Voldoet niet volledig aan de eisen.

```json
{
    "wob_id": "UTR201",
    "titel": "2021-0790 Wob-besluit betreft demonstratie Waku Waku",
    "verantwoordelijk": "Gemeente Utrecht",
    "datum_ingediend": "07-10-2021",
    "datum_besluit": "01-02-2022",
    "beschrijving": "De burgemeester heeft op 2 februari 2022 beslist op een Wob-verzoek van een inwoner. In het Wob-verzoek wordt verzocht om alle documenten in het bezit van de gemeente die betrekking hebben op de demonstraties bij Waku Waku. Tevens wordt er verzocht om alle processtukken van de voorlopige voorziening, waaronder de dagvaarding, bezwaarschrift, verweerschriften, pleitnota's van beide partijen en het proces-verbaal van de politie waar in de zaak naar verwezen wordt.",
    "besluit": "Deels openbaar",
    "verdaagd": true,
    "thema": "Wob-verzoeken vrije tijd",
    "geografisch_gebied": "Utrecht",
    "aantal_documenten": 3,
    "documenten": [
        {
            "document_nr": "UTR201-1",
            "bestandsnaam": "Wob-verzoek.pdf",
            "bestandstype": "PDF",
            "documenttype": "Verzoek",
            "url": "https://www.utrecht.nl/fileadmin/uploads/documenten/7.extern/wob/2021/2021-0790_Waku_Waku/Wob-verzoek.pdf",
            "paginas": 3,
            "download_datum": "03-03-2022",
            "scan": true
        },
        {
            "document_nr": "UTR201-2",
            "bestandsnaam": "Wob-besluit.pdf",
            "bestandstype": "PDF",
            "documenttype": "Besluit",
            "url": "https://www.utrecht.nl/fileadmin/uploads/documenten/7.extern/wob/2021/2021-0790_Waku_Waku/Wob-besluit.pdf",
            "paginas": 5,
            "download_datum": "03-03-2022"
        },
        {
            "document_nr": "UTR201-3",
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



