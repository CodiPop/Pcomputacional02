import os
from tkinter import *

root = Tk()

def main():

    label_1 = Label(root, text="Ingresa a Bono")
    label_2 = Label(root, text="Ingresa a Cornway")
    label_3 = Label(root, text="Ingresa a Markov")

    label_1.grid(row=0)
    label_2.grid(row=1)
    label_3.grid(row=2)

    button_1 = Button(root, text="Bono", command=lambda : os.system('python Bono.py'))
    button_2 = Button(root, text="Cornway", command=lambda :os.system('python Cornway.py'))
    button_3 = Button(root, text="Markov", command=lambda :os.system('python Markov.py'))
    button_1.grid(row=0, column=1, sticky="e", padx=5, pady=5)
    button_2.grid(row=1, column=1, sticky="e", padx=5, pady=5)
    button_3.grid(row=2, column=1, sticky="e", padx=5, pady=5)
    root.mainloop()


if __name__ == '__main__':
    main()