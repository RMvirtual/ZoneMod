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

        self.__frame = wx.Frame(None, size = (1000, 560),
            title = "zoneMod")
        self.__frame.SetBackgroundColour("GREY")
        
        self.__text_console_panel = wx.Panel(self.__frame,
            size = (965, 300),
            pos = (10.0, 10.0))
        
        self.__text_console_output_box = wx.TextCtrl(self.__text_console_panel,
            size = (965, 300),
            style = wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_SIMPLE)

        self.__user_input_panel = wx.Panel(self.__frame,
            size = (965, 195),
            pos = (10, 320))
        self.__user_input_panel.SetBackgroundColour("GREY")

        self.__text_console_input_box = wx.TextCtrl(self.__user_input_panel,
            value = "trololololol",
            style = wx.TE_MULTILINE | wx.TE_WORDWRAP | wx.BORDER_SIMPLE,
            size = (750, 160),
            pos = (0, 0))

        self.__submit_button = wx.Button(self.__user_input_panel,
            label = "Submit",
            size = (60, 25),
            pos = (690, 165))
        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__submit_button)

        self.__skip_button = wx.Button(self.__user_input_panel,
            label = "Skip",
            size = (60, 25),
            pos = (625, 165))
        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__skip_button)

        self.__exit_button = wx.Button(self.__user_input_panel,
            label = "Exit",
            size = (60, 25),
            pos = (900, 165))
        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__exit_button)
        
        self.__zone_label = wx.StaticText(self.__user_input_panel,
            label = "Zone Name:",
            pos = (760, 0),
            size = (70, 20),
            style = wx.BORDER_SIMPLE)
        self.__zone_label.SetBackgroundColour("White")

        self.__zone_input_box = wx.TextCtrl(self.__user_input_panel,
            pos = (832 , 0),
            size = (100, 20))

        self.__create_zone_model_button = wx.Button(self.__user_input_panel,
            label = "Create Zone Model",
            size = (145, 25),
            pos = (760, 40))
        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__create_zone_model_button)
        
        self.__amend_zone_model_button = wx.Button(self.__user_input_panel,
            label = "Amend Zone Model",
            size = (145, 25),
            pos = (760, 70))
        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__amend_zone_model_button)

        self.__export_csv_button = wx.Button(self.__user_input_panel,
            label = "Export Zone Model CSV",
            size = (145, 25),
            pos = (760, 100))
        self.__frame.Bind(wx.EVT_BUTTON, self.button_click,
            self.__export_csv_button)

        self.__import_csv_button = wx.Button(self.__user_input_panel,
            label = "Import Zone Model CSV",
            size = (145, 25),
            pos = (760, 130))
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
    
    def create_zone_model(self):
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
        self.__text_console_output_box.write(text.strip() + "\n")
    
    def clear_console_output(self):
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