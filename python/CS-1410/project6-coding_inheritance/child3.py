

from child1 import Smartphone

class FoldableSmartphone(Smartphone):
    """
    A class representing a foldable smartphone, inheriting from Smartphone.

    Attributes:
    ----------
    is_folded : bool
        Indicates whether the smartphone is folded.

    Methods:
    -------
    toggle_fold():
        Toggles the foldable state of the smartphone.
    to_string():
        Returns a string representation of the current state of the foldable smartphone.
    """
    def __init__(self, battery_level=100, storage_capacity=128.0, brightness=50, is_folded=False):
        """
        Initializes a foldable smartphone with the given attributes.

        Parameters:
        ----------
        battery_level : int, optional
            Initial battery level (default is 100).
        storage_capacity : float, optional
            Total storage capacity in gigabytes (default is 128.0).
        brightness : int, optional
            Initial screen brightness level (default is 50).
        is_folded : bool, optional
            Indicates whether the phone is folded (default is False).
        """
        super().__init__(battery_level, storage_capacity, brightness)
        self.is_folded = is_folded

    def toggleFold(self):
        """
        Toggles the foldable state of the smartphone between folded and unfolded.

        Returns:
        -------
        str
            A message indicating the current state (folded or unfolded).
        """
        self.is_folded = not self.is_folded
        state = "folded" if self.is_folded else "unfolded"
        return f"The phone is now {state}."

    def to_string(self):
        """
        Returns a string representation of the current state of the foldable smartphone.

        Returns:
        -------
        str
            A s ummary of the foldable smartphone's status, including fold state.
        """
        fold_status = "Folded" if self.is_folded else "Unfolded"
        return (f"{super().to_string()}, Fold State: {fold_status}")


if __name__ == "__main__":
    f1 = FoldableSmartphone()
    print(f1.power_off())
    print(f1.power_on())
    print(f1.installApp('Flappy Birb',3.9))
    print(f1.checkStorage())
    print(f1.checkApps())
    print(f1.uninstallApp('Flappy Birb'))
    print(f1.checkStorage())
    print(f1.adjustBrightness(100))
    print(f1.toggleFold())
    print(f1.to_string())
