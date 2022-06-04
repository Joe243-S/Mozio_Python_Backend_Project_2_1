from CreateServiceArea import Create
from ReadServiceArea import Read
from UpdateServiceArea import Update
from DeleteServiceArea import Delete


class ChoiceServiceArea:

    def function_service_area(self):
        done_service_area = True
        while done_service_area is True:
            print('Service Area\'s DataBase Management\n'
                  'Enter option C to create\n'
                  'Enter option R to read\n'
                  'Enter option U to update\n'
                  'Enter option D to delete\n'
                  'Enter option Q to close the Service Area\'s DataBase Management')
            choice = input('Choose your option: ')
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
                done_service_area = False
                print('Service Area\'s DataBase Management is closed.')
            else:
                print('Wrong option, try again!')


ChoiceServiceArea()
