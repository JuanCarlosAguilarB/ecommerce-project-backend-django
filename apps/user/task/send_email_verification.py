from celery import shared_task

from apps.commons import MailService

from django.template.loader import render_to_string


@shared_task
def send_verification_email(user_email, verification_code):
    """
    Simulated task to send a verification email.

    :param str user_email: Email address of the user.
    :param str verification_code: Verification code to be sent.
    :return: Simulated success message.
    """

    email_service = MailService(
        f'{verification_code} is your verification code',
        user_email,
    )
    html = render_to_string('send_verification_code_email.html', {
        'verification_code': verification_code,
    })

    email_service.send_mail_with_html(html)

    print(
        f"Sending verification email to {user_email} with code: {verification_code}")

    return "Verification email sent successfully"
