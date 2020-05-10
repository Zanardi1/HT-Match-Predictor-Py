import global_library
from application.admin import add_match as a
from application.xml import create_string as cs
from application.xml import dl_xml_file as dl
from application.xml import xml_parsing as xp
from application import config
import tkinter as tk
from tkinter.ttk import Progressbar, Button
from multiprocessing import Process, Queue


def show_progress_window(low_end, high_end, match_counter):
    root = tk.Tk()
    progress_bar = Progressbar(root, mode='determinate', orient='horizontal', length=200)
    progress_bar['maximum'] = high_end - low_end
    progress_bar['value'] = match_counter
    progress_bar.pack()
    cancel_button = Button(root, text='Anulare')
    cancel_button.pack()
    root.mainloop()


def import_engine(low_end, high_end):
    file = config['DEFAULT']['PROTECTED_RESOURCE_PATH']
    for match_id in range(low_end, high_end + 1, 1):
        p = Process(target=show_progress_window, args=(low_end, high_end, match_id - low_end))
        p.start()
        p.join()
        params = cs.create_match_details_string(match_id)
        dl.download_xml_file(file, params, global_library.details_savepath)
        match_details = xp.parse_match_details_file(match_id)
        a.add_a_match(match_details[0], match_details[1], match_details[2], match_details[3], match_details[4],
                      match_details[5], match_details[6], match_details[7], match_details[8], match_details[9],
                      match_details[10], match_details[11], match_details[12], match_details[13], match_details[14],
                      match_details[15], match_details[16])
