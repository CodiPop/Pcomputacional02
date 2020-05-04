import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

m = 10
N = 10
n = 50
Mapa = np.zeros((N,N),dtype=int)
MapaNuevo = np.copy(Mapa)
Vivos = []
Muertos = []

class Game:
    def __init__(self,n,N):
        self.N = N
        cont = 0
        for i in range(0,n):
            X = np.random.randint(0,N-1,dtype=int)
            Y = np.random.randint(0,N-1,dtype=int)
            Mapa[X][Y] = 1
            Vivos.append((X,Y))
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
        Vivos.append(pos)
        if(pos in Muertos):
            Muertos.remove(pos)
        self.actual = Vivos

    def muertes(self,pos):
        x,y = pos
        MapaNuevo[x][y] = 0
        Muertos.append(pos)
        if(pos in Vivos):
            Vivos.remove(pos)
        else:
            print("La posicion i no se encuentra en ",pos)
        self.actual = Vivos

    def Siguiente(self):
        print("Comienza a iterar")
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

    def VerificarMapa(self,N, Mapa, MapaNuevo):
        for i in range(N):
            for col in range(N):
                if not Mapa[i][col] == MapaNuevo[i][j]:
                    return True
        return False



if __name__ == '__main__':
    h = 0
    print(Mapa)
    Juego = iter(Game(n, N))
    print(Mapa)
    running = True
    while running:
        h += 1
        if h == m:
            running = False
        next(Juego)
        Mapa = np.copy(MapaNuevo)
        print(Mapa)

