
from twilio.rest import Client

class Menu():
    def __init__(self):
        self.menu = []
        self.order_list = []
        self.final_price = 0
        self.twilio_account_sid = ""
        self.twilio_auth_token = ""
        self.twilio_phone_number = ""
        self.recipient_phone_number = ""
    
    def add_to_menu(self, name, price):
        menu_item = FoodItem(name,price)
        self.menu.append({menu_item.name:menu_item.price})

    def show_menu(self):
        return self.menu
    
    def add_to_order(self, order_taken):
        self.order_list = []
        for item_name in order_taken:
            menu_item = next((item for item in self.menu if item_name in item), None)
            if menu_item:
                self.order_list.append(menu_item)
        return self.order_list
    
    def receipt(self):
        receipt_list = []
        counter = 1
        for item in self.order_list:
            for name, price in item.items():
                key = f"Item {counter}"
                receipt_list.append({key:{name:price}})
                self.final_price += float(price)
                counter += 1
        
        receipt_list.append({"Final Price":self.final_price})
        return receipt_list
    
    def send_confirmation(self):
        # Initialize Twilio client
        client = Client(self.twilio_account_sid, self.twilio_auth_token)

        # Compose the message
        message_body = "Thank you for your order!\n"
        for item in self.order_list:
            for name, price in item.items():
                message_body += f"{name}: ${price}\n"

        message_body += f"Total: ${self.final_price}\n"

        # Send the message
        message = client.messages.create(
            to=self.recipient_phone_number,
            from_=self.twilio_phone_number,
            body=message_body
        )

class FoodItem():
    def __init__(self,name, price):
        self.name = name
        self.price = price

subject = Menu()
subject.add_to_menu('Pizza', "13.50")
subject.add_to_menu('Cheeseburger', "10.00")
subject.add_to_menu('Steak', "17.99")
subject.add_to_order(["Pizza", "Pizza", "Cheeseburger", "Steak", "Cheeseburger"])
subject.send_confirmation()