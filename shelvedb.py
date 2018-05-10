import shelve
from db import DB
import os


class ShelveDB(DB):
    default_db_filename = os.path.join('shelve_data', 'shelvedb')

    def __init__(self, data=None, filename=default_db_filename):
        DB.__init__(self)
        if data is None:
            data = {}
        self._data = data
        self.__filename = filename
        self.__makedir()

    def save(self):
        with shelve.open(self.__filename) as filedb:
            filedb.update(self._data)

    def load(self):
        with shelve.open(self.__filename) as filedb:
            self._data = dict(filedb)

    def __makedir(self):
        dirname = os.path.dirname(self.__filename)
        if not os.path.exists(dirname):
            os.mkdir(dirname)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.save()

    def __del__(self):
        self.save()


def main():
    import person

    # testing
    pickledb = ShelveDB({
            'oleg': person.Person('Oleg', 16, 35000, 'designer'),
            'ivan': person.Person('Ivan', 33, 78000, 'programmer')
    })
    pickledb.save()
    pickledb.load()
    print(pickledb)


if __name__ == '__main__':
    main()
