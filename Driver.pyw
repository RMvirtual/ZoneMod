import os
import csv
import re
from Postcode import Postcode
from ZoneModel import ZoneModel

def main():
    """ Driver for the main application to run. """

    zoneModel = ZoneModel("test")
    postcode = zoneModel.get_postcode_by_index(52)

    print(postcode.get_area_code())


main()