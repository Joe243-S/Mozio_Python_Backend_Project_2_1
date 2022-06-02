import Data as d

class delete:

    def func_deleteData(self):
        connection = d.getConnection()

        name = input('Enter Provider\'s name: ')

        try:

            query = """SELECT * FROM Provider WHERE CONVERT(VARCHAR, name) = %s"""
            cursor = connection.cursor()
            deleteP = (name)
            cursor.execute(query, deleteP)

            item = cursor.fetchone()
            print('Data fetched for Provider\'s Id', name)
            print('name\t\t email\t\t\t\t\t phone_number\t\t language\t\t currency')
            print('----------------------------------------------------------------------------------')
            print(' {}\t\t {}\t\t {}\t\t {}\t\t\t {} '.format(item[0], item[1], item[2], item[3], item[4]))
            print('----------------------------------------------------------------------------------')
            confirm = input('Delete (Y/N)?')

            if confirm == 'Y':
                deleteQuery = """DELETE FROM Provider WHERE CONVERT(VARCHAR, name) = %s"""

                cursor.execute(deleteQuery, deleteP)
                connection.commit()
                print('Deleted')

            else:
                print('Cancelled')


        except:
            print('Somethng worng, please check.')

        finally:
            connection.close()
            print("MySQL connection is closed")