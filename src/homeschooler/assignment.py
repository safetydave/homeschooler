

class Assignment:

    def __init__(self, a):
        self.a = a

    # Neighbours have just one task assigned to a different child
    def neighbours(self, n):
        return [tuple((a + r * (i == j)) % n for i, a in enumerate(self.a))
                for r in range(1, n) for j, _ in enumerate(self.a)]

