from something import expensive

class C:
    def __init__(self, x):
        self.x = x

        self.y = expensive(x)
        # ^^^^^^^^^^^^^^^^^^^
