import Data


class Update:

    def function_update_data(self):
        connection = Data.get_connection()
        name = input('Enter the Provider\'s name: ')
        try:
            query = "SELECT * FROM Provider WHERE CONVERT(VARCHAR, name) = %s"
            cursor = connection.cursor()
            update_provider = (name,)
            cursor.execute(query, update_provider)
            item = cursor.fetchone()
            print('Data fetched for the Provider', name)
            print('name\t\t\t email\t\t\t\t\t\t phone_number\t\t language\t\t\t currency\n'
                  '----------------------------------------------------------------------------------------------\n'
                  ' {}\t\t\t {}\t\t {}\t\t {}\t\t\t {} '.format(item[0], item[1], item[2], item[3], item[4]))
            print('----------------------------------------------------------------------------------------------')
            print('Enter new details')
            new_name = input('Enter the new name: ')
            email = input('Enter the new email: ')
            phone_number = input('Enter the new phone number: ')
            language = input('Enter the new language: ')
            currency = input('Enter the new currency: ')
            update_query = "UPDATE Provider SET name = %s, email = %s, phone_number = %s, language = %s," \
                           " currency = %s WHERE CONVERT(VARCHAR, name) = %s"
            record_update_provider = (new_name, email, phone_number, language, currency, update_provider)
            cursor.execute(update_query, record_update_provider)
            connection.commit()
            print('Updated')
        except:
            print('Ops! Error, try again.')
        finally:
            connection.close()
            print("Done")
