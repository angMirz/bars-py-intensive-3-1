def read_by_row(file):
    for row in open(file, 'r'):
       if 'ERROR' in row.upper():
        yield row