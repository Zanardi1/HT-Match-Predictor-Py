import easygui
import application.dl_xml_file as d
import application.create_string as c


def download_basic_info():
    download_string = c.DownloadStringCreation()
    filename = download_string.create_manager_compendium_string(1187457)
    d.download_xml_file(filename, 'manager.xml')
    return 0
