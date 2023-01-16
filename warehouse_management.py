# MIT License
# 
# Copyright (c) 2022 Christopher Cauchi
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Class - Create a base class for Warehouse to store inventory
class Warehouse:
    # Initiate the inventory list and the number of speakers, headphones and stereos
    inventory = []
    n_speakers = 0
    n_headphones = 0
    n_stereos = 0

    def add_items(self, n_items):
        """Function to add items to specific stock type"""
        # Initiation of the 'Stock' class and the number of items we will add to the initiated Stock name
        self.quantity = self.quantity + n_items 

    def get_n_items(self):
        """Function that returns number of items present for specific stock type"""
        # Quantity to be defined in the 'Stock' class which inherits from 'Warehouse' class
        return self.quantity 

    def remove_items(self, n_items):
        """Function that removes items from specific stock type"""
        # Initiation of the 'Stock' class and the number of items we will remove from the initiated Stock name
        self.quantity = self.quantity - n_items 

    def inventory_report(self):
        """Function that will generate the inventory report for all stock names"""
        print("____________________ \033[1mInventory Report\033[0m _______________________")
        print("\x1B[3mName                            Quantity   Type\x1B[0m")
        # Loop through all initiations of Stock class added in 'inventory' list defined above
        for items in self.inventory:
            # Print the necessary spacing to be aligned with the field names above
            space_1 = (' ' * (30 - len(items.name)))
            space_2 = (' ' * (9 - len(str(items.quantity))))
            print(f'{items.name} {space_1} {items.quantity} {space_2} {items.type}')
        print('___________________________ End _____________________________')

    def total_items(self):
        """Function that loops through 'inventory' list and increments the quantity of each Stock initiation and then returns the total items in the warehouse"""
        tot = 0
        for items in self.inventory:
            tot += items.quantity
        return tot

class Stock(Warehouse):
    def __init__(self, name: str, quantity: int, type: str) -> None: 
        """Initialization function for Stock Class. Does not return anything and if it does, returns None"""
        # Specify name of the Stock initiation
        self.name = name
        # Specify the number of items currently in the Warehouse
        self.quantity = quantity
        # Specify the type of the Stock chosen
        self.type = type

class Speakers(Stock):
    def __init__(self, name, quantity):
        """Initialization function for the Speakers class, inheriting amount from Stock class"""
        # Access the class we inherited from Stock and add a 'type' argument (either Speakers, Headphones or Stereos)
        Stock.__init__(self, name, quantity, type)
        # Add to 'inventory' list inherited from 'Warehouse' class the initiation of the Speakers class that we define (e.g. s1 = Speakers('In-Wall', 2, Speakers) )
        self.inventory.append(self)
        # Specify the type of the stock
        self.type = 'Speakers'
        # Increment number of speakers by the quantity added above
        warehouse.n_speakers += quantity

class Headphones(Stock):
    def __init__(self, name, quantity):
        """Initialization function for the Headphones class, inheriting amount from Stock class"""        
        Stock.__init__(self, name, quantity, type)
        self.inventory.append(self)
        self.type = 'Headphones'
        warehouse.n_headphones += quantity

class Stereos(Stock):
    def __init__(self, name, quantity):
        """Initialization function for the Stereos class, inheriting amount from Stock class"""
        Stock.__init__(self, name, quantity, type)
        self.inventory.append(self)
        self.type = 'Stereos'
        warehouse.n_stereos += quantity

# Let's start initiating the classes

if __name__ == "__main__":
    warehouse = Warehouse()

    # Defining the three types of stock
    headphones1 = Headphones('In-Ear Headphones', 200)
    headphones2 = Headphones('Noise-Cancelling Headphones', 220)
    speakers1 = Speakers('Portable Speaker', 200)
    speakers2 = Speakers('In-Wall Speaker', 180)
    speakers3 = Speakers('Soundbar', 50)
    stereos1 = Stereos('Car Stereo', 80)
    print()
    print(f'Warehouse has {warehouse.total_items()} total items')
    print()
    print('__________________________MENU__________________________')
    print()

    # Set switch to 1 to run while loop
    main_menu = 1

    while main_menu == 1:
        # Ask user what functionality he wants to perform
        menu = int(input('1-Add new stock name to the list \n2-Add or remove quantity from current stock in Warehouse \n3-Search for an item\n\n'))

        if menu == 1:
            # If the user wants to generate Inventory and add a new item name in the Warehouse
            print()
            inventory_yes_no = int(input('Generate inventory? 1-Yes 2-No '))
            print()

            # If the user decides to generate the inventory report           
            if inventory_yes_no == 1:
                warehouse.inventory_report()
            print()

            # Ask user if he wants to add another stock to the list
            add_item_yes_no = int(input('Want to add another item? 1-Yes 2-No '))
            if add_item_yes_no == 1:
                print()
                choose_type = int(input('1-Speakers / 2-Headphones / 3-Stereos '))
                print()
                stock_name = input('Name of item: ')
                print()
                stock_quantity = int(input('Quantity of item: '))
                if choose_type == 1:
                    item_to_add = Speakers(stock_name, stock_quantity)
                elif choose_type == 2:
                    item_to_add = Headphones(stock_name, stock_quantity)
                else:
                    item_to_add = Stereos(stock_name, stock_quantity)
            print()
            
            # Ask user if he wants to return to menu to execute other functionality or quit
            main_menu = int(input('1-Return to Menu \n2-Quit '))

        elif menu == 2:
            # If the user wants to generate Inventory and add or remove quantity of current stock names in the Warehouse
            print()
            inventory_yes_no = int(input('Generate inventory report? 1-Yes 2-No '))
            print()

            # If the user decides to generate the inventory report            
            if inventory_yes_no == 1:
                warehouse.inventory_report()
            print()
            add_remove_pass = int(input('Want to add/remove item? 1-Add 2-Remove 0-Pass '))

            # If user chooses to add # of items to current stock
            if add_remove_pass == 1:
                list_items = [x.name for x in warehouse.inventory]
                name = input('Name of item: ')
                stock_quantity = int(input('Quantity of item: '))
                item = warehouse.inventory[list_items.index(name)]
                item.add_items(stock_quantity)

            # If user chooses to remove # of items from current stock
            elif add_remove_pass == 2:
                list_items = [x.name for x in warehouse.inventory]
                name = input('Name of item: ')
                stock_quantity = int(input('Quantity of item: '))
                item = warehouse.inventory[list_items.index(name)]
                item.remove_items(stock_quantity)
            else:
                pass
            print()

            # Ask user if he wants to return to menu to execute other functionality or quit
            main_menu = int(input('1-Return to Menu \n2-Quit '))

        elif menu == 3:
            print()
            # If the user wants to generate inventory report and search for a particular stock type and stock name in the Warehouse
            inventory_yes_no = int(input('Generate inventory report? 1-Yes 2-No '))
            print()

            # If the user decides to generate the inventory report
            if inventory_yes_no == 1:
                warehouse.inventory_report()
            print()
            print(f'Warehouse has {warehouse.total_items()} total items')
            print()

            # Ask user to input the stock type
            choose_type = int(input('Number of items for certain Stock: 1-Speakers 2-Headphones 3-Stereos 0-Pass '))
            if choose_type == 1:
                print(f'There are {warehouse.n_speakers} Speakers items')
            elif choose_type == 2:
                print(f'There are {warehouse.n_headphones} Headphones items')
            elif choose_type == 3:
                print(f'There are {warehouse.n_stereos} Stereo items')
            print()

            # Ask user to input if he/she wants to check if an item is available
            available_yes_no = int(input('Want to search if item is available? 1-Yes 2-No '))
            if available_yes_no == 1:
                name = input('Name of item: ')
                list_items = [x.name for x in warehouse.inventory]
                if name in list_items:
                    item = warehouse.inventory[list_items.index(name)]
                    print(f'{name} is available and current stock is: {item.get_n_items()}')
                else:
                    print(f'{name} is not available')

            # Ask user if he wants to return to menu to execute other functionality or quit
            main_menu = int(input('1-Return to Menu \n2-Quit '))
            print()