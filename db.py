# test


class DB(object):
    def __init__(self):
        self.__data = {}

    @property
    def _data(self):
        return self.__data

    @_data.setter
    def _data(self, data):
        self.__data = data

    def __str__(self):
        string = ''
        for key in self._data:
            string += str(self._data[key]) + '\n'
        return string

    def __getitem__(self, item):
        return self._data[item]

    def __contains__(self, item):
        return item in self.__data

    def __setitem__(self, key, value):
        self.__data[key] = value
