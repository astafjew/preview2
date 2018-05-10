from db import DB
import pickle
import os


class PickleDB(DB):
    default_db_filename = 'data.pickle'

    def __init__(self, data=None, filename=default_db_filename):
        DB.__init__(self)
        if data is None:
            data = dict()
        self._data = data
        self.__filename = filename
        self.__makefile()

    def save(self):
        with open(self.__filename, 'wb') as dbfile:
            pickle.dump(self._data, dbfile)

    def load(self):
        with open(self.__filename, 'rb') as dbfile:
            self._data = pickle.load(dbfile)

    def __makefile(self):
        if not os.path.exists(self.__filename):
            # just create file
            with open(self.__filename, 'wb'):
                pass
        

def main():
    # testing
    pickledb = PickleDB({
        'ivan': {'name': 'Ivan', 'age': 24},
        'oleg': {'name': 'Oleg', 'age': 16}})
    pickledb.save()
    pickledb.load()
    print(pickledb)


if __name__ == '__main__':
    main()