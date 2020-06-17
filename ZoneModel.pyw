import csv

class ZoneModel(object):
    """ Models a collection of postcodes and corresponding zones. """
    
    def __init__(self, name):
        """ Constructor method. """
        self.__name = name
        self.__postcodes = None
        self.initialise_postcodes()
    
    def initialise_postcodes(self):
        with open("baseukpostcodes.csv", newline="") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = " ")

            for row in csv_reader:
                print(", ".join(row))
    