import cgi

import person
import shelvedb
import sys
import os
import form_person_editor as fpe


def main() -> None:
    form = cgi.FieldStorage()

    print('Content-Type: text/html\n')

    sys.path.insert(0, os.getcwd())
    if form['action'].value == 'Fetch':
        try:
            record = fetch(form['key'].value)
            reply(form['key'].value, record)
        except:
            print('<h1>#404 Not Found.</h1><h2>There\'s no {0}.</h2><a href="/people.html">Back</a>'
                  .format(form['key'].value))

    elif form['action'].value == 'Update':
        update(form)


def fetch(key):
    db = shelvedb.ShelveDB()
    db.load()
    return db[key]


def update(form) -> None:
    db = shelvedb.ShelveDB()
    db.load()
    key = form['key'].value
    record: person.Person
    try:
        record = db[key]
    except:
        print('new')
        db[key] = fpe.PersonFormEditor.make(form)
    else:
        record = fpe.PersonFormEditor.edit(record, form)
    db[key] = record
    reply(key, record)


def reply(key, prsn) -> None:
    fieldnames = ('name', 'age', 'job', 'pay')
    with open('peoplecgireply.html', 'r') as replyhtml:
        stringhtml = ''.join(replyhtml.readlines())
        stringhtml= stringhtml.replace('$KEY$', key)
        for field in fieldnames:
            stringhtml = stringhtml.replace('${0}$'.format(field.upper()), str(getattr(prsn, field)))
        print(stringhtml)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
