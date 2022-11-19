def what_are_the_vars(*args, **kwargs):
    """
        returns an instance of Class ObjectC
    """
    var = 0
    obj = ObjectC()
    dict = {}

    if len(kwargs) > 0:
        for key, value in kwargs.items():
            dict[key] = value

    if len(args) > 0:
        for idx, value in enumerate(args):
            name_var = "var_" + str(idx)
            if name_var not in dict:
                dict[name_var] = value
                var += 1
            else:
                return None
    for key, value in dict.items():
        setattr(obj, key, value)
    return obj


class ObjectC(object):

    def __init__(self):
        super().__init__()


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)
