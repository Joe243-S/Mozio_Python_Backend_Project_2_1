import Data as d

class create:

    def func_createData(self):
        connection = d.getConnection()

        name = input('Name: ')
        email = input('Email: ')
        phone_number = input('Phone number: ')
        language = input('Language: ')
        currency = input('Currency: ')

        try:
            cursor = connection.cursor()
            query = """INSERT INTO Provider (name, email, phone_number, language, currency) VALUES (%s, %s, %s, %s, %s)"""

            recordCreateP = (name, email, phone_number, language, currency)
            cursor.execute(query, recordCreateP)

            connection.commit()
            print('Created')

        except:
            print('Somethng worng, please check.')

        finally:
            connection.close()
            print("MySQL connection is closed")