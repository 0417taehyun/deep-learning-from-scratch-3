import numpy as np

from step01 import Variable


class Function:
    def __call__(self, input: Variable) -> Variable:
        x = input.data
        y = self.forward(x)
        return Variable(data=y)

    def forward(self, x: np.ndarray) -> np.ndarray:
        raise NotImplemented("not implemented yet")


class Square(Function):
    def forward(self, x):
        return x ** 2
    