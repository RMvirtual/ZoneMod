import os

class FileSystemNavigation():
    """Class for navigating to correct folder directories for this
    program."""

    def get_current_path(self):
        """Gets the full current working path the file using this
        method resides in."""

        return os.getcwd()
    
    def get_directory_items(self, path):
        """Returns a list of folders and files in a directory."""
        return os.listdir(path)

    def get_directory_path(self):
        """Gets the directory path of the ZoneMod folder that all the files
        and subfolders reside in."""

        current_path = self.get_current_path()

        directory_structure = current_path.split("\\")
        directory_path = ""

        for folder in directory_structure:
            print(folder)
            directory_path += folder + "\\"

            if folder == "ZoneMod":
                break
        
        return directory_path

    def get_resources_directory(self):
        """Returns the path of the resources folder that resides in
        the src/main directory of the ZoneMod directory."""

        return self.get_directory_path() + "src\\main\\resources\\"
    
    def get_postcode_resources_directory(self):
        """Returns the path of the postcodes subfolder in the resources
        directory."""

        return self.get_resources_directory() + "postcodes\\"

    def get_zone_models_directory(self):
        """Returns the path of the postcodes subfolder in the resources
        directory."""

        return self.get_resources_directory() + "zonemodels\\"