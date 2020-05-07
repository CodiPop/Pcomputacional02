import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import ctypes
import pandas as pd
import seaborn as sns



m = 0
N = 0
n = 0

Mapa = np.zeros((N,N),dtype=int)
MapaNuevo = np.copy(Mapa)
Vivos = []
Muertos = []
Nacimientos = []
Moridos = []

class Game:
    def __init__(self,n,N):
        self.N = N
        cont = 0
        i=0
        while(i<n):
                X = np.random.randint(0,N-1,dtype=int)
                Y = np.random.randint(0,N-1,dtype=int)
                pos = X,Y
                if(pos not in Vivos):
                    Mapa[X][Y] = 1
                    Vivos.append((X,Y))
                    Nacimientos.append((X,Y))
                    i += 1

        print(Mapa)
        self.inicio = Vivos

    def __iter__(self):
        self.actual = self.inicio
        return self

    def __next__(self):
        if len(Vivos) > 0 :
            self.MapaNuevo = MapaNuevo
            Generacion(self.actual,Mapa)
            return self.actual
        else:
            raise StopIteration

class Generacion:
    def __init__(self, anterior, elementos):
        self.actual = anterior
        self.elementos = elementos
        self.NuevoMap = self.Siguiente()
        #
    def vivos(self):
        self.actual = Vivos
        return len(Vivos)
        #
    def nacimientos(self,pos):
        x,y = pos
        MapaNuevo[x][y] = 1
        if pos not in Vivos:

            Vivos.append(pos)
            Nacimientos.append(pos)

        if pos in Muertos:

            Muertos.remove(pos)

        self.actual = Vivos

    def muertes(self,pos):
        x,y = pos

        MapaNuevo[x][y] = 0
        if pos not in Muertos:

            Muertos.append(pos)

        if pos in Vivos:
            Vivos.remove(pos)
            Moridos.append(pos)

        self.actual = Vivos

    def Siguiente(self):
        print("Comienza a iterar")
        Moridos.clear()
        Nacimientos.clear()
        for i in range(N):
            for j in range(N):
                SumaVecinos = self.VecinosVivos((i,j))
                if SumaVecinos < 2 or SumaVecinos > 3:
                    self.muertes((i,j))
                elif SumaVecinos == 3 and self.elementos[i][j] == 0:
                    self.nacimientos((i,j))
                else:
                    MapaNuevo[i][j] = self.elementos[i][j]
        return MapaNuevo

    def VecinosVivos(self,pos):
        SumaVivos = 0
        x,y = pos
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    SumaVivos += self.elementos[((x + i) % N)][((y + j) % N)]
        return SumaVivos


root = Tk()
def main():

    label_1 = Label(root, text="Ingrese el tamaño de la matriz")
    label_2 = Label(root, text="Ingrese la cantidad de celulas vivas")
    label_3 = Label(root, text="Ingrese la cantidad de generaciones")

    Entrada1 = IntVar()
    Entrada2 = IntVar()
    Entrada3 = IntVar()

    entry_1 = Entry(root, textvariable=Entrada1)
    entry_2 = Entry(root, textvariable=Entrada2)
    entry_3 = Entry(root, textvariable=Entrada3)

    label_1.grid(row=0)
    label_2.grid(row=1)
    label_3.grid(row=2)

    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)
    entry_3.grid(row=2, column=1)

    button_1 = Button(root, text="Ingresar Datos", command=lambda: Datos(Entrada1, Entrada2, Entrada3))
    button_1.grid(row=3, column=1, sticky="e", padx=5, pady=5)
    root.mainloop()

Aux1 = 0
Aux2 = 0
Aux3 = 0

def Datos(Na,na,ma):
    print("Entro")
    global Aux1,Aux2,Aux3
    Aux1 = Na.get()
    Aux2 = na.get()
    Aux3 = ma.get()
    root.destroy()
    print(Aux1,Aux2,Aux3)


if __name__ == '__main__':

    main()
    N = Aux1
    n = Aux2
    m = Aux3
    x = [i for i in range(0,m+1)]

    Mapa = np.zeros((N, N), dtype=int)
    MapaNuevo = np.copy(Mapa)
    Vivos = []
    Muertos = []
    h = 0
    print(Mapa)
    Juego = iter(Game(n, N))
    CantidadDeVivos=[]
    CantidadDeMuertos=[]
    CantidadDeMoridos = []
    CantidadDeNacimientos=[]
    CantidadDeVivos.append(len(Vivos))
    CantidadDeNacimientos.append(len(Nacimientos))
    CantidadDeMuertos.append(len(Muertos))
    CantidadDeMoridos.append(len(Moridos))
    print(Mapa)
    running = True
    while running:
        h += 1
        if h == m:
            running = False
        try:
            next(Juego)
            CantidadDeVivos.append(len(Vivos))
            CantidadDeNacimientos.append(len(Nacimientos))
            CantidadDeMuertos.append(len(Muertos))
            CantidadDeMoridos.append(len(Moridos))
            Mapa = np.copy(MapaNuevo)
            print(Mapa)
        except:
            ctypes.windll.user32.MessageBoxW(0,"Se acabo el juego porque se muerieron todas las celulas :C","Fin del Juego",1)
            running = False

    print(CantidadDeVivos)
    print(CantidadDeMuertos)
    print(CantidadDeNacimientos)
    print(CantidadDeMoridos)

    x = [i for i in range(1, len(CantidadDeVivos)+1)]
    print(x)
    df = pd.DataFrame({'CantidadDeVivos': CantidadDeVivos,'CantidadDeNacimientos':CantidadDeNacimientos,'CantidadDeMuertes': CantidadDeMoridos }, index=x)
    plt.figure(figsize=(10, 6))
    ax = df.plot.bar(rot=0)
    plt.show()