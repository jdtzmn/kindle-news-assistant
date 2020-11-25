"""A delivery method for the Kindle reader."""
import os
import configparser
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import click
from kindle_news_assistant.safe_open import safe_open
from .template import DeliveryMethod

dirname = os.path.dirname(__file__)
FILENAME = "email.ini"
RELATIVE_PATH = os.path.join("../../userdata/", FILENAME)
absolute_config_path = os.path.join(dirname, RELATIVE_PATH)


class KindleDelivery(DeliveryMethod):
    """Delivery method class for the Kindle reader."""

    def __init__(self):
        """Initialize the class by configuring and connecting to the email client."""
        self.config = configparser.ConfigParser()

        # Initialize the configuration if it has not been set
        self.config.read(absolute_config_path)
        if len(self.config["DEFAULT"]) == 0:
            print(
                "An email configuration has not been set. \
In order to deliver articles, we must connect to an email server. You \
will now be guided through configuring the email details:"
            )
            # Set email sender information
            props = [
                ("host", "What is the email host", None, None),
                ("port", "What is the port", 465, None),
                ("email", "What is the email address", None, None),
                (
                    "password",
                    "What is the password (typing will be hidden)",
                    None,
                    True,
                ),
            ]
            for label, question, default, should_hide in props:
                value = click.prompt(question, default, should_hide)
                self.config["DEFAULT"][label] = str(value)

            # Get kindle email address
            click.confirm(
                f"""We will need your kindle email address to send articles. \
Please:
\n1. Copy the kindle email address for delivery purposes.
2. Navigate to Preferences > Personal Document Settings and add `{self.config["DEFAULT"]["email"]}`
\nLearn more at https://amzn.to/3nVmuBy. Please confirm that we may open Amazon.com \
so you can retrieve your kindle email.""",
                abort=True,
            )
            click.launch("https://amazon.com/mycd")

            kindle_email = click.prompt("Please enter the kindle email below")
            self.config["DEFAULT"]["kindle_email"] = kindle_email

            with safe_open(absolute_config_path, "w") as configfile:
                self.config.write(configfile)

    def __str__(self):
        """Return a readable representation of the KindleDelivery class.

        :return: The display name of this class.
            Used when choosing this class from a list of options.
        """
        return "Kindle"

    @staticmethod
    def convert_issue_to_mobi(book_path: str) -> str:
        """Convert an epub book file to a mobi format for the kindle. \
            Uses calibre command line utility `ebook-convert`.

        :param book_path: The absolute path to the epub file.
        :raises RuntimeError: Raises exception when calibre
            command line tools are not installed.
        :return: The absolute path to the converted mobi file.
        """
        book_directory = os.path.dirname(book_path)
        mobi_path = os.path.join(book_directory, "./issue.mobi")
        exit_code = os.system(f"ebook-convert {book_path} {mobi_path}")

        if exit_code == 32512:
            # Try macOS location
            exit_code = os.system(
                f"/Applications/calibre.app/Contents/MacOS/ebook-convert {book_path} {mobi_path}"
            )
            if exit_code == 32512:
                raise RuntimeError(
                    "Calibre command line tools are not installed. \
Install from https://calibre-ebook.com"
                )

        return mobi_path

    @staticmethod
    def create_book_attachment(book_path: str) -> MIMEBase:
        """Create a MIMEBase attachment containing the book file.

        :param book_path: The path to the epub version of the book.
        :return: The MIMEBase instance to be attached using
            the `message.attach` method.
        """
        mobi_path = KindleDelivery.convert_issue_to_mobi(book_path)

        with safe_open(mobi_path, "rb") as attachment:
            # The content type "application/octet-stream" means that it is a binary file
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode to base64
        encoders.encode_base64(part)

        # Add header
        part.add_header("Content-Disposition", "attachment; filename= issue.mobi")
        return part

    def deliver_issue(self, absolute_path: str):
        """Handle the delivery of a news issue.

        :param absolute_path: An absolute path for the epub file.
        """
        settings = self.config["DEFAULT"]
        subject = "News Assistant New Issue"

        host = settings["host"]
        port = settings["port"]
        email = settings["email"]
        password = settings["password"]
        kindle_email = settings["kindle_email"]

        message = MIMEMultipart()
        message["From"] = email
        message["To"] = kindle_email
        message["Subject"] = subject

        # Add body to email
        body = "This email was generated automatically and meant to be \
received by a kindle email address."
        message.attach(MIMEText(body, "plain"))

        # Convert epub to mobi
        mobi_attachment = self.create_book_attachment(absolute_path)

        # Add attachment and convert to string
        message.attach(mobi_attachment)
        text = message.as_string()

        context = ssl.create_default_context()
        if int(port) == 465:
            # Use SSL
            with smtplib.SMTP_SSL(host, port, context=context) as server:
                server.login(email, password)
                server.sendmail(email, kindle_email, text)
        else:
            # Otherwise use TLS
            with smtplib.SMTP(host, port) as server:
                server.starttls(context=context)
                server.login(email, password)
                server.sendmail(email, kindle_email, text)
