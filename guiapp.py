import tkinter as tk
import tkinter.messagebox
import db
import person
import shelvedb


class GUIApp(object):
    def __init__(self, repository: db.DB):
        self.__repository = repository
        self.__entries = {}
        self.__fieldnames = ('name', 'age', 'job', 'pay')
        self.__window = self.__make_window()

    def mainloop(self) -> None:
        self.__window.mainloop()

    def __make_window(self) -> tk.Tk:
        window = tk.Tk()
        window.title("People Shelve")
        form = tk.Frame(window)
        form.pack()
        for (ix, label) in enumerate(('key',) + self.__fieldnames):
            lab = tk.Label(form, text=label)
            ent = tk.Entry(form)
            lab.grid(row=ix, column=0)
            ent.grid(row=ix, column=1)
            self.__entries[label] = ent
        tk.Button(window, text='Fetch', command=self.__fetch_record)\
            .pack(side=tk.LEFT)
        tk.Button(window, text='Update', command=self.__update_record)\
            .pack(side=tk.LEFT)
        tk.Button(window, text='Quit', command=window.quit)\
            .pack(side=tk.RIGHT)
        return window

    def __fetch_record(self) -> None:
        key = self.__entries['key'].get()
        try:
            record = self.__repository[key]
        except:
            tkinter.messagebox.showerror(title='Error',
                                         message='No Such Key!')
        else:
            for field in self.__fieldnames:
                self.__entries[field].delete(0, tk.END)
                self.__entries[field].insert(0, repr(getattr(record, field)))

    def __update_record(self) -> None:
        key = self.__entries['key'].get()
        if key in self.__repository:
            record = self.__repository[key]
        else:
            record = person.Person(name='?', age=0)
        for field in self.__fieldnames:
            setattr(record, field, eval(self.__entries[field].get()))
        self.__repository[key] = record

    def __del__(self):
        del self.__repository


def main() -> None:
    dtb = shelvedb.ShelveDB()
    dtb.load()
    app = GUIApp(dtb)
    app.mainloop()
    del app


if __name__ == '__main__':
    main()
