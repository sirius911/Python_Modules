from typing import Tuple
from unittest.util import strclass


class VectorException(Exception):
    """"Class exception of Vector's Class"""
    def __init__(self, mesg):
        super().__init__(mesg)

class Vector:
    """Object Vector"""

    def __init__(self, data):
        """init class Vector"""
        if type(data) is tuple:
            try:
                if data[0] != int(data[0]) or data[1] != int(data[1]):
                    raise ValueError("ValueError: The Tupple must be with int !")
                a = int(data[0])
                b = int(data[1])
                if a > b:
                    raise ValueError("ValueError: The Tupple is not correct !")
            except Exception:
                    raise ValueError("ValueError: The Tupple is not correct !")
            self.shape = (b - a,1)
            newList = []
            for x in range(a, b):
                newList.append([float(x)])
            self.values = newList
        elif type(data) is list:
            if len(data) == 0:
                raise ValueError("ValueError: The vector must not be empty !")
            if type(data[0]) is not list:
                raise ValueError("ValueError: The vector not good formated !")
            n = len(data[0])
            if len(data) == 1:
                #Row vector of shape 1 * n
                if n == 0:
                    raise ValueError("ValueError: The vector must not be empty !")
            else:
                #column vector of shape n * 1
                if n == 0:
                    raise ValueError("ValueError: a column must not be empty :")
                if n > 1:
                    raise ValueError("ValueError: the Vector class is not a matrices !")
            self.shape = (len(data), n)
            # valid values
            if self.shape[0] == 1:
                for aValider in data[0]:
                    try:
                        float(aValider)
                    except Exception:
                        raise ValueError("ValueError: Values must be a float !")
            else:
                for aValider in data:
                    try:
                        float(aValider[0])
                    except Exception:
                        raise ValueError("ValueError: Values must be a float !")
            self.values = data
        else:
            try:
                if(int(data) <= 0):
                    raise ValueError("ValueError: Vector size must be an int positive !")
            except:
                    raise ValueError("ValueError: Vector size must be an int positive !")
            self.shape = (int(data),1)
            newList = []
            for x in range(int(data)):
                newList.append([float(x)])
            self.values = newList
    def T(self):
        """Returns the transpose vector (i.e. a column vector into a row vector, or a row vector into a column vector"""
        newValue = []
        if self.shape[0] == 1:
            #T() with shape 1 * n -> n * 1
            for x in self.values[0]:
                newValue.append([x])
            self.values = newValue
        else:
            #T() with shape n * 1 -> 1 * n"
            for x in self.values:
                newValue.append(x[0])
            self.values = [newValue]
        self.shape = (self.shape[1], self.shape[0])

    def dot(self, vectorY):
        """return a dot product between two vectors os same shape"""
        if not isinstance(vectorY,Vector) or vectorY.shape != self.shape:
            raise VectorException("VectorException: The dot product must be with a vector of same shape !")
        dot = 0
        if self.shape[0] == 1:
            #dot with shape 1 * n
            for a,b in zip(self.values[0], vectorY.values[0]):
                dot += a * b
        else:
            #dot with shape n * 1
            for a,b in zip(self.values, vectorY.values):
                dot += a[0] * b[0]
        return dot

    def __add__(self, vectorY):
        """addition with a vector of same shape"""
        if not isinstance(vectorY,Vector):
            raise NotImplementedError("NotImplementeError: Addition of a Vector with a scalar is not defined !")
        if vectorY.shape != self.shape:
            raise VectorException("VectorException: the addition must be with a vector of same shape !")
        value = []
        if self.shape[0] == 1:
            #add with shape 1 * n
            for x,y in zip(self.values[0],vectorY.values[0]):
                value.append(x + y)
            return Vector([value])
        else:
            #add with shape n * 1
            for x,y in zip(self.values, vectorY.values):
               value.append([(x[0]) + (y[0])])
            return Vector(value)
    
    def __radd__(self, vectorY):
        """reverse addition with a vector of same shape"""
        if isinstance(vectorY,Vector):
            return self.__add__(vectorY)
        else:
            raise NotImplementedError("NotImplementeError: Addition of a scalar by a Vector is not defined !")

    def __sub__(self, vectorY):
        """substraction with a vector of same shape"""
        if not isinstance(vectorY,Vector):
            raise NotImplementedError("NotImplementeError: Substraction of a Vector by a scalar is not defined !")
        if vectorY.shape != self.shape:
            raise VectorException("VectorException: The substraction must be with a vector of same shape !")
        value = []
        if self.shape[0] == 1:
            #add with shape 1 * n
            for x,y in zip(self.values[0],vectorY.values[0]):
                value.append(x - y)
            return Vector([value])
        else:
            #add with shape n * 1
            for x,y in zip(self.values, vectorY.values):
               value.append([(x[0]) - (y[0])])
            return Vector(value)

    def __rsub__(self, vectorY):
        """ reverse substraction with a vector of same shape"""
        if not isinstance(vectorY,Vector):
            raise NotImplementedError("NotImplementeError: Substraction of a scalar by a Vector is not defined here !")
        if vectorY.shape != self.shape:
            raise VectorException("VectorException: The substraction must be with a vector of same shape !")
        value = []
        if self.shape[0] == 1:
            #add with shape 1 * n
            for x,y in zip(self.values[0],vectorY.values[0]):
                value.append(y - x)
            return Vector([value])
        else:
            #add with shape n * 1
            for x,y in zip(self.values, vectorY.values):
               value.append([(y[0]) - (x[0])])
            return Vector(value)

    def __mul__(self, scalar):
        """multiplication by a scalar"""
        try:
            scalar = float(scalar)
        except:
            raise NotImplementedError("NotImplementedError: Multiplication by something other than a scalar is not defined here !")
        newValue = []
        if self.shape[0] == 1:
            #shape 1 * n
            for x in self.values[0]:
                newValue.append(x * scalar)
            return Vector([newValue])
        else:
            #shape n * 1
            for x in self.values:
                newValue.append([x[0] * scalar])
            return Vector(newValue)

    def __rmul__(self, scalar):
        """revers multiplication by a scalar"""
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        """division by a scalar"""
        try:
            scalar = float(scalar)
        except:
            raise VectorException("VectorException: the scalar must be a number !")
        else:
            if scalar == 0.0:
                # raise ZeroDivisionError("ZeroDivisionError: Division by zero !")
                print("ZeroDivisionError: Division by zero !")
            else:
                newValue = []
                if self.shape[0] == 1:
                    #shape 1 * n
                    for x in self.values[0]:
                        newValue.append(x / scalar)
                    return Vector([newValue])
                else:
                    #shape n * 1
                    for x in self.values:
                        newValue.append([x[0] / scalar])
                    return Vector(newValue)
    
    def __rtruediv__(self, vector):
        """revers division"""
        raise NotImplementedError("NotImplementedError: Division of a scalar by a Vector is not implemented here !")

    def __str__(self):
        """print value of vector"""
        txt ="Vector("
        txt += str(self.values)
        txt += ")"
        return txt

    def __repr__(self):
        return self.__str__()