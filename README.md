# warehouse_management

This Python script helps manage stock inventory for an audio store. It supports adding, removing, displaying a report on stocks available in the store. The user has the possibility to request the state of the whole inventory or a stock in particular.  
  
## Description
The programme is means to perform all the warehouse operations that are necessary for the inventory control of items related to hi-fi sound.  
  
## Technical specifications
The code has one base class, one subclass and three sub-subclasses.  
  
**Warehouse**: this is the super class which provides the necessary functionality for incrementing a list of inventories with all the attributes in question: type, name, and quantity to be used to generate the report. The class also provides the main functionality to add, remove and get a particular stock, get the total number of items in the warehouse, and generate the inventory report. Variables and functions include:  
  

• Variables
    - _inventory_: list to increment each stock initialized to the warehouse
    - _n_speakers, n_headphones, n_stereos_: quantity counter of each stock type

• Functions
    -        _add_items_: to increase number of items for a particular stock
    -      _get_n_items_: to get the number of items present for a particular stock
    -     _remove_items_: to decrease the number of items for a particular stock
    - _inventory_report_: to generate an inventory report of all the stocks in the warehouse
    -      _total_items_: to get the total number of items across all stocks in the warehouse
    
_Stock_: this subclass inherits the functionalities of the Warehouse class and the values of the variables defined in the above class. On top of that, it allows you to initialize a stock, its name, type, and quantity to then be used for the sub-subclasses.

_Speakers, Headphones, Stereos_: these sub-subclasses inherit the functionality of stock, thereby allowing to input the items into the warehouse and concurrently adds the values added to both the inventory list and the n_speakers variable.

Same concept was used for Headphones and Stereos sub-subclasses.

## Architecture
In the main all the functions described above are used and the following execution model with 3 main functionalities is proposed:

    1. Add new stock name to the list
    2. Add or remove quantity from current stock in Warehouse
    3. Search for an item
    
All the above will perform the functionalities defined in the classes but will also let the user to generate an inventory report before performing one of the functions above.

For more user friendliness, an interactive interface was created that would allow the user to select one of the three above in a more collaborative way.

The interface will remain active until the user decides to quit.
