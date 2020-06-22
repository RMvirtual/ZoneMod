import os
import csv
import re
from GUI import GUI
from Postcode import Postcode
from ZoneModel import ZoneModel
from FileSystemNavigation import FileSystemNavigation

def main():
    """ Driver for the main application to run. """

    gui = GUI()
    gui.check_duplicate_zone_models()

main()