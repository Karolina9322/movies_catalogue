Projekt strony internetowej

Strona internetowa prezentuje informacje o filmach, dane pobierane są z serwisu The Movie Database (TNDb).
Wygląd strony oparty został o framework Bootstrap.

Użytkownik na głównej stronie widzi listę 8 filmów z sekcji Popular, przy pomocy dynamicznej listy wyboru może przejść do list: Top rated, Upcoming, Now Playing.
Po wejściu w szczegóły filmu, strona prezentuje dane filmu: obsada, budżet, gatunek, krótki opis.

Na projekt składają się:

main.py - główny widok strony, importuje z pliku tmdb_client.py, wyświetla w listę filmów oraz ich szczegółów przy pomocy szablonów

tmdb_client.py - plik zawierający metody określające sposób pobierania danych: zdjęcia, listy filmów, obsada itd.

index.html, homepage.html, movies_details.html - szablony 
