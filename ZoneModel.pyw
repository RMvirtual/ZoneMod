import csv
from Postcode import Postcode

class ZoneModel(object):
    """ Models a collection of postcodes and corresponding zones. """
    
    def __init__(self, name):
        """ Constructor method. """
        self.__name = name
        self.__postcodes = []
        self.initialise_postcodes()
    
    def initialise_postcodes(self):
        """ Sets up the postcodes in the zone model so zones can be
        added to them later. Uses base csv files to make setting them
        up easier. """

        with open("baseukpostcodes.csv", newline="") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = " ")

            for row in csv_reader:
                postcode = ", ".join(row)
                area_code, district_number = self.split_apart_postcode(postcode)

                new_postcode = Postcode(area_code, district_number)
                self.__postcodes.append(new_postcode)

    def split_apart_postcode(self, postcode):
        """ Splits apart a full postcode string into area code and
        district number based on first occurence of a numeric character
        (first occurence only to accomodate EC postcodes which have
        trailing alphabetic characters in the district number). """

        for index, character in enumerate(postcode):
            if character.isnumeric():
                break
        
        area_code = postcode[0:index]
        district_number = postcode[index:]

        return area_code, district_number
    
    def get_postcode_by_index(self, index):
        return self.__postcodes[index]
