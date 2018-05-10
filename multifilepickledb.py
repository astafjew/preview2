from db import DB
import pickle
import os
import glob


class MultifilePickleDB(DB):

    default_db_dirname = 'data'

    def __init__(self, data=None, dirname=default_db_dirname):
        db.DB.__init__(self)
        if data is None:
            data = {}
        self._data = data
        self.__dirname = dirname
        self.__makedir()

    def save(self):
        for key in self._data:
            filename = os.path.join(self.__dirname, key + '.pkl')
            with open(filename, 'wb') as dbfile:
                pickle.dump(self._data[key], dbfile)
    
    def load(self):
        filepattern = os.path.join(self.__dirname, '*.pkl')
        for filename in glob.glob(filepattern):
            with open(filename, 'rb') as dbfile:
                key = os.path.basename(filename)[:-4]
                self._data[key] = pickle.load(dbfile)

    def __makedir(self):
        if not os.path.exists(self.__dirname):
            os.mkdir(self.__dirname)


def main():
    # testing
    pickledb = MultifilePickleDB(
        {'ivan': {'name': 'Ivan', 'age': 24},
         'oleg': {'name': 'Oleg', 'age': 16}})
    pickledb.save()
    pickledb.load()
    print(pickledb)


if __name__ == '__main__':
    main()