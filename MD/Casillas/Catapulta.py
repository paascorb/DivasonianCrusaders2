import numpy as np
import math as m

from MD.Casillas.Casilla import Casilla

class Catapulta(Casilla):

    def __init__(self, hachaDivasonica, identificador, danoProyectiles=15, danoProyectilesVariable=7, curacionAuxiliar=None):
        self.danoProyectiles = danoProyectiles
        self.danoProyectilesVariable = danoProyectilesVariable
        self.identificador = identificador

    def realizarDisparo(self):
        return self.danoProyectiles + m.floor(np.random.rand() * 2 * self.danoProyectilesVariable - self.danoProyectilesVariable)

    def equals(self,casilla):
        return casilla is not None and type(casilla) == type(self) and casilla.identificador() == self.identificador and casilla.identificador() != 0
