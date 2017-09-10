'''
Helpers for standard I/O work.
'''
import sys
import getpass

from lib.utils.validators import is_valid_email

def get_login_credentials():
    ''' Get login creds from user. Also includes some validation. '''
    while True:
        email = input('Enter your email address: ')
        if is_valid_email(email):
            break
        print('You entered an invalid email address.')

    password = getpass.getpass()

    return (email, password)


def login_with_email(login_service_instance):
    ''' Login a user with email via auth service. '''
    email, password = get_login_credentials()
    try:
        login_service_instance.login_with_email(email, password)
        print('\nLogged in successfully.\n')
    except Exception:
        print('\nAn error occurred. Please check your connection, credentials and try again.\n')
        sys.exit(1)
