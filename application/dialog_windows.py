import tkinter as tk
from tkinter.messagebox import showerror, showinfo
from multiprocessing import Process


def show_error_window(title, message):
    root = tk.Tk()
    root.withdraw()
    showerror(title, message)
    root.destroy()


def show_info_window(title, message):
    root = tk.Tk()
    root.withdraw()
    showinfo(title, message)
    root.destroy()


def show_error_window_in_thread(title, message):
    p = Process(target=show_error_window, args=(title, message,))
    p.start()
    p.join()


def show_info_window_in_thread(title, message):
    p = Process(target=show_info_window, args=(title, message,))
    p.start()
    p.join()
