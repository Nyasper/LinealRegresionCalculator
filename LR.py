import numpy as np

class LR:
    def __init__(self, xArray, yArray):
        self.x = xArray         #X data
        self.y = yArray         #Y data
        self.m = 0              #Slope
        self.b = 0              #Y-intercept

    def get_m_b(self):
        x0 = np.array([np.ones(self.x.shape[0]), self.x]).T
        B = np.linalg.inv(x0.T @ x0) @ x0.T @ self.y.T

        self.m = B[1]
        self.b = B[0]
