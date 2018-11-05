

class OpenAddressingHash:

    def __init__(self, table_size=101):
        self.table = [None] * table_size
        self.size = table_size

    def hash(self, val):
        return val % self.size

    def insert(self, val):
        pos = self.hash(val)
        if self.table[pos] is not None:
            asc = 1
            i = 1
            while True:
                new_pos = pos + asc
                if new_pos >= self.size:
                    new_pos -= self.size
                if self.table[new_pos] is None:
                    self.table[new_pos] = val
                    return
                else:
                    i += 1
                    asc = asc + i << 1 - 1
        return

    def find(self, val):
        pos = self.hash(val)
        if self.table[pos] is None:
            return None
        elif self.table[pos] != val:
            asc = 1
            i = 1
            while True:
                new_pos = pos + asc
                if new_pos >= self.size:
                    new_pos -= self.size
                if self.table[new_pos] is None:
                    return None
                elif self.table[new_pos] == val:
                    return new_pos
                else:
                    i += 1
                    asc = asc + i << 1 - 1
        return None
