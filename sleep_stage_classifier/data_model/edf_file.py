import pyedflib


class EDFFile:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None

    def open(self):
        if self.file is None:
            self.file = pyedflib.EdfReader(self.file_path)

    def close(self):
        if self.file is not None:
            self.file._close()
            self.file = None

    def is_open(self):
        return self.file is not None
    
    
    def get_start_time(self):
        self.open()
        return self.file.getStartdatetime()
