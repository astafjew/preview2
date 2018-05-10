class Person(object):
    def __init__(self, name: str, age: int, pay: int = 0, job: str = None):
        self.__name = name
        self.__age = age
        self.__pay = pay
        self.__job = job

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
        self.__age = value

    @property
    def pay(self) -> int:
        return self.__pay

    @pay.setter
    def pay(self, value: int) -> None:
        self.__pay = value

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, value: str) -> None:
        self.__job = value

    @property
    def lastname(self) -> str:
        return self.name.split()[-1]

    def give_raise(self, percent: float) -> None:
        self.__pay *= (1.0 + percent)

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        class_attrs = self.__dict__
        string = '> {0}\n'.format(class_name)
        for attr in class_attrs:
            attr_title = attr
            if self.__is_private_attr(attr_title):
                attr_title = self.__format_attr_title(attr)
            else:
                attr_title = attr_title.capitalize()
            string += '  {0}: {1}\n'.format(attr_title, class_attrs[attr])
        return string

    @staticmethod
    def __is_private_attr(attr: str) -> bool:
        class_name = 'Person'
        return attr.startswith('_{0}'.format(class_name))

    @staticmethod
    def __format_attr_title(attr: str) -> str:
        class_name = 'Person'
        attr_title = attr.replace('_', ' ')
        attr_title = attr_title[len(class_name) + 1:].strip().capitalize()
        return attr_title


def main():
    # testing
    person = Person('Ivan', 17)
    print(person)


if __name__ == '__main__':
    main()
