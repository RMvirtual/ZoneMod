import copy
import csv
import re
import wx
from FileSystemNavigation import FileSystemNavigation
from ZoneModel import ZoneModel

class GUI():
    """GUI for running the main application."""

    def __init__(self):
        """ Constructor method. """

        self.__app = wx.App(False)
        self.__mode = None
        self.__current_zone_model = None
        self.__current_zone_model_postcodes = None
        self.__master_area_code = None
        self.__tariff_type = "UK Only"

        self.__create_widgets()
        self.__app.MainLoop()
    
    def __create_widgets(self):
        """Creates the widgets required for the application."""

        # frame for entire window.
        self.__frame = wx.Frame(
            None, 
            size = (1000, 560),
            title = "ZoneMod")

        self.__frame.SetBackgroundColour("GREY")

        # text_console display panel for upper half of the application.
        self.__text_console_panel = wx.Panel(
            self.__frame,
            size = (965, 300),
            pos = (10.0, 10.0))

        # text console display.
        self.__text_console_output_box = wx.TextCtrl(
            self.__text_console_panel,
            size = (965, 300),
            style = wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_SIMPLE)

        # user input panel for bottom half of the application.
        self.__user_input_panel = wx.Panel(
            self.__frame,
            size = (965, 195),
            pos = (10, 320))

        self.__user_input_panel.SetBackgroundColour("GREY")

        # text box for user to input data.
        self.__text_console_input_box = wx.TextCtrl(
            self.__user_input_panel,
            value = "trololololol",
            style = wx.TE_MULTILINE | wx.TE_WORDWRAP | wx.BORDER_SIMPLE,
            size = (750, 160),
            pos = (0, 0))

        # submit button.
        self.__submit_button = wx.Button(
            self.__user_input_panel,
            label = "Submit",
            size = (60, 25),
            pos = (690, 165))

        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__submit_button)

        # skip button.
        self.__skip_button = wx.Button(
            self.__user_input_panel,
            label = "Skip",
            size = (60, 25),
            pos = (625, 165))

        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__skip_button)

        # save button.
        self.__save_button = wx.Button(
            self.__user_input_panel,
            label = "Save",
            size = (145, 25),
            pos = (450, 165))

        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__save_button)

        # exit button.
        self.__exit_button = wx.Button(
            self.__user_input_panel,
            label = "Exit",
            size = (60, 25),
            pos = (0, 165))

        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__exit_button)

        # zone name label.
        self.__zone_label = wx.StaticText(
            self.__user_input_panel,
            label = "Zone Name:",
            pos = (760, 0),
            size = (70, 20),
            style = wx.BORDER_SIMPLE)

        self.__zone_label.SetBackgroundColour("White")

        # zone name text box to input zone name.
        self.__zone_input_box = wx.TextCtrl(
            self.__user_input_panel,
            pos = (832 , 0),
            size = (100, 20))

        # tariff type label to indicate what the dropdown box is for.
        self.__tariff_type_label = wx.StaticText(
            self.__user_input_panel,
            label = "Tariff Type:",
            pos = (760, 26.5),
            size = (70, 20),
            style = wx.BORDER_SIMPLE)

        self.__tariff_type_label.SetBackgroundColour("White")       

        # tariff type dropdown box menu.
        self.__tariff_type_dropdown_menu = wx.ComboBox(
            self.__user_input_panel,
            pos = (832 , 25),
            size = (100, 25),
            value = self.get_tariff_type(),
            choices = ["UK Only", "SCO Only", "UK and SCO"],
            style = wx.CB_DROPDOWN | wx.CB_READONLY)
        
        self.__frame.Bind(wx.EVT_COMBOBOX, self.tariff_type_change,
            self.__tariff_type_dropdown_menu)

        # create zone model button.
        self.__create_zone_model_button = wx.Button(
            self.__user_input_panel,
            label = "Create Zone Model",
            size = (145, 25),
            pos = (760, 55))

        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__create_zone_model_button)
        
        # amend zone model button.
        self.__amend_zone_model_button = wx.Button(
            self.__user_input_panel,
            label = "Amend Zone Model",
            size = (145, 25),
            pos = (760, 85))
        
        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__amend_zone_model_button)

        # export zone model csv button.
        self.__export_csv_button = wx.Button(
            self.__user_input_panel,
            label = "Export Zone Model CSV",
            size = (145, 25),
            pos = (760, 115))
        
        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__export_csv_button)

        # import zone model csv button.
        self.__import_csv_button = wx.Button(
            self.__user_input_panel,
            label = "Import Zone Model CSV",
            size = (145, 25),
            pos = (760, 145))
        
        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__import_csv_button)

        self.__frame.Show()
    
    def button_click(self, event):
        """Defines the program's behaviour when the GUI's buttons are
        pressed."""

        # submit button.
        if event.GetEventObject() == self.__submit_button:
            print("Submit button pressed")

            user_input = self.get_user_input()
            self.submit(user_input)

        # skip button.
        elif event.GetEventObject() == self.__skip_button:
            print("Skip button pressed")

        # exit button.
        elif event.GetEventObject() == self.__exit_button:
            print("Exit button pressed")

        # finished button.
        elif event.GetEventObject() == self.__save_button:
            print("Save button pressed")

            self.__current_zone_model.save_zone_model()
            # self.check_zone_model_gaps()
            self.check_duplicate_zone_models()

        # create zone model button.
        elif event.GetEventObject() == self.__create_zone_model_button:
            print("Create Zone Model button pressed.")

            zone_model = self.create_zone_model()

            if zone_model:
                self.clear_console_output()
                self.__current_zone_model = zone_model
                self.__current_zone_model_postcodes \
                    = zone_model.get_all_postcodes()
                self.change_mode("create zone model")

        # amend zone model button.
        elif event.GetEventObject() == self.__amend_zone_model_button:
            print("Amend Zone Model button pressed")

        # export zone model csv button.
        elif event.GetEventObject() == self.__export_csv_button:
            print("Export CSV button pressed")

        # import zone model csv button.
        elif event.GetEventObject() == self.__import_csv_button:
            print("Import CSV button pressed")
    
    def tariff_type_change(self, event):
        """Changes the tariff type based on the current value of the
        tariff type dropdown menu."""

        self.__tariff_type = self.__tariff_type_dropdown_menu.GetValue()

    def get_tariff_type(self):
        """Returns a string representing the current tariff type
        setting."""
        
        return self.__tariff_type

    def get_mode(self):
        """Returns the current mode/operation that the user is
        expected to complete."""

        return self.__mode
    
    def change_mode(self, new_mode):
        """Changes the current mode/operation that the user is
        expected to complete. Valid options are None, "create zone
        model"."""

        modes = [None, "create zone model"]

        for mode in modes:
            if new_mode.lower() == mode:
                self.__mode = new_mode
                
                return

    def get_master_area_code(self):
        return self.__master_area_code
    
    def set_master_area_code(self, new_area_code):
        self.__master_area_code = new_area_code
        self.write_console_output("Master Code set to: " + str(new_area_code))

    def clear_master_area_code(self):
        self.__master_area_code = None
        self.write_console_output("Master Code cleared.")

    def get_user_input(self):
        """Gets the text from the user input box."""
        
        return self.__text_console_input_box.GetValue()

    def clear_user_input(self):
        """Clears the text from the user input box."""

        self.__text_console_input_box.Remove(0, 2000)
    
    def insert_user_input(self, text):
        """Inserts text in the user input box (ie amendments that need
        making)."""

        self.__text_console_input_box.ChangeValue(text)

    def get_zone_input(self):
        """Gets the text from the zone name input box."""
        
        return self.__zone_input_box.GetValue()

    def get_current_zone_model(self):
        return self.__current_zone_model

    def set_current_zone_model(self, zone_model):
        self.__current_zone_model = zone_model

    def check_zone_model_gaps(self):
        """Checks the current zone model's postcodes for missing 
        zones."""
        
        zone_model = self.get_current_zone_model()

        postcodes = zone_model.get_all_postcodes()
        missing_postcodes = []

        for postcode in postcodes:
            if not postcode.get_zone():
                full_postcode = postcode.get_full_postcode()
                missing_postcodes.append(postcode)
                self.write_console_output(full_postcode + " is missing.")

    def submit(self, user_input_data):
        """Submit data to the zone model to be added/amended."""
        
        delimited_user_input_data = self.delimit_input(user_input_data)

        for item in delimited_user_input_data:
            formatted_input = self.detect_user_input_format(item)
            master_area_code = self.get_master_area_code()
            
            area_code, district_numbers, operation_type \
                = self.determine_operation_type(formatted_input, item)

            if operation_type == "start of subset":
                self.set_master_area_code(area_code)

                user_input_data = area_code + district_numbers

                self.submit(user_input_data)
            
            elif operation_type == "end of subset":
                area_code = master_area_code

                user_input_data = area_code + district_numbers
                self.submit(user_input_data)
                self.clear_master_area_code()
            
            elif (operation_type == "numerical only" and master_area_code):
                user_input_data = master_area_code + district_numbers

                self.submit(user_input_data)

            self.amend_postcode_zone(area_code, district_numbers,
                operation_type)
        
    def detect_user_input_format(self, user_input):
        """Determines what type of structure the postcode being
        analysed is is. Dependent upon how many characters in the
        string and what type those individual characters are. Examples
        include L, L1, LA1, LA12, EC2M.

        Returns a string that contains x for every alphabet character
        and 0 for every numeric character, as well as any brackets or
        hyphens that are present indicating a range."""

        # substitute all letters for x's, all numbers for 0, and
        # maintain any hyphens and brackets.
        input_format = re.sub("[a-zA-Z]", "x", user_input)
        input_format = re.sub("[0-9]", "0", input_format)

        self.write_console_output("\nFormat is " + input_format)

        return input_format

    def determine_operation_type(self, formatted_input, original_input):
        """Assesses the state of the formatted user input provided
        along with other modes and variables to determine what
        operation should be performed."""

        specific_characters = ["x0", "x00", "xx0", "xx00", "xx0x"]

        range_between_characters = [
            "x0-0", "x0-00", "x00-0", "x00-00",
            "x0-x0", "x0-x00", "x00-x0", "x00-x00",
            "xx0-0", "xx0-00", "xx00-0", "xx00-00",
            "xx0-xx0", "xx0-xx00", "xx00-xx0", "xx00-xx00"]

        range_after_characters = [
            "x0+", "x00+", "xx0+", "xx00+"]

        numerical_only_characters = [
            "0", "00", "0-0", "0-00", "00-0", "00-00", "0+", "00++"]

        if formatted_input in numerical_only_characters:
            self.write_console_output(original_input + " is numerical only.")
            
            area_code = None
            district_numbers = original_input
            operation_type = "numerical only"            

        # if the area code is 1 character, but contains an open bracket
        # indicating the start of a subset of postcodes.
        elif formatted_input[0:2] == "x(" and formatted_input[-1] != ")":
            self.write_console_output(original_input + " is L( style.")

            area_code = original_input[0]
            district_numbers = original_input[2:]
            operation_type = "start of subset"

        # if it looks like the start of a subset, but only has one
        # set of district numbers in the entire subset.
        elif formatted_input[0:2] == "x(" and formatted_input[-1] == ")":
            self.write_console_output(original_input + " is L(1) style.")

            area_code = original_input[0]
            district_numbers = original_input[2:-1]
            operation_type = "start of subset"
        
        # if the area code is 2 characters, but contains an open
        # bracket indicating the start of a subset of postcodes.
        elif formatted_input[0:3] == "xx(" and formatted_input[-1] != ")":
            self.write_console_output(original_input + " is LA( style.")

            area_code = original_input[0:2]
            district_numbers = original_input[3:]
            operation_type = "start of subset"
        
        # if it looks like the start of a subset, but only has one set
        # of district numbers in the entire subset.
        elif formatted_input[0:3] == "xx(" and formatted_input[-1] == ")":
            self.write_console_output(original_input + " is LA( style.")

            area_code = original_input[0:2]
            district_numbers = original_input[3:-1]
            operation_type = "start of subset"

        # end of a subset
        elif formatted_input[-1] == ")":
            self.write_console_output(original_input
                + "is the end of a subset ).")
            
            area_code = None
            district_numbers = original_input[:-1]
            operation_type = "end of subset"

        # if is a postcode range (see range characters list but as
        # an example L1-L12).
        elif formatted_input in range_between_characters:
            operation_type = "range-between"
            
            if formatted_input[0:2] == "x0":
                self.write_console_output(original_input 
                    + " is L1-range style.")
                
                area_code = original_input[0]
                district_numbers = original_input[1:]

            elif formatted_input[0:2] == "xx":
                self.write_console_output(original_input 
                    + " is L10-range style.")

                area_code = original_input[0:2]
                district_numbers = original_input[2:]
        
        # if is a postcode range of all codes after a certain district
        # (ie L20+ or L1+).
        elif formatted_input in range_after_characters:
            operation_type = "range-after"

            if formatted_input == "x0+":
                self.write_console_output(original_input
                    + "is L1+ style.")
                
                area_code = original_input[0]
                district_numbers = original_input[1]
            
            elif formatted_input== "x00+":
                self.write_console_output(original_input
                    + "is L10+ style.")
                
                area_code = original_input[0]
                district_numbers = original_input[1:3]
            
            elif formatted_input == "xx0+":
                self.write_console_output(original_input
                    + "is LA1+ style.")
                
                area_code = original_input[0:2]
                district_numbers = original_input[2]

            elif formatted_input == "xx00+":
                self.write_console_output(original_input
                    + "is LA10+ style.")
                
                area_code = original_input[0:2]
                district_numbers = original_input[2:4]

        # if is non-district specific covering the entire area of
        # a one or two letter postcode (ie L or WN postcode).
        elif formatted_input == "x" or formatted_input == "xx":
            self.write_console_output(original_input + " covers a full "
                + "postcode.")

            area_code = original_input
            district_numbers = "all"
            operation_type = "all"

        elif formatted_input in specific_characters:
            # if is a district specific postcode consisting of 1 alphabet
            # character and 1 numerical (ie L1 postcode).
            if formatted_input == "x0":
                self.write_console_output(original_input + " is L1 style.")

                area_code = original_input[0]
                district_numbers = original_input[1]
                operation_type = "specific"

            # if the area code is 1 character and the district number is
            # 2 digits (ie L20 postocode).
            elif formatted_input == "x00":
                self.write_console_output(original_input + " is L20 style.")

                area_code = original_input[0]
                district_numbers = original_input[1:3]
                operation_type = "specific"

            # if the area code is 2 characters and the district number
            # is 1 digit (ie WN6 postcode).
            elif formatted_input == "xx0":
                self.write_console_output(original_input + " is WN6 style.")

                area_code = original_input[0:2]
                district_numbers = original_input[2]
                operation_type = "specific"

            # if the area code is 2 characters and the district number is
            # 2 digits (ie LA20 postcode) or 1 digit and 1 alphabetic
            # character (ie London postcodes such as EC2M or WC2H).
            elif formatted_input == "xx00" or formatted_input == "xx0x":
                self.write_console_output(original_input + " is LA20/EC2M style")

                area_code = original_input[0:2]
                district_numbers = original_input[2:4]
                operation_type = "specific"

        else:
            self.write_console_output(original_input + " is not recognised.")
            
            area_code = None
            district_numbers = None
            operation_type = None
        
        return area_code, district_numbers, operation_type

    def delimit_input(self, user_input):
        user_input = "".join(user_input.replace(".",",").strip().split())

        self.write_console_output("Processing " + user_input + "\n")

        delimited_user_input_data = user_input.split(",")

        self.write_console_output("Split into:")

        # remove empty items.
        for item in delimited_user_input_data:
            if item == "":
                self.write_console_output("Blank Item removed")
                delimited_user_input_data.remove(item)
            
            else:
                self.write_console_output(item)
        
        return delimited_user_input_data

    def amend_postcode_zone(self, area_code, district_numbers,
            operation_type):
        zone_model = self.get_current_zone_model()
        postcodes = zone_model.get_all_postcodes()
        new_zone = self.get_zone_input()

        # all postcodes between a specific district range (ie L1-L20).
        if operation_type == "range-between":
            district_range_string = re.sub("[a-zA-Z]", "", district_numbers)
            district_range = district_range_string.split("-")
        
            start_district_number = int(district_range[0])
            end_district_number = int(district_range[1])

            for postcode in postcodes:
                current_area_code = postcode.get_area_code()

                if current_area_code == area_code.upper():
                    current_district_number = int(
                        postcode.get_district_number())
                    
                    if (current_district_number >= start_district_number and
                            current_district_number <= end_district_number):
                        postcode.amend_zone(new_zone)
                        
                        self.write_console_output(postcode.get_full_postcode()
                        + ": " + postcode.get_zone())
        
        # all postcodes after a specific district (ie L10+).
        elif operation_type == "range-after":
            district_range_string = re.sub("[a-zA-Z]+", "", district_numbers)
            start_district_number = int(district_range_string)

            for postcode in postcodes:
                current_area_code = postcode.get_area_code()

                if current_area_code == area_code.upper():
                    current_district_number = int(
                        postcode.get_district_number())
                    
                    if current_district_number >= start_district_number:
                        postcode.amend_zone(new_zone)

                        self.write_console_output(postcode.get_full_postcode()
                        + ": " + postcode.get_zone())

        # specific postcodes to be amended (ie L10 only).
        elif operation_type == "specific":
            district_range_string = re.sub("[a-zA-Z]", "", district_numbers)
            district_number = int(district_range_string)

            for postcode in postcodes:
                current_area_code = postcode.get_area_code()

                if current_area_code == area_code.upper():
                    current_district_number = int(
                        postcode.get_district_number())
                    
                    if current_district_number == district_number:
                        postcode.amend_zone(new_zone)

                        self.write_console_output(postcode.get_full_postcode()
                        + ": " + postcode.get_zone())

        # amend all postcodes in one area.
        elif operation_type == "all":
            for postcode in postcodes:
                current_area_code = postcode.get_area_code()

                if current_area_code == area_code.upper():
                    postcode.amend_zone(new_zone)
                    
                    self.write_console_output(
                        postcode.get_full_postcode() + ": " + new_zone)

    def create_zone_model(self):
        """Creates a new zone model and prepares the user for data
        entry of postcodes and zones against this new model."""

        zone_model = None

        zm_name_input_box = wx.TextEntryDialog(self.__frame,
            "Please enter the name of the zone model you want to create.")

        if zm_name_input_box.ShowModal() == wx.ID_OK:
            zm_name = zm_name_input_box.GetValue()
            zone_model = ZoneModel(zm_name, self.get_tariff_type())
        
        else:
            print("Text box cancelled")
            self.clear_console_output()
        
        zm_name_input_box.Destroy()

        return zone_model

    def check_duplicate_zone_models(self):
        """Checks for any duplicate zone models the user has already
        created to assist with reusing ones already in place."""

        file_system_navigation = FileSystemNavigation()

        zone_models_directory = (
            file_system_navigation.get_zone_models_directory())

        zone_models_directory_items = (
            file_system_navigation.get_directory_items(zone_models_directory))

        current_zone_model = self.get_current_zone_model()
        current_zone_model_name = current_zone_model.get_name() + ".csv"

        for item in zone_models_directory_items:
            if item.endswith(".csv") and item != current_zone_model_name:
                postcodes_to_check = copy.deepcopy(
                    current_zone_model.get_all_postcodes())

                # check length of the csv file against the amount of 
                # postcodes required to check.
                csv_line_length = self.get_csv_line_length(
                    zone_models_directory + item)

                if csv_line_length == len(postcodes_to_check):
                    with open(zone_models_directory + item,
                            newline="") as zone_model_csv:
                        csv_reader = csv.reader(zone_model_csv, 
                            delimiter = ",")

                        for row in csv_reader:
                            postcode_to_test = row[0]
                            zone_to_test = row[1]

                            for postcode in postcodes_to_check:
                                full_postcode = postcode.get_full_postcode()
                                zone = postcode.get_zone()

                                if full_postcode == postcode_to_test:
                                    if zone == zone_to_test:
                                        postcodes_to_check.remove(postcode)
                
                else:
                    self.write_console_output("Difference in amount of "
                    + "postcodes between current zone model and "
                    + item)

                if postcodes_to_check:
                    self.write_console_output(item + " does not match.")

                else:
                    self.write_console_output(item + " matches.")

    def get_csv_line_length(self, csv_file_location):
        """Returns the amount of rows found in a CSV file."""

        with open(csv_file_location, newline="") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ",")
            row_amount = len(list(csv_reader))

            return row_amount

    def write_console_output(self, text, newline = True):
        """Writes text to the console output screen of the GUI."""
        
        if newline == False:
            self.__text_console_output_box.write(text)
        
        else:
            self.__text_console_output_box.write(text + "\n")
        
    def clear_console_output(self):
        """Removes all text from the console output screen of the
        GUI."""
        console_box = self.__text_console_output_box
        total_lines = console_box.GetNumberOfLines()

        end_position = 0

        for line in range(total_lines):
            # appears to need 2 characters for a line break in terms
            # of position
            line_length = console_box.GetLineLength(line) + 2
            end_position += line_length

        console_box.Remove(0, end_position)