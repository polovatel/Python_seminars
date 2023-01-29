import sqlite3
import phonebook_create as create
import contact_info_output as cont_info
import program_checks as check

print('Welcome to PhoneBook 3.0!')
def greetings_text():
    '''Вывод стартового сообщения'''
    greetings_text: str = input('Type "add" to add new contact. '
                           'To show your saved numbers input "show": ')
    
    while (greetings_text != 'add' 
           and greetings_text != 'show'):
              greetings_text = input('Please, check the '
                               'entred information and try again. To '
                               'quit type "Q"')
    
    if greetings_text == 'add':
        try: 
            return create.insert_new_phone()       
        except sqlite3.OperationalError:
            return check.database_check()
              
    elif greetings_text == 'Q':
        return quit()

    elif greetings_text == 'show':
        try:
            check_input_info = input('To open Phonebook with '
                                    'line output method, type "line" '
                                    'if you would like to see your '
                                    'contacts with column output '
                                    'method, type "column": ')
            while (check_input_info != 'line'
                and check_input_info != 'column'):
                    check_input_info =  input('Please, check the '
                                'entred information and try again: ')
            if check_input_info == 'line':
                return(f'Here is your PhoneBook '
                       f'{cont_info.show_my_contacts_horiz()}')
            elif check_input_info == 'column':
                return(f'Here is your PhoneBook '
                       f'{cont_info.show_my_contacts_vertic()}')
        except sqlite3.OperationalError:
            return check.database_check()
