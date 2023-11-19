# Django
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
# from django.core.mail import send_mail


# send emails with django
class MailService:
    """
    A class to handle email sending using Django's EmailMultiAlternatives.

    This class encapsulates functionalities to compose and send emails with HTML content.

    Attributes:
        subject (str): The subject of the email.
        message (str): The main message body of the email.
        to_email (list[str] or str): The list of email addresses to send the email.

    Methods:
        __init__(subject, message, from_email, to_email):
            Initializes the MailService instance with necessary email details.
        send_mail_with_html(html_content):
            Sends an HTML-formatted email.

    Usage:
        mail_service = MailService(
            'Subject of the email',
            'Main message body',
            'sender@example.com',
            ['recipient1@example.com', 'recipient2@example.com']
        )
        mail_service.send_mail_with_html('<p>This is an HTML formatted email.</p>')
    """

    def __init__(
            self, subject: str,
            to_email,
            message: str = '') -> None:
        """
        Initializes the MailService instance.

        :param str subject: Subject of the email
        :param str message: Message of the email
        :param list[str] or str to_email: List of emails to send
        """

        self.subject = subject
        self.message = message
        self.to_email = to_email

        if isinstance(self.to_email, str):
            self.to_email = [self.to_email]

        if isinstance(self.to_email, list):
            self.to_email = self.to_email

        self.fetch_email_service = EmailMultiAlternatives(
            self.subject,
            self.message,
            settings.EMAIL_HOST_USER,  # from_email
            self.to_email
        )

    def send_mail_with_html(self, html_content) -> None:
        """
        Sends an HTML-formatted email.

        :param str html_content: HTML content of the email
        """
        email = self.fetch_email_service

        email.attach_alternative(html_content, "text/html")
        email.send()
        print('send email')
