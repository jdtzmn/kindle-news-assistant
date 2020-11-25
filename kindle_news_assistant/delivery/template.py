"""An abstract class template for an extensible delivery method."""
from abc import ABC, abstractmethod
from typing import NoReturn


class DeliveryMethod(ABC):
    """An abstract class template for a given issue delivery method."""

    def __str__(self):
        """Get the display name of the current class. The recommendation is to set this in the \
        child class, but it is not required.

        :return: The display name of this class. Useful for choosing a delivery method from a list.
        """
        return self.__name__  # pylint: disable=no-member

    @abstractmethod
    def deliver_issue(self, absolute_path: str) -> NoReturn:
        """Handle the delivery of a news issue.

        :param absolute_path: An absolute path for the epub file.
        """
