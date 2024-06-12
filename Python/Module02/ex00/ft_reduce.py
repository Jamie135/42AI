def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if not callable(function_to_apply):
        raise TypeError("function_to_apply must be a callable")
    if not hasattr(iterable, '__iter__'):
        raise TypeError("iterable must be an iterable")
    
    it = iter(iterable)
    try:
        value = next(it)
    except StopIteration:
        raise TypeError("reduce() of empty sequence with no initial value")
    
    for i in it:
        value = function_to_apply(value, i)
    
    return value


# lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# print(ft_reduce(lambda u, v: u + v, lst))  # Output: "Hello world"
    