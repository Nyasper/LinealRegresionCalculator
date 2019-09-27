import numpy as np
import matplotlib.pyplot as plt


class Regresion:
    def __init__(self, xArray, yArray):
        self.x = xArray
        self.y = yArray
        self.m = 0              #Pendiente
        self.b = 0              #Ordenada al origen

    def grafica(self, x_name="X", y_name="Y"):
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.grid()

        x1 = self.x[0]
        y1 = (self.m * self.x[0]) + self.b

        x2 = self.x[-1]
        y2 = (self.m * self.x[-1]) + self.b
        
        plt.plot(self.x, self.y, 'o', label="Datos")
        plt.plot([x1,x2], [y1,y2], color="red", label="Ajuste")
        plt.legend()

        plt.show()

    def regresion(self):
        x0 = np.array([np.ones(self.x.shape[0]), self.x]).T
        B = np.linalg.inv(x0.T @ x0) @ x0.T @ self.y.T

        self.m = B[1]
        self.b = B[0]

        return B

    def recta(self):
        print("la ecuacion de recta de la forma y = mx + b es:", end="\n\n")
        print("\ty = {}x + {}".format(self.m,self.b), end="\n\n")
        print("\tm = {}\tb = {}".format(self.m,self.b))