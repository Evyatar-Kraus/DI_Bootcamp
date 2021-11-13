#Instructions below

import psycopg2
from psycopg2 import OperationalError
from psycopg2.errorcodes import UNIQUE_VIOLATION
from psycopg2 import errors
from dotenv import dotenv_values

#load env vars (like db name, user etc.. for program)

def get_env_db_info_dict():
    config = dotenv_values(".env")
    return config

def create_connection(db_name, db_user, db_pass, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_pass,
            host=db_host,
            port=db_port,
        )
        # print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred, connection unsuccessful")
    return connection


def get_new_connection():
    return create_connection(**(get_env_db_info_dict()))

TABLE_NAME = 'menu'


class MenuItem:
    def __init__(self,name,price):
        self.item_name = name
        self.item_price = price
        pass

    def save(self):
        conn = get_new_connection()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO  menu (item_name,item_price) VALUES (%s, %s)",
            ( self.item_name, self.item_price))
            conn.commit()
            print("Item saved")
        except errors.lookup(UNIQUE_VIOLATION):
            print("Error saving - item already exits - same name and price")
            raise Exception("Cant save")
        except:
            print("Error saving")
        finally:
            conn.close()
            cur.close()
            # print("connection closed")
        return

    def delete(self):
        conn = get_new_connection()
        cur = conn.cursor()
        try:
            cur.execute("DELETE FROM menu WHERE item_name=%s and item_price=%s",
            ( self.item_name,self.item_price))
            conn.commit()
            print("Item deleted")
        except:
            print("Error deleting")
        finally:
            conn.close()
            cur.close()
            # print("connection closed")
        return

    def update(self,new_name,new_price):
        conn = get_new_connection()
        cur = conn.cursor()
        try:
            cur.execute("UPDATE menu SET item_name = %s, item_price =%s WHERE item_name = %s and item_price=%s",
            ( new_name, new_price, self.item_name, self.item_price))
            conn.commit()
            print("item was updated")
            self.item_name = new_name
            self.item_price = new_price
        except errors.lookup(UNIQUE_VIOLATION):
            print("Error updating - item already exits - same name and price")
        except:
            print("Error updating item")
        finally:
            conn.close()
            cur.close()
            # print("connection closed")
        return


    @classmethod
    def all(self):
        conn = get_new_connection()
        cur = conn.cursor()
        cur.execute("SELECT item_name,item_price FROM menu ORDER BY item_name")
        results = cur.fetchall()
        results = list(map(lambda res: MenuItem(res[0],res[1]),results))
        conn.commit()
        conn.close()
        cur.close()
        # print("connection closed")
        return results

    @classmethod
    def get_by_name(self,item_name):
        conn = get_new_connection()
        cur = conn.cursor()
        print(f"Trying to retrieve item {item_name}")
        cur.execute("SELECT item_name,item_price FROM menu WHERE item_name=%s",
         (item_name,) )
        result = cur.fetchone()
        if result == None:
            print("Error - No such item found")
            return None
        conn.commit()
        conn.close()
        cur.close()
        # print("connection closed")
        return MenuItem(result[0],result[1])

    def __repr__(self) -> str:
        return f"""\"{self.item_name}\" -> \"price: {self.item_price}\""""




#table create script
# CREATE TABLE menu
# (
#     id serial primary key,
#     item_name varchar(50) NOT NULL,
#     item_price integer NOT NULL,
#     CONSTRAINT unique_item_price_name UNIQUE (item_name, item_price)
# )



# Code examples:
# chips = MenuItem.get_by_name('Chips')
# print(chips)
# item_burger =  MenuItem('Burger',35)
# print(item_burger)
# item_burger.save()

# print("get Burger with get_by_name")
# item_burger = MenuItem.get_by_name('Burger')
# print(item_burger)

# print("add veggie burger")
# item_veggie_burger = MenuItem('Veggie Burger',40)
# item_veggie_burger.save()
# print(item_veggie_burger)

# item_veggie_burger.update("Mushroom Burger",42)
# print(item_veggie_burger)

# item_veggie_burger.update("Burger",35)

# #adding fish burger and deleting it
# item_fish_burger = MenuItem("Fish Burger",45)
# item_fish_burger.save()
# item_fish_burger.delete()

# item_chicken_burger = MenuItem.get_by_name('Chicken Burger')

# print("get all menu items")
# all_items = MenuItem.all()
# print(all_items)




# instructions
# Description: Create a restaurant menu management system for a manager.
# The program should allow the manager to view the menu, add an item and delete an item.

# PART 1
# In this exercise we will use PostgreSQL and Python.
#  Create a new database and a new table in pgAdmin (or in psql)
#  Read the instructions below before creating the new table
# Create a new class called MenuItem, the attributes should be the name
#  and price of each item.
# Create several methods (save, delete, update) these methods will
# allow a user to save, delete and update
# items from the database.
# Within the MenuItem class create a method called all which will return
# a list of all our MenuItem objects.
# Create another method called get_by_name that will return a
# single MenuItem object depending on it’s name, if an object is
# not found (there is no item matching the name in the get_by_name method) return None.