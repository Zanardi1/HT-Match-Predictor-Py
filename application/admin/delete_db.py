import os
import tkinter as tk
from tkinter.messagebox import showwarning, showinfo

from sqlalchemy_utils import drop_database


# TODO fereastra de dialog dispare, odata cu root
def delete_database():
    folder = os.getcwd()
    db_path = ''.join([folder, '\\application\\db\\matches.db'])
    db_uri = 'sqlite:///{}'.format(db_path)
    root = tk.Tk()
    root.withdraw()
    if os.path.exists(db_path):
        drop_database(db_uri)
        showinfo('Succes!', 'Baza de date a fost stearsa')
    else:
        showwarning('Esec', 'Baza de date nu exista!')
    root.destroy()
