import wx
from ZoneModel import ZoneModel

class GUI():
    """ GUI for running the main application. """

    def __init__(self):
        self.__app = wx.App(False)
        self.__mode = None

        self.__create_widgets()
        self.__app.MainLoop()
    
    def __create_widgets(self):
        """ Creates the widgets required for the application. """

        # frame for entire window.
        self.__frame = wx.Frame(
            None, 
            size = (1000, 560),
            title = "zoneMod")

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

        # finished button.
        self.__finished_button = wx.Button(
            self.__user_input_panel,
            label = "Finished",
            size = (145, 25),
            pos = (450, 165))

        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__finished_button)

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
            value = "UK Only",
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
        if event.GetEventObject() == self.__submit_button:
            print("Submit button pressed")
        
        elif event.GetEventObject() == self.__skip_button:
            print("Skip button pressed")

        elif event.GetEventObject() == self.__exit_button:
            print("Exit button pressed")
        
        elif event.GetEventObject() == self.__finished_button:
            print("Finished button pressed")

        elif event.GetEventObject() == self.__create_zone_model_button:
            print("Create Zone Model button pressed.")
            if self.__mode == None:
                self.create_zone_model()

        elif event.GetEventObject() == self.__amend_zone_model_button:
            print("Amend Zone Model button pressed")

        elif event.GetEventObject() == self.__export_csv_button:
            print("Export CSV button pressed")

        elif event.GetEventObject() == self.__import_csv_button:
            print("Import CSV button pressed")
    
    def tariff_type_change(self, event):
        print(self.__tariff_type_dropdown_menu.GetValue())
    
    def create_zone_model(self):
        """ Creates a new zone model and prepares the user for data
        entry of postcodes and zones against this new model. """ 
        zm_name_input_box = wx.TextEntryDialog(self.__frame,
            "Please enter the name of the zone model you want to create.")

        if zm_name_input_box.ShowModal() == wx.ID_OK:
            zm_name = zm_name_input_box.GetValue()
            zoneModel = ZoneModel(zm_name)
            zoneModel.save_zone_model()
        
        else:
            print("Text box cancelled")
            self.clear_console_output()
        
        zm_name_input_box.Destroy()
    
    def write_console_output(self, text):
        """ Writes text to the console output screen of the GUI. """

        self.__text_console_output_box.write(text.strip() + "\n")
    
    def clear_console_output(self):
        """ Removes all text from the console output screen of the
        GUI. """
        console_box = self.__text_console_output_box
        print(console_box.PositionToXY(4))
        total_lines = console_box.GetNumberOfLines()

        print("Total Lines: ", total_lines)
        end_position = 0

        for line in range(total_lines):
            print("Line No: ", line)

            # appears to need 2 characters for a line break in terms
            # of position
            line_length = console_box.GetLineLength(line) + 2

            print("Line Length: ", line_length)
            end_position += line_length
        
        print(end_position)
        console_box.Remove(0, end_position)