# HT-Match-Predictor-Py
HT Match Predictor este a aplicație de estimare a sanselor de castig ale unei echipe de fotbal din jocul Hattrick, in functie de evaluarile pe compartimente pe care aceasta le are și de evaluările adversarului, evaluări introduse de către utilizator. Estimarea se bazează pe rezultatele meciurilor anterioare în care echipele ce s-au confruntat atunci au avut aceleași evaluări ca și cele introduse. Deoarece sunt 14 criterii de evaluare, fiecare dintre ele având câte 80 de evaluări, este nevoie de un număr enorm de meciuri pentru a putea obține rezultatele dorite. Versiunile viitoare vor oferi o flexibilitate mai mare în introducerea evaluărilor după care se va căuta, rezultând astfel un număr mai mare de meciuri din care să se caute.

Pentru a estima, se aleg cele 14 criterii de căutare și se face click pe butonul de estimare.

Există două moduri de a folosi acest program: **modul anonim** și **modul conectat**.

Modul anonim poate fi folosit de către oricine, indiferent dacă are sau nu cont de Hattrick. Utilizarea acestui mod este cea mai simplă, introducându-se criteriile mentionate mai sus și efectuând un click pe butonul de estimare.

Modul conectat poate fi folosit de către utilizatorii care au cont pe Hattrick. Acest mod a fost creat pentru a permite acestora să selecteze un meci pe care îl va juca în viitor una dintre echipele sale. În mod automat, evaluările echipei sale din acel meci vor fi încărcate, respectându-se locul unde va juca echipa sa (acasă sau în deplasare). Utilizatorului nu-i mai rămâne decât să aleagă evaluările adversarului pe care el le consideră probabile și să vadă rezultatele obținute. Cu alte cuvinte, modul conectat elimină necesitatea de a introduce evaluările unei echipe (cea a utilizatorului).

Din modul anonim se poate intra în **panoul de control**, care oferă acces la baza de date. Din motive evidente, o singură persoană are aici acces (nu spunem cine).

Aplicația a fost scrisă în limbajul Python, 3.7.4. Codurile sursă se află în dosarul **application**. Structura de dosare a aplicației este următoarea:
1. **admin**. Reține codul sursă pentru panoul de control și funcțiile pe care acesta le oferă: crearea, ștergerea, efectuarea unei copii de siguranță (backup) a bazei de date și înlocuirea bazei de date cu o copie de siguranță;
2. **backup**. Reține copiile de siguranță ale bazei de date făcute de-a lungul timpului. Aplicația nu oferă posibilitatea ștergerii vreunei astfel de copii;
3. **connected**. Reține codul sursă pentru interfața pentru accesarea aplicației din modul conectat;
4. **db**. Este dosarul ce conține baza de date;
5. **estimation**. Este dosarul ce conține codul sursă pentru estimarea șanselor menționate mai sus;
6. **index**. Este dosarul ce conține codul sursă pentru prima pagină, cea care apare la pornirea aplicației;
7. **static** și **templates** sunt două dosare ce conțin imaginile și codul sursă pentru acele părți ale paginii web care sunt comune tuturor paginilor din aplicație. Fiecare pagină care apare pe durata utilizării programului este construită din mai multe părți. Unele sunt comune tuturor paginilor (cele ce apar în aceste două dosare), iar celelalte părți sunt specifice fiecărei funcții;
8. **xml**. Este dosarul ce conține fișierele XML descărcate din Hattrick și funcțiile de parcurgere a acestora și de extragere a datelor necesare.

Fiecare funcție este explicată în codul sursă al acesteia.
