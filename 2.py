def sizer(cls):
    class SizerWrapper(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            object.__setattr__(self, '_size_set', False)
            object.__setattr__(self, '_size_value', None)

        @property
        def size(self):
            if self._size_set:
                return self._size_value
            try:
                return len(self)
            except TypeError:
                try:
                    return abs(self)
                except TypeError:
                    return 0

        @size.setter
        def size(self, value):
            object.__setattr__(self, '_size_set', True)
            object.__setattr__(self, '_size_value', value)

        @size.deleter
        def size(self):
            object.__setattr__(self, '_size_set', False)
            object.__setattr__(self, '_size_value', None)

    SizerWrapper.__name__ = cls.__name__
    SizerWrapper.__qualname__ = cls.__qualname__
    SizerWrapper.__module__ = cls.__module__
    return SizerWrapper
