# Subrutinele necesare descarcarii informatiilor de baza despre utilizatorul conectat

import os

import application.xml.create_string as cs
import application.xml.dl_xml_file as dl

savepath = os.path.abspath('User.xml')


def download_basic_info():
    c = cs.DownloadStringCreator()
    path = c.create_manager_compendium_string()
    dl.download_xml_file(path, savepath)
    return 0
