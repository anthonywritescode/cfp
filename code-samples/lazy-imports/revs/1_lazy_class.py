import functools

from something import expensive

class C:
    def __init__(self, x):
        self.x = x

    @functools.cached_property
    def y(self):
        return expensive(x)
        # ^^^^^^^^^^^^^^^^^
