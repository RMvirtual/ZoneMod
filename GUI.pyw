import wx

class GUI():
    """ GUI for running the main application. """

    def __init__(self):
        self.__app = wx.App(False)
        self.__create_widgets()
        self.__app.MainLoop()
    
    def __create_widgets(self):
        """ Creates the widgets required for the application. """
        strings = ""
        
        for number in range(50):
            strings += ("Test " + str(number) + "\n")

        self.__frame = wx.Frame(None, size = (1000, 560),
            title = "zoneMod")
        self.__frame.SetBackgroundColour("GREY")
        
        self.__text_console_panel = wx.Panel(self.__frame,
            size = (965, 300),
            pos = (10.0, 10.0))
        
        self.__text_console_output_box = wx.TextCtrl(self.__text_console_panel,
            size = (965, 300),
            style = wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_SIMPLE,
            value= strings)

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
        self.__frame.Bind(wx.EVT_BUTTON, self.test, self.__submit_button)

        self.__skip_button = wx.Button(self.__user_input_panel,
            label = "Skip",
            size = (60, 25),
            pos = (625, 165))
        
        self.__exit_button = wx.Button(self.__user_input_panel,
            label = "Exit",
            size = (60, 25),
            pos = (900, 165))
        
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
        
        self.__amend_zone_model_button = wx.Button(self.__user_input_panel,
            label = "Amend Zone Model",
            size = (145, 25),
            pos = (760, 70))

        self.__export_csv_button = wx.Button(self.__user_input_panel,
            label = "Export Zone Model CSV",
            size = (145, 25),
            pos = (760, 100))

        self.__import_csv_button = wx.Button(self.__user_input_panel,
            label = "Import Zone Model CSV",
            size = (145, 25),
            pos = (760, 130))

        self.__frame.Show()
    
    def test(self, event):
        print(event.GetEventObject())
        if event.GetEventObject() == self.__submit_button:
            print("Submit button pressed")