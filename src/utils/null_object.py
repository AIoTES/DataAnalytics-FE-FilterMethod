class Null:
    """ Null objects always and reliably "do nothing." """

    def __init__(self, *args, **kwargs): pass

    def __call__(self, *args, **kwargs): return self

    def __repr__(self): return "Null(  )"

    @staticmethod
    def __nonzero__(): return 0

    def __getattr__(self, name): return self

    def __setattr__(self, name, value): return self

    def __delattr__(self, name): return self
