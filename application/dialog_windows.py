import tkinter as tk
from tkinter.messagebox import showerror, showinfo
from multiprocessing import Process, Queue
from tkinter.simpledialog import askstring
from tkinter import filedialog as f
from typing import Any


def show_error_window(title: str, message: str) -> None:
    """Procedura afiseaza o fereastra ce scrie un mesaj de eroare si un titlu.

    Algoritm:
    -----------
    Se efectueaza pasii necesari afisarii casutei de dialog, conform documentatiei tkinter.

    Parametri:
    -----------
    title: str
        titlul ferestrei;
    message: str
        mesajul ce este scris in fereastra.

    Intoarce:
    ----------
    Nimic."""

    root = tk.Tk()
    root.withdraw()
    showerror(title, message)
    root.destroy()


def show_info_window(title: str, message: str) -> None:
    """Procedura afiseaza o fereastra ce scrie un mesaj de informare si un titlu.

    Algoritm:
    -----------
    Se efectueaza pasii necesari afisarii casutei de dialog, conform documentatiei tkinter.

    Parametri:
    -----------
    title: str
        titlul ferestrei;
    message: str
        mesajul ce este scris in fereastra.

    Intoarce:
    ----------
    Nimic."""

    root = tk.Tk()
    root.withdraw()
    showinfo(title, message)
    root.destroy()


def show_string_input_window(title: str, message: str, q: Any) -> None:
    """Procedura afiseaza o fereastra ce solicita introducerea unui sir de caractere, scrie un mesaj explicativ
    si are un titlu.

    Algoritm:
    -----------
    Se efectueaza pasii necesari afisarii casutei de dialog, conform documentatiei tkinter. In plus, textul introdus
    de catre utilizator se extrage cu ajutorul unei cozi. Aceasta va fi folosita intr-o alta functie,
    show_string_input_window_in_thread.

    Parametri:
    -----------
    title: str
        titlul ferestrei;
    message: str
        mesajul ce este scris in fereastra;
    q: Any
        o instanta a unei cozi, ce va retine textul introdus de catre utilizator.

    Intoarce:
    ----------
    Nimic."""

    root = tk.Tk()
    root.withdraw()
    ans = askstring(title, message)
    root.destroy()
    q.put(ans)


def restore_backup_window(q: Any) -> None:
    """Procedura afiseaza o fereastra din care utilizatorul poate selecta un fisier, in acest caz un backup la baza
    de date.

    Algoritm:
    -----------
    Se efectueaza pasii necesari afisarii casutei de dialog, conform documentatiei tkinter. In plus, fisierul
    selectat de catre utilizator, inclusiv calea sa absoluta, se extrage cu ajutorul unei cozi. Aceasta va fi
    folosita intr-o alta functie, restore_backup_window_in_thread.

    Parametri:
    -----------
    q: Any
        o instanta a unei cozi, ce va retine textul introdus de catre utilizator;

    Intoarce:
    ----------
    Nimic."""

    root = tk.Tk()
    root.withdraw()
    ans = f.askopenfilename()
    root.destroy()
    q.put(ans)


def show_error_window_in_thread(title: str, message: str) -> None:
    """Procedura afiseaza o fereastra ce scrie un mesaj de eroare si un titlu, intr-un fir separat de executie.

    Algoritm:
    ----------
    Se apeleaza procedura show_error_window intr-un fir separat.

    Parametri:
    -----------
    title: str
        titlul ferestrei;
    message: str
        mesajul ce este scris in fereastra.

    Intoarce:
    ----------
    Nimic."""

    p = Process(target=show_error_window, args=(title, message))
    p.start()
    p.join()


def show_info_window_in_thread(title: str, message: str) -> None:
    """Procedura afiseaza o fereastra ce scrie un mesaj de informare si un titlu, intr-un fir separat de executie.

    Algoritm:
    ----------
    Se apeleaza procedura show_info_window intr-un fir separat.

    Parametri:
    -----------
    title: str
        titlul ferestrei;
    message: str
        mesajul ce este scris in fereastra.

    Intoarce:
    ----------
    Nimic."""

    p = Process(target=show_info_window, args=(title, message))
    p.start()
    p.join()


def show_string_input_window_in_thread(title: str, message: str) -> str:
    """Functia afiseaza o fereastra ce solicita introducerea unui sir de caractere, scrie un mesaj explicativ
    si are un titlu, intr-un fir separat de executie.

    Algoritm:
    ----------
    Se apeleaza procedura show_string_input_window intr-un fir separat.

    Parametri:
    -----------
    title: str
        titlul ferestrei;
    message: str
        mesajul ce este scris in fereastra.

    Intoarce:
    ----------
    Nimic."""

    queue = Queue()
    p = Process(target=show_string_input_window, args=(title, message, queue))
    p.start()
    p.join()
    ans = queue.get()
    return ans


def restore_backup_window_in_thread() -> str:
    """Functia afiseaza o fereastra din care utilizatorul poate selecta un fisier, in acest caz un backup la baza
    de date.

    Algoritm:
    ----------
    Se apeleaza procedura restore_backup_window intr-un fir separat.

    Parametri:
    -----------
    Niciunul.

    Intoarce:
    ----------
    Un sir de caractere ce contine fisierul backup din care se va reface baza de date, inclusiv calea absoluta
    pana la acesta."""

    queue = Queue()
    p = Process(target=restore_backup_window, args=(queue,))
    p.start()
    p.join()
    ans = queue.get()
    return ans
