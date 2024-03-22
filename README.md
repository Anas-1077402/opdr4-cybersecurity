# wp3-2024-starter
Applicatie geproduceerd door Rachaan de Graaff, Anas Amhaou & Niels Hoogeveen. Deze 
applicatie is ontworpen voor Stichting Accessibility (zie ook de [opdracht](CASUS.md)) 


## Installatie
Voer al deze stappen uit in de opdrachtprompt (cmd)

1. **Maak een virtuele omgeving aan:**
    ```
    python3 -m venv myenv
    ```

2. **Activeer de virtuele omgeving:**
    ```
    myvenv\Scripts\activate
    ```

3. **Installeer de requirements:**
    ```
    pip install -r requirements.txt
    ```

4. **Start het met het draaien van de applicatie:**
    ```
    python root\manage.py runserver
    ```

5. **Openen van de applicatie:**
    Run de applicatie op [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

    Gebruik de volgende inloggegevens:
    - Beheerder:
        - Gebruikersnaam: test_rachaan
        - Wachtwoord: Test123N

    - Ervaringsdeskundige:
        - Gebruikersnaam: test_niels
        - Wachtwoord: Test123N


## API documentatie
Voor de opzet om een onderzoek te posten of te updaten kijk dan naar: [test_data](test_data.json)

API/organisatie/<int:organisatie_id>/onderzoeken/<int:onderzoeks_id>?api={api_key}:

    - GET (1 specifiek onderzoek)
        Retourneert:
            onderzoeks_id (integer)
            organisatie (integer)
            status (string)
            titel (string)
            omschrijving (string)
            datum_vanaf (date)
            datum_tot (date)
            soort_onderzoek (string)
            locatie (string)
            met_beloning (boolean)
            beloning (string)
            doelgroep_leeftijd_van (integer)
            doelgroep_leeftijd_tot (integer)
            contact_opgenomen (boolean)
            opmerkingen_beheerder (string)


    - PUT (1 specifiek onderzoek)
        Een JSON-object met de velden die bijgewerkt moeten worden:
            api (string): API-key van de organisatie
            titel (string): Titel van het onderzoek
            omschrijving (string): Omschrijving van het onderzoek
            datum_vanaf (date): Begindatum van het onderzoek
            datum_tot (date): Einddatum van het onderzoek
            soort_onderzoek (string): Soort onderzoek
            locatie (string): Locatie van het onderzoek
            met_beloning (boolean): Geeft aan of er een beloning is voor deelnemers
            beloning (string): Omschrijving van de beloning (optioneel)
            doelgroep_leeftijd_van (integer): Minimale leeftijd van de doelgroep
            doelgroep_leeftijd_tot (integer): Maximale leeftijd van de doelgroep
            contact_opgenomen (boolean): Geeft aan of er contact is opgenomen met de doelgroep
            opmerkingen_beheerder (string): Eventuele opmerkingen van de beheerder

        Retourneert:
            onderzoeks_id (integer)
            organisatie (integer)
            status (string)
            titel (string)
            omschrijving (string)
            datum_vanaf (date)
            datum_tot (date)
            soort_onderzoek (string)
            locatie (string)
            met_beloning (boolean)
            beloning (string)
            doelgroep_leeftijd_van (integer)
            doelgroep_leeftijd_tot (integer)
            contact_opgenomen (boolean)
            opmerkingen_beheerder (string)


API/organisatie/<int:organisatie_id>/onderzoeken?api={api_key}:

    - POST (nieuw onderzoek aanmaken)
        Een JSON-object met de velden die bijgewerkt moeten worden:
            api (string): API-key van de organisatie
            titel (string): Titel van het onderzoek
            omschrijving (string): Omschrijving van het onderzoek
            datum_vanaf (date): Begindatum van het onderzoek
            datum_tot (date): Einddatum van het onderzoek
            soort_onderzoek (string): Soort onderzoek
            locatie (string): Locatie van het onderzoek
            met_beloning (boolean): Geeft aan of er een beloning is voor deelnemers
            beloning (string): Omschrijving van de beloning (optioneel)
            doelgroep_leeftijd_van (integer): Minimale leeftijd van de doelgroep
            doelgroep_leeftijd_tot (integer): Maximale leeftijd van de doelgroep
            contact_opgenomen (boolean): Geeft aan of er contact is opgenomen met de doelgroep
            opmerkingen_beheerder (string): Eventuele opmerkingen van de beheerder

        Retourneert:
            onderzoeks_id (integer)
            organisatie (integer)
            status (string)
            titel (string)
            omschrijving (string)
            datum_vanaf (date)
            datum_tot (date)
            soort_onderzoek (string)
            locatie (string)
            met_beloning (boolean)
            beloning (string)
            doelgroep_leeftijd_van (integer)
            doelgroep_leeftijd_tot (integer)
            contact_opgenomen (boolean)
            opmerkingen_beheerder (string)

    - GET (alle onderzoeken ophalen)
        Retourneert:
        Een lijst van alle onderzoeken met de volgende velden:
            onderzoeks_id (integer)
            organisatie (integer)
            status (string)
            titel (string)
            omschrijving (string)
            datum_vanaf (date)
            datum_tot (date)
            soort_onderzoek (string)
            locatie (string)
            met_beloning (boolean)
            beloning (string)
            doelgroep_leeftijd_van (integer)
            doelgroep_leeftijd_tot (integer)
            contact_opgenomen (boolean)
            opmerkingen_beheerder (string)



## Bronnen
De bronnen zijn te vinden in een apart bestand genaamd: `bronnen.md`
