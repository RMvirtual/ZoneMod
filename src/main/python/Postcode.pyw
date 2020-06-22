class Postcode():
    """ A UK postcode that also allows a zone to be tied to it. """
    
    def __init__(self, area_code, district_number):
        """ Constructor method. """
        self.__area_code = area_code.upper()
        self.__district_number = district_number
        self.__zone = ""

    def get_area_code(self):
        """ Returns the area code (ie PO42 would return PO). """
        
        return self.__area_code
    
    def get_district_number(self):
        """ Returns the district number (ie PO42 would return 42). """
        
        return self.__district_number

    def get_zone(self):
        """ Returns the name of the zone that the postcode belongs
        to. """

        return self.__zone
    
    def get_full_postcode(self):
        """ Returns the full postcode representation (ie PO42 would
        return PO42 in full). """

        return self.__area_code.strip() + self.__district_number.strip()

    def amend_zone(self, new_zone):
        """ Amends the zone of this postcode to a string representation
        of a zone. """
        
        self.__zone = new_zone.upper()