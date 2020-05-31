# Subrutinele necesare descarcarii unui fisier XML din Hattrick

from rauth import OAuth1Session

from application import config


def download_xml_file(file, params, destination_file) -> None:
    session = OAuth1Session(consumer_key=config['DEFAULT']['CONSUMER_KEY'],
                            consumer_secret=config['DEFAULT']['CONSUMER_SECRET'],
                            access_token=config['DEFAULT']['ACCESS_TOKEN'],
                            access_token_secret=config['DEFAULT']['ACCESS_TOKEN_SECRET'])
    query = session.get(file, params=params)
    session.close()

    f = open(destination_file, 'w', encoding='utf-8')
    f.write(query.text)
    f.close()
