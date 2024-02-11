from lib.solo_project import *
from unittest.mock import patch, MagicMock
import unittest

def test_add_to_menu():
    subject = Menu()
    subject.add_to_menu('Pizza', "13.50")
    assert subject.menu == [{"Pizza": "13.50"}]

def test_show_menu():
    subject = Menu()
    subject.add_to_menu('Pizza', "13.50")
    subject.add_to_menu('Cheeseburger', "10.00")
    subject.add_to_menu('Steak', "17.99")
    assert subject.show_menu() == [{"Pizza": "13.50"}, {"Cheeseburger": "10.00"}, {"Steak": "17.99"}]

def test_add_to_order():
    subject = Menu()
    subject.add_to_menu('Pizza', "13.50")
    subject.add_to_menu('Cheeseburger', "10.00")
    subject.add_to_menu('Steak', "17.99")
    subject.add_to_order(["Pizza", "Cheeseburger", "Steak"])
    assert subject.order_list == [{"Pizza": "13.50"}, {"Cheeseburger": "10.00"}, {"Steak": "17.99"}]

def test_receipt():
    subject = Menu()
    subject.add_to_menu('Pizza', "13.50")
    subject.add_to_menu('Cheeseburger', "10.00")
    subject.add_to_menu('Steak', "17.99")
    subject.add_to_order(["Pizza", "Pizza", "Cheeseburger", "Steak", "Cheeseburger"])
    assert subject.receipt() == [{"Item 1":{"Pizza":"13.50"}},
                                {"Item 2":{"Pizza":"13.50"}},
                                {"Item 3":{"Cheeseburger":"10.00"}},
                                {"Item 4":{"Steak":"17.99"}},
                                {"Item 5":{"Cheeseburger":"10.00"}},
                                {"Final Price":64.99}]

def test_send_confirmation(self, mock_twilio_client):
        # Replace these values with your actual Twilio credentials and phone numbers
        twilio_account_sid = ""
        twilio_auth_token = ""
        twilio_phone_number = ""
        recipient_phone_number = ""

        # Create a mock Twilio client
        mock_client = MagicMock()
        mock_twilio_client.return_value = mock_client

        # Instantiate the Menu class with mock Twilio client
        subject = Menu(twilio_account_sid, twilio_auth_token, twilio_phone_number, recipient_phone_number)

        # Add some items to the order list (replace this with your actual order)
        subject.add_to_menu('Pizza', "13.50")
        subject.add_to_menu('Cheeseburger', "10.00")
        subject.add_to_menu('Steak', "17.99")
        subject.add_to_order(["Pizza", "Pizza", "Cheeseburger", "Steak", "Cheeseburger"])

        # Call the send_confirmation method
        subject.send_confirmation()

        # Assert that the Twilio client was created with the correct credentials
        mock_twilio_client.assert_called_once_with(twilio_account_sid, twilio_auth_token)

        # Assert that the Twilio message was sent with the correct parameters
        mock_client.messages.create.assert_called_once_with(
            to=recipient_phone_number,
            from_=twilio_phone_number,
            body=unittest.mock.ANY  # You can also assert the exact body if needed
        )
