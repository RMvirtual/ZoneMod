class Postcode(object):
    """ A UK postcode that also allows a zone to be tied to it. """
    
    def __init__(self, area_code, district_number):
        """ Constructor method. """
        self.__area_code = area_code
        self.__district_number = district_number
        self.__zone = None

    def get_area_code(self):
        return self.__area_code
    
    def get_district_number(self):
        return self.__district_number
    
    def get_zone(self):
        return self.__zone
    
    def amend_zone(self, new_zone):
        self.__zone = new_zone