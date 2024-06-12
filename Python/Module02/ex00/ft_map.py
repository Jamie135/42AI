def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
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
        yield function_to_apply(i)


# x = [1, 2, 3, 4, 5]
# print(list(ft_map(lambda dum: dum + 1, x)))  # Output: [2, 3, 4, 5, 6]
