"""
Set local machine up for API development.
- Generates config file
- Creates tables
- Creates virtual environment.
"""

import configparser
from getpass import getpass
import peewee as pw
import subprocess
import sys
from time import sleep
from api.models import (
    Credentials, Posts
)

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'HOST': 'localhost',
    'DATABASE': 'blogstate',
    'PASSWORD': '',
    'USER': 'root'
}


def verify_credentials_and_setup_tables():
    """
    Attempts connecting to the database based on supplied credentials.
    Creates required tables if it can, else returns an error.
    """
    db = pw.MySQLDatabase(config['DEFAULT']['database'],
                          user=config['DEFAULT']['user'],
                          password=config['DEFAULT']['password'],
                          host=config['DEFAULT']['host'])
    try:
        db.connect()
        db.create_tables([
            Credentials,
            Posts,
        ])
    except pw.OperationalError:
        return True
    return None


def set_interactive_credentials():
    """
    Obtain database variables from user to connect to database, and store in
    configuration file.
    """

    config['DEFAULT']['HOST'] = input(
        'Server name/IP (leave blank if on local server): '
    ) or config['DEFAULT']['HOST']

    config['DEFAULT']['DATABASE'] = input(
        'The name of the database you created (leave blank if using the '
        'name "blogstate"): '
    ) or config['DEFAULT']['DATABASE']

    config['DEFAULT']['USER'] = input(
        'User name for the database (leave blank if `root`): '
    ) or config['DEFAULT']['USER']

    config['DEFAULT']['PASSWORD'] = getpass(
        'Password of development database (will be stored in the generated '
        '"config.ini"): '
    ) or config['DEFAULT']['PASSWORD']


def setup_virtual_environment():
    # NOT TESTED ON WINDOWS
    if sys.platform == 'linux':
        try:
            subprocess.call('python3 -m venv venv')
            subprocess.call('pip3 install -r requirements.txt')
        except:    # noqa
            return True
    return None
    


def generate_config_file():
    """
    Generates an ini file of the configuration which works so far.
    Running this function overwrites any previous setup values.
    """

    config['TOKENS'] = {}
    config['TOKENS']['API'] = 'secret'
    # This token is to be set in the `Authorization` header in all requests to
    # the API. For development purposes, it can be set to something easy to
    # remember.

    with open('config.ini', 'w') as cfg:
        config.write(cfg)


if __name__ == "__main__":
    print(
        '\n================================\n'
        '+++ DEVELOPMENT SERVER SETUP +++'
        '\n================================\n'
    )
    sleep(1)

    # A series of inputs to set database connection variables
    set_interactive_credentials()

    print('\nAttempt connection to database and create tables ...')
    sleep(0.5)

    err = verify_credentials_and_setup_tables()
    if err is not None:
        print(
            '[EXIT] An error occurred. This is an issue with either the '
            'values you entered, or with your MySQL server installation.'
        )
        exit(1)

    # Freeze the values to a "config.ini" file
    generate_config_file()

    # Attempt setting up the virtual environment in the same directory
    err = setup_virtual_environment()
    if err is not None:
        print(
            'It is best if you manually setup the virtual environment.'
            '\nSee https://github.com/roshnet/blogstate-api README.\n' 
        )

    # Finish setup, database looks good, all set!
    sleep(0.5)
    print(
        'The database has been set up. You can create users, add posts '
        'and play around with the API.\n'
        'Please run this setup again if you supplied incorrect values.'
    )
