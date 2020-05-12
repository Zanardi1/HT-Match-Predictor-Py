import tkinter
import threading
from tkinter.ttk import Progressbar, Button

import global_library
from application import config
from application.admin import add_match as a
from application.xml import create_string as cs
from application.xml import dl_xml_file as dl
from application.xml import xml_parsing as xp


class ProgressWindow:
    def __init__(self):
        self.high_end = 0
        self.low_end = 0
        self.root = tkinter.Tk()
        self.progress_bar = Progressbar(self.root, mode='determinate', orient='horizontal', length=200)
        self.progress_bar['maximum'] = self.high_end - self.low_end
        self.progress_bar['value'] = 0
        self.progress_bar.pack()
        self.cancel_button = Button(self.root, text='Anulare')
        self.cancel_button.pack()

    def update(self, value):
        self.progress_bar['value'] = value


# def show_progress_window(low_end, high_end, match_count):
#     root = tk.Tk()
#
#     root.mainloop()


def import_engine(low_end, high_end):
    progress_window = ProgressWindow()
    file = config['DEFAULT']['PROTECTED_RESOURCE_PATH']
    thread = threading.Thread(target=progress_window, args=(low_end, high_end, 0))
    thread.start()
    for match_id in range(low_end, high_end + 1, 1):
        progress_window.update(match_id)
        params = cs.create_match_details_string(match_id)
        dl.download_xml_file(file, params, global_library.details_savepath)
        match_details = xp.parse_match_details_file(match_id)
        a.add_a_match(match_details[0], match_details[1], match_details[2], match_details[3], match_details[4],
                      match_details[5], match_details[6], match_details[7], match_details[8], match_details[9],
                      match_details[10], match_details[11], match_details[12], match_details[13], match_details[14],
                      match_details[15], match_details[16])
    progress_window.root.mainloop()
