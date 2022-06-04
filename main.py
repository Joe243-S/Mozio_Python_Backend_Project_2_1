from ProviderCRUD import ChoiceProvider
from ServiceAreaCRUD import ChoiceServiceArea


def main():
    done_main = True
    while done_main is True:
        print('Welcome to Mozio Group\n'
              'Enter option P for Provider\'s DataBase Management\n'
              'Enter option S for Service Area\'s DataBase Management\n'
              'Enter option C to close the DataBase connection')

        file = input('Enter your option: ')

        if file == 'P':
            provider_object = ChoiceProvider()
            provider_object.function_provider()

        elif file == 'S':
            service_object = ChoiceServiceArea()
            service_object.function_service_area()

        elif file == 'C':
            done_main = False
            print('The DataBase connection is closed\n'
                  'Thanks for trusting Mozio Group')

        else:
            print('Wrong option, try again!')


main()

