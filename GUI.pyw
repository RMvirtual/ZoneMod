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
        
        self.__text_console_output = wx.TextCtrl(self.__text_console_panel,
            size = (965, 300),
            style = wx.TE_MULTILINE | wx.TE_READONLY, value= strings)

        self.__user_input_panel = wx.Panel(self.__frame,
            size = (965, 195),
            pos = (10, 320))
        self.__user_input_panel.SetBackgroundColour("GREY")

        self.__txt_box = wx.TextCtrl(self.__user_input_panel,
            value = "trololololol",
            style = wx.TE_MULTILINE | wx.TE_WORDWRAP,
            size = (750, 160),
            pos = (0, 0))

        self.__submit_button = wx.Button(self.__user_input_panel,
            label = "Submit",
            size = (60, 25),
            pos = (690, 165))

        self.__skip_button = wx.Button(self.__user_input_panel,
            label = "Skip",
            size = (60, 25),
            pos = (625, 165))
        
        self.__exit_button = wx.Button(self.__user_input_panel,
            label = "Exit",
            size = (60, 25),
            pos = (900, 165))

        self.__frame.Show()