"""A delivery method for the ReMarkable tablet."""
import os
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

    def __str__(self):
        """Return a readable representation of the RemarkableDelivery class.

        :return: The display name of this class.
            Used when choosing this class from a list of options.
        """
        return "ReMarkable"

    @staticmethod
    def convert_issue_to_pdf(book_path: str) -> str:
        """Convert an epub book file to a pdf format for the remarkable. \
            Uses calibre command line utility `ebook-convert`.

        :param book_path: The absolute path to the epub file.
        :raises RuntimeError: Raises exception when calibre
            command line tools are not installed.
        :return: The absolute path to the converted pdf file.
        """
        book_directory = os.path.dirname(book_path)
        pdf_path = os.path.join(book_directory, "./issue.pdf")
        exit_code = os.system(f"ebook-convert {book_path} {pdf_path}")

        if exit_code == 32512:
            # Try macOS location
            exit_code = os.system(
                f"/Applications/calibre.app/Contents/MacOS/ebook-convert {book_path} {pdf_path}"
            )
            if exit_code == 32512:
                raise RuntimeError(
                    "Calibre command line tools are not installed. \
Install from https://calibre-ebook.com"
                )
        
        return pdf_path

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
        pdf_path = RemarkableDelivery.convert_issue_to_pdf(absolute_path)
        document = ZipDocument(doc=pdf_path)
        now = datetime.now()
        document.metadata["VissibleName"] = now.strftime("%d %B, %Y")
        self.client.upload(document, delivery_folder)
