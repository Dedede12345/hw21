import re


class Par(str):

    def __init__(self, txt: str):
        super(Par, self).__init__()
        self.elements = txt.split('. ')

    @property
    def txt(self):
        return '. '.join(self.elements)

    # @txt.setter
    # def txt(self, new_txt):
    #     self._txt = new_txt
    #
    # @txt.getter
    # def txt(self):

    def __add__(self, other):
        return self + other

    def flen(self):
        return sum(tuple(map(len, self.elements)))

    def __eq__(self, other):
        return self.flen() == len(other)

    def __neg__(self):
        return self[::-1]

    def __len__(self):
        return len(self.elements)

    def repr(self):
        return repr(self)

    def __str__(self):
        return self.txt

    def __getitem__(self, key):
        return self.elements[key]

    def __setitem__(self, key, value):
        self.elements[key] = value

    def append(self, value):
        return self.elements.append(value)

    def __reversed__(self):
        return self.elements[::-1]


class Word(Par):

    def __init__(self, text):
        super(Par, self).__init__(text)
        self._txt = text

    def __len__(self):
        return len(self._txt)

    def __str__(self):
        return str(self._txt)

    def __repr__(self):
        return repr(self._txt)

    @property
    def txt(self):
        return self._txt

    def __eq__(self, other):
        return len(self.txt) == len(other)

    def __getitem__(self, key):
        return self._txt[key]

    def __setitem__(self, key, value):
        self._txt = self._txt[:key] + value + self._txt[key+1:]


par = Par('Dasdfasdf asdf. Dsafs.')
print(par.elements)
print(len(par))
print(par[0])
par[1] = '0000000000000000.'
print(par)