import Data


class Read:

    def function_read_data(self):
        connection = Data.get_connection()
        cursor = connection.cursor()
        read_query = "SELECT * FROM Provider"
        cursor.execute(read_query)
        for row in cursor:
            print('Provider = %r' % (row,))
        connection.close()
        print("Done")
