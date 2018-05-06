"""
Simple class for 3D vectors using 'array' of 'float'.
"""

import math
import types
import array as ar     # Python array, not NumPy ndarray

_TINY = 1e-15


class Vector3:
    """Vector of 3 floating point elements, single precision.
    """
    def __init__(self, *args):
        if len(args) == 0:      # no initial arguments
            self.vec = ar.array('f', [0.0, 0.0, 0.0])
        elif len(args) == 1 and type(args[0]) == type([]):
            self.vec = ar.array('f', args[0])
            while len(self.vec) < 3:
                self.vec.append(0.0)
        elif len(args) <= 3:
            self.vec = ar.array('f', [ s for s in args])

        # fill in elements for short array
        while len(self.vec) < 3:
            self.vec.append(0.0)

    def __repr__(self):
        v = []
        for s in self.vec:
            a = abs(s)
            digits = 5
            if a == 0.0:
                pass
            else:
                while a < 1.0:
                    a *= 10.0
                    digits += 1
            v.append(round(s, digits))
        return 'Vector3' + repr(v)

    def __add__(self, other):
        _v = [ x+y for x,y in zip(self.vec,other.vec) ]
        vec = Vector3(_v)
        return vec

    def __sub__(self, other):
        _v = [ x-y for x,y in zip(self.vec,other.vec) ]
        vec = Vector3(_v)
        return vec

    def __mul__(self, other):
        """Multiple two objects: vector * scalar, or vector * vector.
        Return a vector or dot product.
        """
        if isinstance(other, float):
            # vector = vector * scalar
            #print("scalar")
            _v = [ x*other for x in self.vec ]
            vec = Vector3(_v)
            return vec
        elif isinstance(other, Vector3):
            if len(other.vec) != 3:
                raise ValueError('Vector3 __mul__ other not len 3')
            _sum = 0.0
            for x,y in zip(self.vec,other.vec):
                _sum += x*y
            return _sum
        else:
            raise TypeError('Vector3 __mul__ type error')

    def __getitem__(self, ndx):
        """Get value of "self" at index ndx."""
        value = self.vec[ndx]
        return value

    def __setitem__(self, ndx, value):
        """Set value of "self" at index ndx."""
        self.vec[ndx] = value

    # No __div__ in standard operators

    def __abs__(self):
        """Absolute value of vector, i.e., its length."""
        return math.sqrt(self * self)
    def abs(self):
        return self.__abs__()

    def __eq__(self, other):
        # This should probably be max(abs(self), abs(other)) * 1e-12
        return abs(self-other) < _TINY

    def __ne__(self, other):
        return not self == other

def cross(v1, v2):
    c = []
    a = v1.vec
    b = v2.vec
    c.append(a[1]*b[2] - a[2]*b[1])
    c.append(a[2]*b[0] - a[0]*b[2])
    c.append(a[0]*b[1] - a[1]*b[0])
    return Vector3(c)


