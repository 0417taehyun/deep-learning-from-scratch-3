import numpy as np

from step02 import Function


class Exp(Function):
    def forward(self, x):
        return np.exp(x)



if __name__ == "__main__":
    from step01 import Variable
    from step02 import Square


    A = Square()
    B = Exp()
    C = Square()

    x = Variable(data=np.array(0.5))

    # Composite Function
    a = A(x)
    b = B(a)
    y = C(b)

    print(y.data)
