from shelvedb import ShelveDB
from person import Person


class ConsoleApp(object):
    def __init__(self, repository):
        self.__repository = repository

    def start(self) -> None:
        while True:
            key = input('\nKey?=>')
            if not key:
                break
            if key in self.__repository:
                record = self.__repository[key]
            else:
                record = Person(name='?', age=0)
            for field in ('name', 'age', 'job', 'pay'):
                currval = getattr(record, field)
                new_text = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
                if new_text:
                    setattr(record, field, eval(new_text))
            self.__repository[key] = record

    def __del__(self) -> None:
        del self.__repository


def main() -> None:
    db = ShelveDB()
    db.load()
    capp = ConsoleApp(db)
    capp.start()


if __name__ == '__main__':
    main()
