from contextlib import contextmanager

@contextmanager
def open_file(name):
    file = open(name, 'w')
    print(len(file.readlines()))
    yield file
    file.close()
