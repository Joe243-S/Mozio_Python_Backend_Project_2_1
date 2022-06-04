import Data


class Create:

    def function_create_data(self):
        connection = Data.get_connection()
        name = input('Enter the name: ')
        email = input('Enter the email: ')
        phone_number = input('Enter the phone number: ')
        language = input('Enter the language: ')
        currency = input('Enter the currency: ')
        try:
            cursor = connection.cursor()
            create_query = "INSERT INTO Provider (name, email, phone_number, language, currency) " \
                           "VALUES (%s, %s, %s, %s, %s)"
            record_create_provider = (name, email, phone_number, language, currency)
            cursor.execute(create_query, record_create_provider)
            connection.commit()
            print('Created')
        except:
            print('Ops! Error, try again.')
        finally:
            connection.close()
            print("Done")
