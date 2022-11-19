from decimal import DivisionByZero


def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args: function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return: An iterable.
            None if the iterable can not be used by the function.
    """
    iterable_iter = iter(iterable)
    while 42:
        try:
            yield function_to_apply(next(iterable_iter))
        except StopIteration:
            break
        except Exception as e:
            raise Exception(e)
