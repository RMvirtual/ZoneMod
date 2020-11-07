import csv
from Postcode import Postcode
from FileSystemNavigation import FileSystemNavigation

class ZoneModel():
    """Models a collection of postcodes and corresponding zones."""
    
    def __init__(self, name, tariff_type):
        """Constructor method."""

        self.__name = name.upper()[0:10]
        self.__postcodes = []
        self.initialise_postcodes(tariff_type)
    
    def initialise_postcodes(self, tariff_type):
        """Sets up the postcodes in the zone model so zones can be
        added to them later. Uses base csv files to make setting them
        up easier. Differentiates which postcodes are generated based
        on tariff type."""

        file_system_navigation = FileSystemNavigation()
        
        postcodes_directory = (
            file_system_navigation.get_postcode_resources_directory())

        if tariff_type == "UK Only" or tariff_type == "UK and SCO":
            with open(postcodes_directory + "baseukpostcodes.csv",
                    newline="") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter = " ")

                for row in csv_reader:
                    postcode = ", ".join(row)
                    area_code, district_number = self.split_apart_postcode(
                        postcode)

                    new_postcode = Postcode(area_code, district_number)
                    self.__postcodes.append(new_postcode)
        
        if tariff_type == "SCO Only" or tariff_type == "UK and SCO":
            with open(postcodes_directory + "basescopostcodes.csv",
                    newline="") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter = " ")

                for row in csv_reader:
                    postcode = ", ".join(row)
                    area_code, district_number = self.split_apart_postcode(
                        postcode)

                    new_postcode = Postcode(area_code, district_number)
                    self.__postcodes.append(new_postcode)

    def split_apart_postcode(self, postcode):
        """Splits apart a full postcode string into area code and
        district number based on first occurence of a numeric character
        (first occurence only to accomodate EC postcodes which have
        trailing alphabetic characters in the district number)."""

        for index, character in enumerate(postcode):
            if character.isnumeric():
                break

        area_code = postcode[0:index]
        district_number = postcode[index:]

        return area_code, district_number

    def get_name(self):
        """Returns the name of the zone model."""

        return self.__name

    def get_postcode_by_index(self, index):
        """Returns a Postcode object from the postcodes list based on
        the index position within that list."""

        return self.__postcodes[index]
    
    def get_postcode_by_string(self, postcode_string):
        """Searches for a postcode found within the postcodes list
        based on its full representation as a string."""

        for postcode in self.__postcodes:
            full_postcode = postcode.get_full_postcode.upper()

            if full_postcode == postcode_string.upper():
                return postcode
        
        return None
    
    def get_all_postcodes(self):
        """Returns the full list of postcodes contained in this
        zone model."""

        return self.__postcodes
    
    def save_zone_model(self):
        """Saves/overwrites a csv file of the zone model's current
        state."""

        file_system_nav = FileSystemNavigation()
        zone_models_directory = file_system_nav.get_zone_models_directory()

        csv_path = zone_models_directory + self.get_name() + ".csv"
        
        with open(csv_path, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter = ",")
            postcodes = self.get_all_postcodes()

            for postcode in postcodes:
                # CsvWriter needs a list object to work so creating
                # a list even though only one row.
                row = [postcode.get_full_postcode(), postcode.get_zone()]

                csv_writer.writerow(row)

    def export_fcl_csv(self):
        """Saves/overwrites a csv file of the zone model in the format
        FCL requires for upload."""

        file_sys_nav = FileSystemNavigation()
        fcl_csv_directory = file_sys_nav.get_fcl_csv_directory()

        fcl_csv_output_path = fcl_csv_directory + self.get_name() + ".csv" 
        
        with open(fcl_csv_output_path, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter = ",")
            postcodes = self.get_all_postcodes()

            for postcode in postcodes:
                # CsvWriter needs a list object to work so creating
                # a list even though only one row.
                row = (
                    ["04", self.get_name(), "GB", postcode.get_zone(),
                    postcode.get_full_postcode()])
                
                csv_writer.writerow(row)