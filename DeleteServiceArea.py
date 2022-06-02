import Data as d

class delete:

    def func_deleteData(self):
        connection = d.getConnection()

        name = input('Enter Service Area\'s name: ')

        try:

            query = """SELECT * FROM ServiceArea WHERE CONVERT(VARCHAR, name) = %s"""
            cursor = connection.cursor()
            deleteS = (name)
            cursor.execute(query, deleteS)

            item = cursor.fetchone()
            print('Data fetched for Provider\'s Id', name)
            print(' name\t\t\t price\t\t geojson_information')
            print('--------------------------------------------------------')
            print(' {}\t\t {}\t\t {} '.format(item[0], item[1], item[2]))
            print('--------------------------------------------------------')
            confirm = input('Delete (Y/N)?')

            if confirm == 'Y':
                deleteQuery = """DELETE FROM ServiceArea WHERE CONVERT(VARCHAR, name) = %s"""

                cursor.execute(deleteQuery, deleteS)
                connection.commit()
                print('Deleted')

            else:
                print('Cancelled')


        except:
            print('Somethng worng, please check.')

        finally:
            connection.close()
            print("MySQL connection is closed")