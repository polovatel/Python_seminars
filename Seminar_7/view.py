import phonebook_create as create
import contact_info_output as cont_info

print('Welcome to PhoneBook 3.0!')
def greetings_text():
    greetings_text = input('Type "add" to add new contact. '
                           'To show your saved numbers input "show": ')
    
    while (greetings_text != 'add' 
           and greetings_text != 'show'):
              greetings_text = input('Please, check the '
                               'entred information and try again. To '
                               'quit type "Q"')
    
    if greetings_text == 'add':
        return create.insert_new_phone()
    
    elif greetings_text == 'Q':
        return quit()

    elif greetings_text == 'show':
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
            return(f'Here is your PhoneBook {cont_info.show_my_contacts_horiz()}')
        elif check_input_info == 'column':
            return(f'Here is your PhoneBook {cont_info.show_my_contacts_vertic()}')