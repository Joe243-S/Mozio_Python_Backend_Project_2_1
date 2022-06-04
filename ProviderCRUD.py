from CreateProvider import Create
from ReadProvider import Read
from UpdateProvider import Update
from DeleteProvider import Delete


class ChoiceProvider:

    def function_provider(self):
        done_provider = True
        while done_provider is True:
            print('Provider\'s DataBase Management\n'
                  'Enter option C to create\n'
                  'Enter option R to read\n'
                  'Enter option U to update\n'
                  'Enter option D to delete\n'
                  'Enter option Q to close the Provider\'s DataBase Management')
            choice = input('Enter your option: ')
            if choice == 'C':
                create_object = Create()
                create_object.function_create_data()
            elif choice == 'R':
                read_object = Read()
                read_object.function_read_data()
            elif choice == 'U':
                update_object = Update()
                update_object.function_update_data()
            elif choice == 'D':
                delete_object = Delete()
                delete_object.function_delete_data()
            elif choice == 'Q':
                done_provider = False
                print('Provider\'s DataBase Management is closed.')
            else:
                print('Wrong option, try again!')


ChoiceProvider()
