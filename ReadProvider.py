import Data as d

class read:

    def func_readData(self):
        connection = d.getConnection()

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Provider")

        for row in cursor:
            print('row = %r' % (row,))

        connection.close()
        print("MySQL connection is closed")