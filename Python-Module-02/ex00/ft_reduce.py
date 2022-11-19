def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
        Args:
            function_to_apply: a function taking an iterable.
            iterable: an iterable object (list, tuple, iterator).
        Return:
            A value, of same type of elements in the iterable parameter.
            None if the iterable can not be used by the function.
    """
    result = iterable[0]
    for i in range(1, len(iterable)):
        try:
            result = function_to_apply(result, iterable[i])
        except Exception as e:
            raise Exception(e)
    return result
