from functools import reduce
from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

g = '\033[92m' # vert
b = '\033[94m' # blue
y = '\033[93m' # jaune
r = '\033[91m' # rouge
n = '\033[0m' #gris, couleur normale

def print_result(result_1, result_2):
    """Print the result of ft_map VS map"""

    print(f"* {y}{str(list(result_1)): ^20}{n} | {b}{str(list(result_2)): ^20}{n}  |", end="")
    equal_values = (x1 == x2 for x1, x2 in zip(result_1, result_2))
    if all(equal_values):
        print(f" {g}OK{n} *")
    else:
        print(f" {r}KO{n} *")
    print("*---------------------------------------------------*")

def func(x):
    """function test"""
    try:
        return 1/x
    except:
        pass

def sum(x, y):
    """sum x + y"""
    # print(f"{x} + {y} = {x+y}")
    return x + y

print("********** T E S T    ft_map   vs     map ***********")
print("\n*****************************************************")
s1 = "ft_map()"
s2 = "map()"
print(f"* {y}{s1: ^20}{n} VS {b}{s2: ^20}{n} | VS *")
print("*---------------------------------------------------*")

x = [1, 2, 3, 4, 5]
result_ft = ft_map(lambda dum: dum + 1, x)
result_pyp = map(lambda dum: dum + 1, x)
print_result(result_ft, result_pyp)

x = []
result_ft = ft_map(lambda dum: dum + 1, x)
result_pyp = map(lambda dum: dum + 1, x)
print_result(result_ft, result_pyp)

x = "abc"
result_ft = ft_map(lambda dum: dum + "", x)
result_pyp = map(lambda dum: dum + "", x)
print_result(result_ft, result_pyp)

x = (5, 4, 7, 10)
result_ft = ft_map(lambda dum: dum % 2, x)
result_pyp = map(lambda dum: dum % 2, x)
print_result(result_ft, result_pyp)

x = {5, 2, 9, 12}
result_ft = ft_map(lambda dum: dum % 3, x)
result_pyp = map(lambda dum: dum % 3, x)
print_result(result_ft, result_pyp)

x = {"key":"01", "name":"clorin"}
result_ft = ft_map(lambda dum: "[" + dum + "]", x.values())
result_pyp = map(lambda dum: "[" + dum + "]", x.values())
print_result(result_ft, result_pyp)

x = [2, 5, 0]
try:
    result_ft = ft_map(func, x)
except Exception as e:
    pass
try:
    result_pyp = map(func, x)
except Exception as e:
    pass
print_result(result_ft, result_pyp)

print("*** E R R O R S ***")
x = {5, 2, 9, 12, 0}
try:
    
    print(list(ft_map(lambda dum: dum + ".", x)))
except Exception as e:
    print(f"Error ft_map() : {e}")

try:
    print(list(map(lambda dum: dum + ".", x)))
except Exception as e:
    print(f"Error map() : {e}")

try:
    
    print(list(ft_map(lambda dum: 1 / dum, x)))
except Exception as e:
    print(f"Error ft_map() : {e}")

try:
    print(list(map(lambda dum: 1 / dum, x)))
except Exception as e:
    print(f"Error map() : {e}")

input("Press ENTER to Continue....")
print("\n********** T E S T    ft_filter   vs     filter ***********")
print("\n*****************************************************")
s1 = "ft_filter()"
s2 = "filter()"
print(f"* {y}{s1: ^20}{n} VS {b}{s2: ^20}{n} | VS *")
print("*---------------------------------------------------*")

x = [1, 2, 3, 4, 5]
result_ft = ft_filter(lambda dum: dum % 2, x)
result_py = filter(lambda dum: dum % 2, x)
print_result(result_ft, result_pyp)

x = range(0, 10)
result_ft = ft_filter(lambda dum: dum % 2, x)
result_pyp = filter(lambda dum: dum % 2, x)
print_result(result_ft, result_pyp)

x = "abc"
try:
    result_ft = ft_filter(lambda dum: dum % 2, x)
    print(list(result_ft))
except Exception as e:
    print(e)

try:
    result_pyp = filter(lambda dum: dum % 2, x)
    print(list(result_pyp))
except Exception as e:
    print(e)

input("Press ENTER to Continue....")
print("\n********** T E S T   ft_reduce ***********")
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(f"\nlst = {lst}")
result_ft = ft_reduce(lambda u, v: u + v, lst)
result_pyp = reduce(lambda u, v: u + v, lst)
print(f"ft_reduce(lambda u, v: u + v, lst) = {result_ft} : ", end="")
if result_ft == result_pyp:
    print(f"{g}OK{n}")
else:
    print(f"{r}KO{n}")

x = [1, 2, 3]
print(f"\nx = {x}")
result_ft = ft_reduce(sum, x)
result_pyp = reduce(sum, x)
print(f"ft_reduce(sum, x) = {result_ft} : ", end="")
if result_ft == result_pyp:
    print(f"{g}OK{n}")
else:
    print(f"{r}KO{n}")
    
x = [5, 1, 8, 2, 4, 7]
print(f"\nx = {x}")
result_ft = ft_reduce(lambda x, y:x if x > y else y, x)
result_pyp = reduce(lambda x, y:x if x > y else y, x)
print(f"ft_reduce(lambda x, y:x if x > y else y, x) = {result_ft} : ")
if result_ft == result_pyp:
    print(f"{g}OK{n}")
else:
    print(f"{r}KO{n}")

x = [1, 2, 3]
print(f"\nx = {x}")
print(f"ft_reduce(lambda x, y: x + '.'+y, x, x) = ",end="")
try:
    result_ft = ft_reduce(lambda x, y: x + '.'+y, x)

except Exception as e:
    result_ft = str(e)

try:
    result_pyp = reduce(lambda x, y: x + '.'+y, x)
except Exception as e:
    result_pyp = str(e)

print(f"{result_ft} : ", end="")
if result_ft == result_pyp:
    print(f"{g}OK{n}")
else:
    print(f"{r}KO{n}")
    print(result_ft)
    print(result_pyp)