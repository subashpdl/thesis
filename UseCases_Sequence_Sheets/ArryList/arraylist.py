class ArrayList:
    def __init__(self):
        self._data = []

    def add(self, item):
        self._data.append(item)

    def insert(self, index, item):
        self._data.insert(index, item)

    def get(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of bounds")
        return self._data[index]

    def remove(self, item):
        if item in self._data:
            self._data.remove(item)
        else:
            raise ValueError(f"{item} not in list")

    def size(self):
        return len(self._data)

