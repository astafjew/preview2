import person as prsn


class PersonFormEditor(object):
    @staticmethod
    def edit(person, form) -> prsn.Person:
        person_keys = ('name', 'age', 'job', 'pay')
        for key in person_keys:
            setattr(person, key, form[key].value)
        return person

    @staticmethod
    def make(form) -> prsn.Person:
        return prsn.Person(form['name'].value,
                           form['age'].value,
                           form['pay'].value,
                           form['job'].value)

