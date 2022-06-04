import Data
from Location import get_information


class Create:

    def function_create_data(self):
        connection = Data.get_connection()
        name = input('Enter the name: ')
        price = input('Enter the price: ')
        information = input('Enter the location: ')
        location = get_information(information)
        try:
            cursor = connection.cursor()
            create_query = "INSERT INTO ServiceArea(name, price, location) VALUES (%s, %s, %s)"
            record_create_service_area = (name, price, location)
            cursor.execute(create_query, record_create_service_area)
            connection.commit()
            print('Created')
        except:
            print('Ops! Error, try again.')
        finally:
            connection.close()
            print("Done")
