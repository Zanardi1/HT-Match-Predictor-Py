import requests


def download_xml_file(path, target):
    response = requests.get(path)
    with open(target, 'wb') as file:
        file.write(response.content)
