import os
import csv
from Postcode import Postcode

def main():
    """ Driver for the main application to run. """
    print("Hello world.")
    ab42_postcode = Postcode("AB", 42)
    print(ab42_postcode.get_area_code())
    input("Press enter to exit.")

main()