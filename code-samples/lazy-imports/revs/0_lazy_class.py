from something import expensive

class C:
    def __init__(self, x):
        self.x = x

    @property
    def y(self):
        return expensive(x)
        # ^^^^^^^^^^^^^^^^^
