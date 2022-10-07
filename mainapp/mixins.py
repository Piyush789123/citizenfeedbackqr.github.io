from django.conf import settings
from twilio.rest import Client
import random


class MassaHandler:
    phone_number=None
    otp = None
    def __init__(self, phone_number, otp) -> None:
        self.phone_number=phone_number
        self.otp=otp

    def send_otp_on_phone(self):
        client = Client(settings.A,settings.AUTH)
        message = client.messages.create(
                            body=f'YOUR OTP {self.otp}',
                            from_='+12058839488',
                            to=self.phone_number
                        )

