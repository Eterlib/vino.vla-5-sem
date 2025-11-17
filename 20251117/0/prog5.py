class Counter:
    def __set_name__(self, owner, name):
        self.name = name
        self.value = 0

    def __get__(self, instance, owner=None):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class C:
    counter = Counter()

    def __init__(self):
        self.counter += 1

    def __del__(self):
        self.counter -= 1
