import random
from tkinter import *
from tkinter import ttk


def homo():
    alphabet = {"A": ["Z", "X", "Y", "11"], "B": ["C", "D", "F", "99"]}
    tekst = input("Wpisz teskt do zaszyfrowania: ")
    for x in tekst:
        if x in alphabet.keys():
            sign = random.sample(alphabet[x], 1)
            print(sign[0])


if __name__ == '__main__':
    root = Tk()

    tekst = StringVar()
    token = StringVar()
    wynik = StringVar()


    def veigara(txt, key):
        result = ""

        if txt and key:

            txt = txt.replace(" ", "")
            txt = txt.lower()
            key = key.lower()

            kk = key

            while len(key) < len(txt):
                key = key + kk

            for x, y in zip(txt, key):

                code_x = ord(x) - 97
                code_y = ord(y) - 97

                if code_x < 0:
                    code_x = 26
                if code_y < 0:
                    code_y = 26

                part_result = (code_x + code_y) % 27

                if part_result == 26:
                    part_result = "_"
                else:
                    part_result = chr(part_result + 97)

                result = result + part_result

            wynik.delete(0, END)
            wynik.insert(0, result)
        elif key:
            tekst.insert(0, "Wpisz tekst")
        else:
            token.insert(0, "Wpisz token")


    def de_veigara(wyn, key):
        part_result = ""

        key = key.lower()
        wyn = wyn.lower()

        kk = key

        if key and wyn:

            while len(key) < len(wyn):
                key = key + kk

            for x, y in zip(wyn, key):

                if x == "_":
                    code_x = 26
                else:
                    code_x = ord(x) - 97
                code_y = ord(y) - 97

                if code_x >= code_y:

                    znak = code_x - code_y

                    if znak == 26:
                        part_result = part_result + "_"
                    else:
                        part_result = part_result + chr(znak + 97)
                else:
                    znak = ((27 - abs(code_x - code_y)) % 27)
                    if znak == 26:
                        part_result = part_result + "_"
                    else:
                        part_result = part_result + chr(znak + 97)

            tekst.delete(0, END)
            tekst.insert(0, part_result)

    label1 = ttk.Label(root, text="Wejscie")
    label1.grid(column=1, row=1)
    label2 = ttk.Label(root, text="Token")
    label2.grid(column=3, row=3)
    label3 = ttk.Label(root, text="Wynik")
    label3.grid(column=5, row=1)

    szyfruj = ttk.Button(root, text='Szyfruj', command=lambda: veigara(tekst.get(), token.get()))
    szyfruj.grid(column=2, row=5)
    deszyfruj = ttk.Button(root, text='Deszyfruj', command=lambda: de_veigara(wynik.get(), token.get()))
    deszyfruj.grid(column=5, row=5)
    tekst = ttk.Entry(root, textvariable=tekst)
    tekst.grid(column=1, row=2, columnspan=4, sticky=(N, W, E, S), padx=10, pady=10)

    token = ttk.Entry(root, textvariable=token)
    token.grid(column=2, row=4, columnspan=4, sticky=(N, W, E, S), padx=10, pady=10)

    wynik = ttk.Entry(root, textvariable=wynik)
    wynik.grid(column=5, row=2, columnspan=4, sticky=(N, W, E, S), padx=10, pady=10)

    root.mainloop()
