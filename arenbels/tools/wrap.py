
def wrap(pre=None,post=None):
    """ Standard wrapper for Python functions.
    pre, post are functions


    Usage :

    @wrap(pre,post)
    def other_function(...):
        ...
        ...

    """
    if pre is None:
        def pre(*args,**kwargs):
            pass
    if post is None:
        def post(*args,**kwargs):
            pass
    def wrapper(func):
        def call(*args,**kwargs):
            pre(func,*args,**kwargs)
            result = func(*args,**kwargs)
            post(func,*args,**kwargs)
            return result
        return call
    return wrapper