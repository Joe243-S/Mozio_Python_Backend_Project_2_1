import Data as d
from Geojson import getInformation

class update:

    def func_updateData(self):
        connection = d.getConnection()

        name = input('Enter Service Area\'s name: ')

        try:

            query = """SELECT * FROM ServiceArea WHERE CONVERT(VARCHAR, name) = %s"""
            cursor = connection.cursor()
            updateS = (name)
            cursor.execute(query, updateS)

            item = cursor.fetchone()
            print('Data fetched for Provider\'s Id', name)
            print(' name\t\t\t price\t\t geojson_information')
            print('--------------------------------------------------------')
            print(' {}\t\t {}\t\t {} '.format(item[0], item[1], item[2]))
            print('--------------------------------------------------------')
            print('Enter new details')

            newName = input('Enter new name: ')
            price = input('Enter new price: ')
            information = input('Enter new location: ')

            geojson_information = getInformation(information)

            query = """UPDATE ServiceArea SET name = %s, price = %s, geojson_information = %s WHERE CONVERT(VARCHAR, name) = %s"""

            recordUpdateS = (newName, price, geojson_information, updateS)
            cursor.execute(query, recordUpdateS)

            connection.commit()
            print('Updated')

        except:
            print('Somethng worng, please check.')

        finally:
            connection.close()
            print("MySQL connection is closed")