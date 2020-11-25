"""General delivery method to choose other delivery methods from a list."""
from os import abort
from typing import List, cast, Optional
from simple_term_menu import TerminalMenu
from .template import DeliveryMethod
from .remarkable import RemarkableDelivery
from .kindle import KindleDelivery

DELIVERY_METHODS: List = [
    cast(DeliveryMethod, RemarkableDelivery),
    cast(DeliveryMethod, KindleDelivery),
]


class GeneralDeliveryMethod(DeliveryMethod):
    """General delivery method."""

    methods: List[str] = [method.__str__(method) for method in DELIVERY_METHODS]

    def __init__(self, method: Optional[str]):
        """Choose a delivery method from a list.

        :param method: The method flag set through a command line interface argument.
        """
        delivery_method_index = (
            self.methods.index(method) if method in self.methods else -1
        )

        if delivery_method_index is -1:
            terminal_menu = TerminalMenu(self.methods)
            print("Please select a delivery method:")
            optional_index = terminal_menu.show()
            delivery_method_index = (
                cast(int, optional_index)
                if isinstance(optional_index, int)
                else abort()
            )

        self.delivery_method: DeliveryMethod = DELIVERY_METHODS[delivery_method_index]()

    def deliver_issue(self, absolute_path: str):
        """Deliver the issue using the selected delivery method.

        :param absolute_path: An absolute path for the epub file.
        """
        self.delivery_method.deliver_issue(absolute_path)
