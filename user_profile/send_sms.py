from twilio.rest import Client
from autohub_backend.settings import twillio_sid, twillio_auth_token, sender_phone


def send_sms(contact_number, otp):
    """

    :param phone_number:
    :param otp:
    :return:
    """
    client = Client(twillio_sid, twillio_auth_token)
    client.messages.create(from_= sender_phone ,
                           to= contact_number,
                           body='Your otp code is {} '.format(otp))