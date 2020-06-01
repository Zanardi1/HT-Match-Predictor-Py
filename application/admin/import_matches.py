import global_library
from application import config
from application.admin import add_match as a
from application.xml import create_string as cs
from application.xml import dl_xml_file as dl
from application.xml import xml_parsing as xp


def import_engine(low_end: int, high_end: int) -> None:
    """Procedura introduce in baza de date meciurile din Hattrick care au numerele de identificare
    consecutive, intre doua valori date ca parametri.

    Algoritm:
    ----------
    Pentru fiecare numar de identificare aflat intre cele doua limite:
        1. Descarca fisierul XML care contine datele potrivite;
        2. Citeste datele dorite din fisier;
        3. Adauga aceste date in baza de date.
    La final, salveaza baza de date cu noile inregistrari.

    Parametri:
    ----------
    low_end: int
        limita inferioara a numerelor de identificare. Trebuie sa fie un numar intreg, strict pozitiv;
    high_end: int
        limita superioara a numerelor de identificare. Trebuie sa fie un numar intreg, strict positiv.

    Intoarce:
    ----------
    Nimic."""

    if low_end > high_end:  # Daca valorile sunt transmise inversat, aici ele se inverseaza din nou
        low_end, high_end = high_end, low_end
    for match_id in range(low_end, high_end + 1, 1):
        dl.download_xml_file(file=config['DEFAULT']['PROTECTED_RESOURCE_PATH'],
                             params=cs.create_match_details_string(match_id=match_id),
                             destination_file=global_library.details_savepath)
        match_details = xp.parse_match_details_file(match_id=match_id)
        a.add_a_match(match_details[0], match_details[1], match_details[2], match_details[3], match_details[4],
                      match_details[5], match_details[6], match_details[7], match_details[8], match_details[9],
                      match_details[10], match_details[11], match_details[12], match_details[13], match_details[14],
                      match_details[15], match_details[16])
    a.commit_to_database()
