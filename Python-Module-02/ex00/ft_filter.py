def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
        Args: function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
        Return: An iterable.
                None if the iterable can not be used by the function.
    """
    iterable_iter = iter(iterable)
    while 42:
        try:
            elem = next(iterable_iter)
            if function_to_apply(elem):
                yield elem
        except StopIteration:
            break
        except Exception as e:
            raise Exception(e)
