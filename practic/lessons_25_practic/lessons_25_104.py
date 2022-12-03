import os

class Something:

    def __new__(cls, *args, **kwargs):
        print(f' __new__ сработал, переданы аргументы: {args, kwargs}')
        instance = super().__new__(cls)
        instance.new_attribute = 'добавлено'
        return instance

    def __init__(self, name, age):
        self.name = name
        self.age = age


class FileObject:
    def __init__(self, filename):
        self.file = open(filename, 'r', encoding='utf8')

    def read_file(self):
        print(self.file.readlines())

    def __del__(self):
        self.file.close()
        del self.file




a =