import Data


class Delete:

    def function_delete_data(self):
        connection = Data.get_connection()
        name = input('Enter the Service Area\'s name: ')
        try:
            query = "SELECT * FROM ServiceArea WHERE CONVERT(VARCHAR, name) = %s"
            cursor = connection.cursor()
            delete_service_area = (name,)
            cursor.execute(query, delete_service_area)
            item = cursor.fetchone()
            print('Data fetched for the Service Area', name)
            print('name\t\t\t\t price\t\t location\n'
                  '---------------------------------------------------------------------------------\n'
                  '{}\t\t\t\t {}\t\t {} '.format(item[0], item[1], item[2]))
            print('---------------------------------------------------------------------------------')
            confirm = input('Delete(Y/N)?')
            if confirm == 'Y':
                delete_query = "DELETE FROM ServiceArea WHERE CONVERT(VARCHAR, name) = %s"
                cursor.execute(delete_query, delete_service_area)
                connection.commit()
                print('Deleted')
            else:
                print('Cancelled')
        except:
            print('Ops! Error, try again.')
        finally:
            connection.close()
            print("Done")
