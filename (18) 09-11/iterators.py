class FileIterator():

    def __init__(self, file):
        try:
            self.opened = open(f"{file}", "r")
        except FileNotFoundError:
            print('StopIteration occured, file not found.')
            raise StopIteration
        self.lines = self.opened.read().split('\n')
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter < len(self.lines):
            return self.lines[self.counter]
        else:
            self.opened.close()
            raise StopIteration
