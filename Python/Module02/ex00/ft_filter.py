def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError("The function must be a callable")
    if not hasattr(iterable, '__iter__'):
        raise TypeError("The object must be an iterable")
    for i in iterable:
        if function_to_apply(i):
            yield i


# x = [1, 2, 3, 4, 5]
# print(list(ft_filter(lambda dum: not (dum % 2), x)))  # Output: [2, 4]
