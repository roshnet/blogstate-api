import configparser
from getpass import getpass
import peewee as pw
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


def generate_config_file():
    pass


def main():
    """
    Generates config file, creates tables.
    """

    print(
        '================================'
        '+++ DEVELOPMENT SERVER SETUP +++'
        '================================'
    )
    sleep(1)

    config['DEFAULT']['HOST'] = input(
        'Server name/IP (leave blank if on local server): '
    ) or config['DEFAULT']['HOST']
    config['DEFAULT']['DATABASE'] = input(
        'The name of the database you created '
        '(leave blank if using `blogstate`): '
    ) or config['DEFAULT']['DATABASE']
    config['DEFAULT']['USER'] = input(
        'User name for the database (leave blank if `root`): '
    ) or config['DEFAULT']['USER']
    config['DEFAULT']['PASSWORD'] = getpass(
        'Password of development database (will be stored in the generated '
        '"config.ini"): '
    ) or config['DEFAULT']['PASSWORD']

    print('\nAttempt connection to database and create tables ...')
    sleep(0.5)

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
        print(
            '\n[EXIT] An error occurred. This is an issue with either the '
            'values you entered, or with your MySQL server installation.'
        )
        exit(1)

    # Finish setup, database looks good, all set!
    sleep(0.5)
    print(
        'The database has been set up. You can create users, add posts '
        'and play around with the application.\n'
        'Please run this setup again if you supplied incorrect values.'
    )


if __name__ == "__main__":
    main()
