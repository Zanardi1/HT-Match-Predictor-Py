# Subrutinele necesare descarcarii unui fisier XML din Hattrick

from rauth import OAuth1Session

from application import config


def download_xml_file(file: str, params: dict, destination_file: str) -> None:
    """Procedura descarca un fisier XML si-l salveaza pe hard-disk.

    Algoritm:
    -----------
    Se creaza o instanta a clasei OAuth1Session, care se ocupa de conectarea la Hattrick. Odata conexiunea realizata,
    se face o cerere pentru fisierul transmis ca parametru, cu parametrii transmisi tot ca parametru. Odata ce sunt
    obtinute datele dorite, se inchide conexiunea iar datele sunt salvate intr-un fisier text, in format XML, in
    folderul xml, cu numele transmis ca parametru.

    Parametri:
    -----------
    file: str
        retine numele fisierului de pe serverul Hattrick, ce va fi descarcat;
    params: dict
        un dictionar ce contine parametri care vor fi transmisi serverului Hattrick, utili la alegerea numai a
        anumitor date ce vor fi incluse in fisierul care ve fi descarcat;
    destination_file: str
        numele fisierului ce va fi salvat pe hard-disk.

    Intoarce:
    ----------
    Nimic."""

    session = OAuth1Session(consumer_key=config['DEFAULT']['CONSUMER_KEY'],
                            consumer_secret=config['DEFAULT']['CONSUMER_SECRET'],
                            access_token=config['DEFAULT']['ACCESS_TOKEN'],
                            access_token_secret=config['DEFAULT']['ACCESS_TOKEN_SECRET'])
    query = session.get(file, params=params)
    session.close()

    f = open(destination_file, 'w', encoding='utf-8')
    f.write(query.text)
    f.close()
