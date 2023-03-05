# Flask

## init 

>*The provided code includes three functions that perform deployment tasks for a Flask application, initialize an admin user, and initialize a database with sample data. Here is a brief summary of what each function does:

>*deploy() - This function creates an instance of the Flask application, initializes its database schema, and performs any necessary database migrations to update the schema to the latest version.

>*init_admin() - This function prompts the user for an email address and password for the administrator account, creates a new User object with those credentials and the username "admin", and adds it to the database.

>*init_db() - This function creates a new database table using a custom DB_Manager class, then adds several sample data records to the table.
 
## Routes
>*This is a Flask web application that provides a simple e-commerce store. The application allows users to register, log in, view items, and add them to their cart. The admin panel enables an admin to view all the registered users and their details, and manage the items available for sale. The application uses SQLAlchemy ORM to communicate with the SQLite database, Flask-Login to manage user authentication, and Flask-Bcrypt to hash passwords.

### The application consists of several routes, including:

>*/ - the home page, which displays all items available for sale.

>*/register - allows a user to register a new account.

>*/login - allows a user to log in to an existing account.

>*/logout - logs out the user and redirects them to the login page.

>*/admin - the admin panel, which displays all registered users and their details, and allows the admin to manage the items available for sale.

>*/about - displays information about the application.

>*/contact - displays contact information for the store.

>*/cart - displays the items in the user's cart.

>*/checkout - allows the user to checkout their items and provides a form to enter shipping details.

### Note- The application also includes a DB_Manager class to manage database interactions, and ess module for custom decorators to restrict access to certain routes.

# SQL Overview
>* This code defines a class DB_Manager that can be used to manage a database for a restaurant order management system. The class is responsible for creating tables, inserting records, querying records, and deleting records. The database is implemented using SQLite3.

## Dependencies
>*The code requires the sqlite3 and os modules.

## Class Methods
>* __init__(self)-The constructor method of the DB_Manager class connects to the SQLite3 database and creates a conn instance variable.

## TableCreation(self)
>* This method creates the ITEM and ORDERS tables in the database if they don't already exist.

## QuarryAllItem(self)
>* This method queries all records in the ITEM table and returns a list of lists, where each list contains the values for a single record.

## QuarryItemPrice(self)
>* This method queries the Price column of all records in the ITEM table and returns a list of prices.

## QuarryItemDescriptiom(self)
>* This method queries the Description column of all records in the ITEM table and returns a list of descriptions.

## QuarryAllOrder(self)
>* This method queries all records in the ORDERS table and returns a list of lists, where each list contains the values for a single record.

## QuarryOrderByUser_ID(self, ID)
>* This method queries the ORDERS table for records that match the given User_ID and returns a list of lists, where each list contains the values for a single record.

## AddItem(self, Name, Price, Description)
>* This method inserts a new record into the ITEM table with the given Name, Price, and Description values.

## AddOrder(self, Item_ID, User_ID, Table_Number,Order_Status)
>* This method inserts a new record into the ORDERS table with the given Item_ID, User_ID, Table_Number, and Order_Status values.

## RemoveItembyItem_ID(self, Item_ID)
>* This method deletes a record from the ITEM table that matches the given Item_ID.

## RemoveOrderbyItem_ID(self, ID)
>* This method deletes a record from the ORDERS table that matches the given Order_ID.

## RemoveOrderbyUser_ID(self, ID)
>* This method deletes all records from the ORDERS table that match the given User_ID.

## SqlQuarryExec(self, quarry)
>* This method executes an SQL query on the database and returns the results as a list of tuples.

## Commit(self)
>* This method commits any changes made to the database.

# Main Block
>* The main block of the code creates an instance of the DB_Manager class and calls its TableCreation method to create the necessary tables in the database.