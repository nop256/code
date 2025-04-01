

from parent import Electronics

class Smartphone(Electronics):
    """
    A class representing a smartphone with basic attributes and behaviors.

    Attributes:
    ----------
    battery_level : int
        The current battery level, represented as a percentage (0 to 100).
    storage_capacity : float
        The total storage capacity in gigabytes (GB).
    used_storage : float
        The amount of storage currently used in gigabytes (GB).
    brightness : int
        The current brightness level, represented as a percentage (0 to 100).
    installed_apps : list
        A list to store the names of installed apps and their sizes.

    Methods:
    -------
    checkBatteryLevel():
        Returns the current battery level.

    installApp(app_size):
        Installs an application of a given size (in GB) if there is enough available storage. Updates the used storage.

    checkApps():
        Returns a list of installed apps.

    uninstallApp(app):
        Uninstalls the specified app if it exists, freeing up its storage.

    adjustBrightness(level):
        Adjusts the brightness level to a specified percentage.

    to_string():
        Returns a string representation of the current state of the smartphone.
    """



    def __init__(self,battery_level=100,storage_capacity=128.0,brightness=50):
        """
        Initializes a new instance with the given attributes (or defaults).

        Parameters:
        ----------
        battery_level : int, optional
            Initial battery level (default is 100).
        storage_capacity : float, optional
            Total storage capacity in GB (default is 128.0).
        brightness : int, optional
            Initial screen brightness level (default is 50).
        """
        super().__init__(battery_level) # Calls the parent class's constructor
        self.storage_capacity = storage_capacity
        self.used_storage = 0.00
        self.brightness = brightness
        self.installed_apps = []

    def checkStorage(self):
        """

        Returns:
        -------
        str
            Current storage usage out of original maximum storage capacity.
        """
        available_storage = self.storage_capacity - self.used_storage
        percentage_used = (self.used_storage / self.storage_capacity) * 100
        return f"Storage usage: {self.used_storage}/{self.storage_capacity} GB ({percentage_used:.2f}% used)"


    def installApp(self,app_name, app_size):
        """
        Installs an app on the phone if there is enough storage capacity available.
        Reduces the available storage capacity by the size of the app.

        Parameters:
        -----------
        app_name : str
            The name of the app to be installed.
        app_size : float
            The size of the app to be installed in gigabytes (GB).

        Returns:
        -------
        str
            A message indicating whether the app was installed successfully or if there was insufficient storage.
        """
        if app_size <= (self.storage_capacity - self.used_storage):
            self.installed_apps.append((app_name, app_size))
            self.used_storage += app_size
            return f"The app '{app_name}' was installed successfully."
        else:
            return f"You do not have enough available storage to install '{app_name}'."

    def checkApps(self):
        """
        Returns a list of all installed apps.

        Returns:
        -------
        str
            A list of installed apps with their sizes.
        """
        if not self.installed_apps:
            return "You have no apps installed."
        apps_list = "\n".join([f"{app_name} ({size} GB)" for app_name, size in self.installed_apps])
        return f"Installed apps:\n{apps_list}"


    def uninstallApp(self,app_name):
        """
        Uninstalls the specified app, if it exists, freeing up its storage.

        Parameters:
        ----------
        app : str
            The name of the app to uninstall.

        Returns:
        -------
        str
            A message indicating whether the app was uninstalled or if it wasn't found.
        """
        for app, size in self.installed_apps:
            if app == app_name:
                self.installed_apps.remove((app, size))
                self.used_storage -= size
                return f"The app '{app_name}' was uninstalled successfully."
        return f"The app '{app_name}' is not currently installed."


    def adjustBrightness(self,new_brightness):
        """
        Adjusts the screen brightness to a new level.

        Parameters:
        ----------
        new_brightness : int
            The new brightness level to set (0-100):

        Returns:
        -------
        str
            A message indicating the new brightness level.

        """
        if 0 <= new_brightness <= 100:
            self.brightness = new_brightness
            return f"Brightness set to {new_brightness}"
        else: return "Invalid brightness level. Please enter a value between 0 and 100."


    def to_string(self):
        """
        Returns a string representation of the current state of the phone.

        Returns:
        -------
        str
            A string that contains the current battery level, used and total storage, and brightness level.
        """
        electronics_info = super().to_string() # Calls the parent lcass's __str__ method
        apps_list = ', '.join([app for app, _ in self.installed_apps]) or "None"
        return (f"{electronics_info}, "
                f"Storage: {self.used_storage}/{self.storage_capacity} GB, "
                f"Brightness: {self.brightness}%, Installed Apps: {apps_list}")


if __name__ == "__main__":
     s1 = Smartphone()
     print(s1.power_on())
     print(s1.power_off())
     print(s1.checkStorage())
     print(s1.installApp('Angry Birbs', 2.8))
     print(s1.checkApps())
     print(s1.uninstallApp('Angry Birbs'))
     print(s1.adjustBrightness(49))
     print(s1.to_string())
