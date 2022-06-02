import Data as d
from Geojson import getInformation

class create:

    def func_createData(self):
        connection = d.getConnection()
        name = input('Name: ')
        price = input('Price: ')
        information = input('Enter location: ')

        geojson_information = getInformation(information)

        try:
            cursor = connection.cursor()
            query = """INSERT INTO ServiceArea(name, price, geojson_information) VALUES (%s, %s, %s)"""

            recordCreateS = (name, price, geojson_information)
            cursor.execute(query, recordCreateS)

            connection.commit()
            print('Created')

        except:
            print('Somethng worng, please check.')

        finally:
            connection.close()
            print("MySQL connection is closed")