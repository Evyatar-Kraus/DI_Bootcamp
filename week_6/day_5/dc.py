# Daily Challenge : Web API To DB
# Last updated : April 9th, 2021


# What You Will Learn :
# Web API and Database


# Instructions
# Using this API, create the functionality which will write 10 random countries to your database.

# These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.

import requests
from pprint import pprint
import psycopg2
import random
from psycopg2 import OperationalError
from psycopg2.errorcodes import UNIQUE_VIOLATION
from psycopg2 import errors
from dotenv import dotenv_values

countries_api_url = 'https://restcountries.com/v3.1'

def get_10_random_countries():
    response = requests.get(f"{countries_api_url}/all", timeout=10)
    response_json = response.json()
    random_countries = random.sample(response_json,10)
    # pprint(random_countries)
    random_countries = list(map(lambda country: {
        'subregion':country.get('subregion') ,
        'capital':country.get('capital'),
        'flag':country.get('flag'),
        'name':country.get('name'),
        'population':country.get('population')
    },random_countries))
    return random_countries




def get_env_db_info_dict():
    config = dotenv_values(".countries.env")
    return config

print(get_env_db_info_dict())

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

def add_countries_to_db():
        countries = get_10_random_countries()
        conn = get_new_connection()
        cur = conn.cursor()
        for country in countries:
            # pprint(country)
            try:
                cur.execute("INSERT INTO  countries (country_name,country_capital,country_population,country_flag ,country_subregion) VALUES (%s, %s, %s, %s, %s)",(
                    country.get('name').get('common'),\
                    country.get('capital')[0],\
                    country.get('population'),\
                    country.get('flag'),\
                    country.get('subregion')))
                conn.commit()
                print("Country saved")
            except errors.lookup(UNIQUE_VIOLATION):
                print("Error saving - Country already exits - same country name")
            except:
                print("Error saving")
        conn.close()
        cur.close()


add_countries_to_db()

#table create script
# CREATE TABLE countries
#  (
#      id serial primary key,
#      country_name varchar(100) NOT NULL UNIQUE,
#      country_capital varchar(100) NOT NULL,
#      country_population bigint NOT NULL,
#      country_flag varchar(2),
#      country_subregion varchar(100)
# );
