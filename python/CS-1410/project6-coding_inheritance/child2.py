

from parent import Electronics

class Laptop(Electronics):
    """
    A class representing a laptop, inheriting from Electronics.

    Attributes:
    ----------
    ram_size : int
        Amount of RAM in GB.
    disk_space : float
        Total disk space in GB.
    used_disk_space : float
        The amount of disk space currently used.

    Methods:
    -------
    install_software(software_name, software_size):
        Installs software if there is enough available disk space.
    to_string():
        Returns a string representation of the current state of the laptop.
    """
    def __init__(self, battery_level=100, ram_size=16, disk_space=512.0):
        """
        Initializes a laptop with battery level, RAM size, and disk space.

        Parameters:
        ----------
        battery_level : int, optional
            Initial battery level (default is 100).
        ram_size : int, optional
            Total RAM size in gigabytes (default is 16).
        disk_space : float, optional
            Total disk space in gigabytes (default is 512.0).
        """
        super().__init__(battery_level)
        self.ram_size = ram_size
        self.disk_space = disk_space
        self.used_disk_space = 0.0

    def install_software(self, software_name, software_size):
        """
        Installs software if there is enough available disk space.

        Parameters:
        ----------
        software_name : str
            The name of the software to install.
        software_size : float
            The size of the software in gigabytes.

        Returns:
        -------
        str
            A message indicating whether the software was installed successfully.
        """
        if software_size <= (self.disk_space - self.used_disk_space):
            self.used_disk_space += software_size
            return f"'{software_name}' installed successfully"
        else: return f"Not enough disk space to install {software_name}"

    def to_string(self):
        """
        Returns a string representation of the current state of the laptop.
        """
        electronics_info = super().to_string()
        return (f"{electronics_info}, "
                f"RAM: {self.ram_size} GB, Disk Space: {self.used_disk_space}/{self.disk_space} GB")


if __name__ == "__main__":
    l1 = Laptop()
    print(l1.power_on())
    print(l1.power_off())
    print(l1.install_software('Thonny',3))
    print(l1.to_string())
