# Anatomie

Hoe representeren we een Wob-verzoek? Wat willen we opslaan?

## Geheel Wob-verzoek

Verplichte velden:
- ID
- Titel
- Verantwoordelijken
- Indiendatum
- Besluitdatum

Optionele velden:
- Beschrijving
- Intern volgnummer
- Verzoeker
- Geografische velden:
    - Geografisch gebied
    - BAG ID
    - BGT ID
    - Longitude
    - Latitude
    - Postcodegebied

### Besluit document (verplicht)

- Documentnummer (# van verzoek)
- Bestandsnaam
- Link naar bestand
- Besluit (openbaar, deels openbaar, niet openbaar)
- Verdaagd (ja/nee)

### Inventaris document (optioneel)

- Documentnummer (# van verzoek)
- Bestandsnaam
- Link naar bestand

### Bijlage document(en)

Verplichte velden:
- Documentnummer (van verzoek): 1
- Type: Verslag, E-mail, Nota, Brief, SMS, Rapport, Notitie, Presentatie, Spreadsheet, Overeenkomst, Memo, Anders
- Naam document
- Beoordeling: Deels openbaar
- Datum
- Link naar bestand
- Aantal pagina's

Optionele velden:
- Weigeringsgronden (eventueel, bij niet of deels openbaar): 10.1.b; 10.2.e
- Afzender
- Ontvanger

## Formaat

csv? json? xml? 

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
            "paginas": 7
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
            "paginas": 7
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
            "paginas": 5
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
            "paginas": 12
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
            "paginas": 32
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