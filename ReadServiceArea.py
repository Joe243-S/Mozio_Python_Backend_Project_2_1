import Data


class Read:

    def function_read_data(self):
        connection = Data.get_connection()
        cursor = connection.cursor()
        delete_query = "SELECT * FROM ServiceArea"
        cursor.execute(delete_query)
        for row in cursor:
            print('Service Area = %r' % (row,))
        connection.close()
        print("Done")
