from numpy import random as nr
from . import exceptions as ex

class Uniform:
    def __init__(self, a, b):
        if not 0 <= a <= b:
            raise ex.ParameterError("Parameters must be 0 <= a <= b")
        self._a = a
        self._b = b

    def generate(self):
        return nr.uniform(self._a, self._b)

class Erlang:
    def __init__(self, shape, scale, reenter_prop):
        self._shape = int(shape)
        self._scale = int(scale)
        self._reenter_prop = int(reenter_prop)

    def generate(self):
        print(nr.gamma(self._shape, self._scale, self._reenter_prop))
        return nr.gamma(self._shape, self._scale, self._reenter_prop)
