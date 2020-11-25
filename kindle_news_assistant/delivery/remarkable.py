"""A delivery method for the ReMarkable tablet."""
from datetime import datetime
import click
from rmapy.api import Client
from rmapy.document import ZipDocument
from rmapy.folder import Folder
from .template import DeliveryMethod

DELIVERY_FOLDER = "News Assistant"


class RemarkableDelivery(DeliveryMethod):
    """Delivery method class for the ReMarkable tablet."""

    def __init__(self):
        """Initialize the class by connecting the user to the ReMarkable cloud."""
        self.client = Client()

        if not self.client.is_auth():
            click.confirm(
                "We will need to register with the ReMarkable cloud. \
Please confirm that we may open a webpage.",
                abort=True,
            )
            click.launch("https://my.remarkable.com/connect/remarkable")

            device_token = click.prompt("Please enter the device token below")
            self.client.register_device(device_token)

        self.client.renew_token()

        super().__init__()

    def __str__(self):
        """Return a readable representation of the RemarkableDelivery class.

        :return: The display name of this class.
            Used when choosing this class from a list of options.
        """
        return "ReMarkable"

    def deliver_issue(self, absolute_path: str):
        """Deliver issues to the ReMarkable.

        :param absolute_path: An absolute path for the epub file.
        """
        # Ensure a "News Assistant" folder exists
        collection = self.client.get_meta_items()
        root_folders = [
            f for f in collection if isinstance(f, Folder) and f.Parent == ""
        ]

        delivery_folder_filter = [
            f for f in root_folders if f.VissibleName == DELIVERY_FOLDER
        ]
        if len(delivery_folder_filter) == 0:
            folder = Folder(DELIVERY_FOLDER)
            self.client.create_folder(folder)
            delivery_folder_filter.append(folder)

        delivery_folder = delivery_folder_filter[0]

        # Upload the issue
        document = ZipDocument(doc=absolute_path)
        now = datetime.now()
        document.metadata["VissibleName"] = now.strftime("%d %B, %Y")
        self.client.upload(document, delivery_folder)