from person import Person


class Manager(Person):
    def __init__(self, name, age, pay):
        super().__init__(name, age, pay, 'manager')

    def give_raise(self, percent, bonus=0.1):
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':
    manager = Manager('Jones', 13, 30000)
    print(manager)
