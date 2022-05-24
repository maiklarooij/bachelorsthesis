# Anatomie

Hoe representeren we een Wob-verzoek? Wat willen we opslaan?

## Geheel Wob-verzoek

|Veld|Engels|Namespace|Type|Verplicht?|Omschrijving|Voorbeeld|
|:----|:----|:----|:----|:----|:----|:----|
|identifier|identifier|DCMI|number|Ja|Uniek ID|3928|
|titel|title|DCMI|string|Ja|Titel Wob-verzoek|Besluit op Wob-verzoeken over samenwerkingsovereenkomsten Nederlandse overheid en het World Economic Forum (WOF)|
|type|type|DCMI|string|Ja|2 keuzes: ‘Verzoek’ of ‘Actieve openbaarmaking’|Verzoek|
|bronUrl|sourceUrl|WOO|string|Ja|URL naar publicatie|https://www.rijksoverheid.nl/documenten/wob-verzoeken/2022/03/31/besluit-op-wob-verzoek-over-een-eu-rapport-over-gujarat-2002|
|thema|topic|WOO/FOAF|string|Nee|Eventueel thema van het Wob-verzoek|Wob-verzoeken vrije tijd|
|idThema|idTopic|WOO|string|Nee|Uniek ID van het thema|VT01|
|behandeldDoor|handledBy|WOO|string|Ja|Verantwoordelijke voor het behandelen van het Wob-verzoek|Ministerie van Buitenlandse Zaken|
|datumIngediend|fileDate|WOO|date|Ja, bij type = ‘Verzoek’|Datum van indienen Wob-verzoek (ISO 8601)|2021-12-04|
|datumBesluit|decisionDate|WOO|date|Ja|Datum van reactie/besluit Wob-verzoek (ISO 8601)|2022-02-02|
|beoordeling|valuation|WOO|string|Ja|Beoordeling geheel Wob-verzoek|Deels openbaar|
|isVerdaagd|isAdjourned|WOO|boolean|Ja, bij type = ‘Verzoek’|Geeft aan of het besluit verdaagd is (ja/nee)|False|
|beschrijving|description|DCMI|string|Nee|Beschrijving Wob-verzoek|Besluit op een verzoek om informatie over de samenwerkingsovereenkomsten tussen de Nederlandse overheid en het World Economic Forum (WEF).|
|documenten|documents|WOO|array|Nee|Lijst met alle documenten. Elk document is een object.|-|
|idIntern|idInternal|WOO|string/number|Nee|Volgnummer voor intern gebruik|BUZA-129|
|verzoeker|requester|WOO|string|Nee|Naam verzoeker|Follow the Money|
|aantalDocumenten|numberDocuments|WOO|number|Nee|Aantal vrijgegeven documenten|5|
|verkregenVan|retrievedAt|
|firstRecipient


### Document (besluit, verzoek, inventaris, bijlage)

|Veld|Engels|Namespace|Type|Verplicht?|Omschrijving|Voorbeeld|
|:----|:----|:----|:----|:----|:----|:----|
|identifier|identifier|DCMI|number|Ja|Uniek Document ID|3|
|titel|title|DCMI|string|Ja|Titel van het document|Besluit Wob verzoek De Vaandeldrager|
|bestandsNaam|fileName|FTM|string|Ja|Bestandsnaam|2021-105+Besluit+Wob-verzoek++De+Vaandeldrager.pdf|
|bestandsExtensie|fileExtension|FTM|string|Ja|Type bestand (pdf, zip, etc)|PDF|
|mimeType|mimeType|FTM|string|Ja|MIME type van het bestand|application/pdf|
|documentType|documentType|WOO|string|Ja|Type document (keuze uit: bijlage, besluit, inventaris, verzoek)|Besluit|
|url|url|WOO|string|Ja|URL naar bestand|https://www.rijksoverheid.nl/documenten/wob-verzoeken/2022/02/25/besluit-wob-verzoek-schilderij-de-vaandeldager-over-adviezen-aankoop|
|aantalPaginas|numberPages|WOO|number|Ja|Aantal pagina's bestand|3|
|aantalWoorden|numberWords|WOO|number|Nee|Aantal woorden in bestand|291|
|isScan|isScan|WOO|boolean|Nee|Is het document ingescand (en dus niet leesbaar voor een computer)? |False|
|aantalTekstpaginas|numberTextPages|WOO|number|Nee|Aantal pagina's in bestand met tekst|2|
|datumDownload|downloadDate|WOO|date|Nee|Gedownload op datum (ISO 8601)|2022-03-01|
|taal|language|FTM|string|Nee|Taal van het document (ISO-639-3 standaard)|nld|
|bestandsGrootte|fileSize|FTM|string|Nee|Grootte van het bestand|392 kB|
|crawler|crawler|FTM|string|Nee|Gebruikte crawler om het bestand op te halen|webCrawler 2.0|


### Extra velden voor vrijgegeven document

|Veld|Engels|Namespace|Type|Verplicht?|Omschrijving|Voorbeeld|
|:----|:----|:----|:----|:----|:----|:----|
|bijlageType|annexType|WOO|string|Ja|Type vrijgegeven document|E-Mail|
|beoordeling|valuation|WOO|string|Ja|Beoordeling van het document (deels openbaar, openbaar, niet openbaar, reeds openbaar)|Deels openbaar|
|weigeringsGronden|groundsOfRefusal|WOO|array|Ja (enkel bij beoordeling 'deels openbaar' en 'niet openbaar')|Vindplaats weigeringsgronden bij niet geheel openbaar document|10.1.b; 10.2.e|
|vindplaatsReedsOpenbaar|alreadyPublicLocation |WOO|string|Ja (enkel bij beoordeling 'reeds openbaar')|Vindplaats (URL) van reeds openbare documenten|https://www.rijksoverheid.nl/binaries/rijksoverheid/documenten/wob-verzoeken/2022/02/07/besluit-op-wob-verzoek-over-openbaarmaking-van-dossier-hoe-werkt-szw/wob-besluit+hoe+werkt+SZW+dossier.pdf|
|afzender|originator|WOO|string|Nee|Afzender bijlage|Ministerie van Buitenlandse Zaken|
|ontvanger|recipient|WOO|string|Nee|Ontvanger bijlage|Officier van Justitie|
|datum|date|DCMI|date|Ja|Datum gecreëerd (ISO 8601)|2021-09-14|

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



