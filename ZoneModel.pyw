import csv
from Postcode import Postcode

class ZoneModel():
    """ Models a collection of postcodes and corresponding zones. """
    
    def __init__(self, name):
        """ Constructor method. """

        self.__name = name.upper()
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
                area_code, district_number = self.split_apart_postcode(
                    postcode)

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

    def get_name(self):
        """ Returns the name of the zone model. """

        return self.__name

    def get_postcode_by_index(self, index):
        """ Returns a Postcode object from the postcodes list based on
        the index position within that list. """

        return self.__postcodes[index]
    
    def get_postcode_by_string(self, postcode_string):
        """ Searches for a postcode found within the postcodes list
        based on its full representation as a string. """

        for postcode in self.__postcodes:        
            if (postcode.get_full_postcode().upper()
                    == postcode_string.upper()):
                print("Match Found: " + postcode.get_full_postcode())
                
                return postcode
        
        print("No match found.")
        
        return None
    
    def get_all_postcodes(self):
        """ Returns the full list of postcodes contained in this
        zone model. """

        return self.__postcodes
    
    def save_zone_model(self):
        """ Saves/overwrites a csv file of the zone model's current
        state. """

        with open(self.get_name() + ".csv", "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter = ",")
            postcodes = self.get_all_postcodes()

            for postcode in postcodes:
                # csvwriter needs a list object to work so creating
                # a list even though only one row.
                row = [postcode.get_full_postcode()]
                
                csv_writer.writerow(row)