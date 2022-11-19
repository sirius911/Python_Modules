import csv
import sys
from unicodedata import name


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.header_fields = None
        try:
            self.file = open(self.filename,'rt', newline='')
        except FileNotFoundError as e:
            print(f"{filename} not found")
            self.file = None

    def __enter__(self):
        if self.file != None:
            read = csv.reader(self.file, delimiter=self.sep, quotechar='\"', quoting=csv.QUOTE_NONE)
            self.data = list(read)
            if self.header:
                self.header_fields = self.data[0]
            self.nb_value = len(self.data[0])

            if not self.corrupted():
                return self
        return None

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file != None:
            self.file.close()


    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:  nested list (list(list, list, ...)) representing the data.
        """
        if self.header:
            return self.data[1+self.skip_top:-self.skip_bottom if self.skip_bottom > 0 else None]
        else:
            return self.data

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        return self.header_fields

    def corrupted(self):
        """return False if th file is not corrupted
        True if corrupted"""

        for lign in self.data:
            if len(lign) != self.nb_value:
                return True
            for data in lign:
                if len(data) == 0:
                    return True
        return False
