# Subrutinele necesare descarcarii informatiilor de baza despre utilizatorul conectat

import os

import easygui

import application.xml.create_string as cs
import application.xml.dl_xml_file as dl

savepath = os.path.abspath('xml\\User.xml')


def download_basic_info():
    params = cs.create_manager_compendium_string()
    dl.download_xml_file(params, savepath)
    return 0
