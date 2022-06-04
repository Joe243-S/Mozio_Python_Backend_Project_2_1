import Data


class Delete:

    def function_delete_data(self):
        connection = Data.get_connection()
        name = input('Enter the Provider\'s name: ')
        try:
            query = "SELECT * FROM Provider WHERE CONVERT(VARCHAR, name) = %s"
            cursor = connection.cursor()
            delete_provider = (name,)
            cursor.execute(query, delete_provider)
            item = cursor.fetchone()
            print('Data fetched for the Provider', name)
            print('name\t\t\t email\t\t\t\t\t\t phone_number\t\t language\t\t\t currency\n'
                  '----------------------------------------------------------------------------------------------\n'
                  ' {}\t\t\t {}\t\t {}\t\t {}\t\t\t {} '.format(item[0], item[1], item[2], item[3], item[4]))
            print('----------------------------------------------------------------------------------------------')
            confirm = input('Delete(Y/N)?')
            if confirm == 'Y':
                delete_query = "DELETE FROM Provider WHERE CONVERT(VARCHAR, name) = %s"
                cursor.execute(delete_query, delete_provider)
                connection.commit()
                print('Deleted')
            else:
                print('Cancelled')
        except:
            print('Ops! Error, try again.')
        finally:
            connection.close()
            print("Done")
