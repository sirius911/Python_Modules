from telnetlib import VT3270REGIME
from termios import VEOF
from vector import Vector

print("\n*** init with size")
vInt = Vector(4)
print(f"Vector(4) = {vInt}")
print(f"Vector(4).shape = {vInt.shape}")

print("\n*** Init with tupple")
vTupple = Vector((10, 16))
print(f"Vector(10,16) = {vTupple}")
print(f"Vector(10,16).shape = {vTupple.shape}")

# Column vector of shape n - 1
print("\n*** Column Vector ***")
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(f"v1.shape = {v1.shape}")
print(f"v1.values = {v1.values}")
v2 = Vector([[2.0],[1.5],[2.25],[4.0]])
print(f"v2 = {str(v2)}")
add1 = v1 + v2
print(f"v1 + v2 = {str(add1)}")
print(f"(v1+v2).shape = {add1.shape}")
sub1 = v1 - v2
print(f"v1 - v2 = {str(sub1)}")
print(f"(v1-v2).shape = {sub1.shape}")
v1.T()
print(f"v1.T() = {str(v1)}")
v1.T()
print(f"v1.T() = {str(v1)}")
print(f"v1.dot(v2) = {v1.dot(v2)}")
print(f"v1 * 2.0 = {v1 * 2.0}")
print(f"2.0 * v1 = {2.0 * v1}")

print(f"v1 / 5.0 = {v1 / 5.0}")

#Row vector of shape 1 * n
print("\n*** Row Vectors ***")
v3 = Vector([[0.0, 1.0, 2.0, 3.0]])
v4 = Vector([[1.0, 2.0, 3.0, 4.0]])
print(f"v3 = {str(v3)}")
print(f"v4 = {str(v4)}")
add2 = v3 + v4
print(f"v3 + v4 = {str(add2)}")
print(f"(v3+v4).shape = {add2.shape}")
sub2 = v4 - Vector([[1.0, 1.0, 1.0, 1.0]])
print(f"v4 - [[1.0, 1.0, 1.0, 1.0]] = {str(sub2)}")
print(f"(v4-[[1.0, 1.0, 1.0, 1.0]]).shape = {sub2.shape}")

print(f"Vector([[1.0, 3.0]]).dot(Vector([[2.0, 4.0]])) = {Vector([[1.0, 3.0]]).dot(Vector([[2.0, 4.0]]))}")

print(f"v3 * 5.5 = {v3 * 5.5}")
print(f"5.5 * v3 = {5.5 * v3}")

print(f"v3 / 2.5 = {v3 / 2.5}")

print("\n*** Error's gestion ***")
# errors
try:
    print("Vector(-3) -> ", end = "")
    vError = Vector(-3)
except Exception as e:
    print(e)

try:
    print("Vector((15, 12)) -> ", end = "")
    vError = Vector((15, 12))
except Exception as e:
    print(e)

try:
    print("Vector([]) -> ", end = "")
    vError = Vector([])
except Exception as e:
    print(e)

try:
    print("Vector([[],[0.1, 0.2, 0.3, 0.4]]) -> ", end = "")
    vError = Vector([[],[0.1, 0.2, 0.3, 0.4]])
except Exception as e:
    print(e)

try:
    print("Vector([[0.1, 0.2, 0.3, 0.4],[0.1, 0.2, 0.3, 0.4]]) -> ", end = "")
    vError = Vector([[0.1, 0.2, 0.3, 0.4],[0.1, 0.2, 0.3, 0.4]])
except Exception as e:
    print(e)

try:
    print("Vector(\"a\") -> ", end = "")
    vError = Vector("a")
except Exception as e:
    print(e)

try:
    print("Vector([\"a\",\"a\"]) -> ", end = "")
    vError = Vector(["a","a"])
except Exception as e:
    print(e)

try:
    print("Vector([[\"f42.0\"]]) -> ", end = "")
    vError = Vector([["f42.0"]])
except Exception as e:
    print(e)

try:
    print("Vector(\"-42\") -> ", end = "")
    vError = Vector("-42")
except Exception as e:
    print(e)

try:
    print("v1 + v3 = ", end = "")
    print(v1 + v3)
except Exception as e:
    print(e)

try:
    print("v1.dot(v3) = ", end = "")
    print(v1.dot(v3))
except Exception as e:
    print(e)

try:
    print("5.1, + v1 = ", end = "")
    print(5.1 + v1)
except Exception as e:
    print(e)

try:
    print("v1 + 5.6 = ", end = "")
    print(v1 + 5.6)
except Exception as e:
    print(e)

try:
    print("v4 - 5.2 = ", end = "")
    print(v4 - 5.2)
except Exception as e:
    print(e) 

try:
    print("5.2 - v4 = ", end = "")
    print(5.2 - v4)
except Exception as e:
    print(e)

try:
    print("v4 * v1 = ", end = "")
    print(v4 * v1)
except Exception as e:
    print(e)   

try:
    print("5.5 / v1 = ", end = "")
    print(5.5 / v1)
except Exception as e:
    print(e)

try:
    print("v1  / 0.0 = ", end = "")
    print(v1 / 0.0)
except Exception as e:
    print(e) 