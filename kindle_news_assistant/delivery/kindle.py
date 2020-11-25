"""A delivery method for the Kindle reader."""
from .template import DeliveryMethod


class KindleDelivery(DeliveryMethod):
    """Delivery method class for the Kindle reader."""

    def __str__(self):
        """Return a readable representation of the KindleDelivery class.

        :return: The display name of this class.
            Used when choosing this class from a list of options.
        """
        return "Kindle"

    def deliver_issue(self, absolute_path: str):
        """Handle the delivery of a news issue.

        :param absolute_path: An absolute path for the epub file.
        """
        print("Not implemented yet.")
