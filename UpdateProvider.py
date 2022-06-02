import Data as d

class update:

    def func_updateData(self):
        connection = d.getConnection()

        name = input('Enter Provider\'s name: ')

        try:

            query = """SELECT * FROM Provider WHERE CONVERT(VARCHAR, name) = %s"""
            cursor = connection.cursor()
            updateP = (name)
            cursor.execute(query, updateP)

            item = cursor.fetchone()
            print('Data fetched for Provider\'s Id', name)
            print('name\t\t email\t\t\t\t\t phone_number\t\t language\t\t currency')
            print('----------------------------------------------------------------------------------')
            print(' {}\t\t {}\t\t {}\t\t {}\t\t\t {} '.format(item[0], item[1], item[2], item[3], item[4]))
            print('----------------------------------------------------------------------------------')
            print('Enter new details')

            newName = input('Enter new name: ')
            email = input('Enter new email: ')
            phone_number = input('Enter new phone number: ')
            language = input('Enter new language: ')
            currency = input('Enter new currency: ')

            query = """UPDATE Provider SET name = %s, email = %s, phone_number = %s, language = %s, currency = %s WHERE CONVERT(VARCHAR, name) = %s"""

            recordUpdateP = (newName, email, phone_number, language, currency, updateP)
            cursor.execute(query, recordUpdateP)

            connection.commit()
            print('Updated')

        except:
            print('Somethng worng, please check.')

        finally:
            connection.close()
            print("MySQL connection is closed")