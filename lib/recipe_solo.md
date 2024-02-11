## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

Use twilo-python to implement the next 

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

and order class containing a list of items called menu and an empty list of items called order.

a function to order several items off of the menu

a function to return a list of all items ordered, their prices and a total price

a function to confirm the order and send a text to their phone 

## 2. Design the Class Interface

Class Order():
    def init()
    generate various objects to enter into the menu
    menu_list = [full menu]
    order_list() = []

    def see menu
        returns a list of all items on the menu

    def add_to_order(list):
        adds all items listed to the order list if it is present in the menu

    def recipt():
        returns a list of all items, their prices and a final price.

    def confirm order():
        sends a text confirming the order,

Class Order_Mock()
    similar to above but for the purpose of mock testing.

Class Food_item()
    contains the name and price of a menu item

## 3. Create Examples as Tests

test menu
    prove the menu is generate on init

test add to order
    after adding several objects to the order, prove the objects are present in the list

test recipt
    after adding several objects, prove the recipt contains the item number, name and price of each item with a final total price at the end

Mock tests
    unit testing of the order class

## 4. Implement the Behaviour
