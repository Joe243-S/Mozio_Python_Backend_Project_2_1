import Data
from Location import get_information


class Update:

    def function_update_data(self):
        connection = Data.get_connection()
        name = input('Enter the Service Area\'s name: ')
        try:
            query = "SELECT * FROM ServiceArea WHERE CONVERT(VARCHAR, name) = %s"
            cursor = connection.cursor()
            update_service_area = (name,)
            cursor.execute(query, update_service_area)
            item = cursor.fetchone()
            print('Data fetched for the Service Area', name)
            print('name\t\t\t\t price\t\t location\n'
                  '---------------------------------------------------------------------------------\n'
                  '{}\t\t\t\t {}\t\t {} '.format(item[0], item[1], item[2]))
            print('---------------------------------------------------------------------------------')
            print('Enter new details')
            new_name = input('Enter the new name: ')
            price = input('Enter the new price: ')
            information = input('Enter the new location: ')
            location = get_information(information)
            update_query = "UPDATE ServiceArea SET name = %s, price = %s, location = %s " \
                           "WHERE CONVERT(VARCHAR, name) = %s"
            record_update_service_area = (new_name, price, location, update_service_area)
            cursor.execute(update_query, record_update_service_area)
            connection.commit()
            print('Updated')
        except:
            print('Ops! Error, try again.')
        finally:
            connection.close()
            print("Done")
