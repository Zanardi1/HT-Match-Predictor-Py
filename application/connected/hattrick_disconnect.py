import tkinter as tk
from multiprocessing import Process
from tkinter.messagebox import showinfo

import global_library
from application import config
from application.xml import dl_xml_file as d


def show_disconnect_window():
    root = tk.Tk()
    root.withdraw()
    showinfo("Disconnection successful!", "You are disconnected from your Hattrick account!")
    root.destroy()


def disconnection_engine():
    d.download_xml_file(config['DEFAULT']['INVALIDATE_TOKEN_PATH'], {}, global_library.disconnect_savepath)
    config.remove_option('DEFAULT', 'ACCESS_TOKEN')
    config.remove_option('DEFAULT', 'ACCESS_TOKEN_SECRET')
    with open(global_library.configuration_file, 'w') as configfile:
        config.write(configfile)
    p = Process(target=show_disconnect_window)
    p.start()
    p.join()
