import pymssql


def get_connection():
    data = pymssql.connect(server='mysqlserve243.database.windows.net', port=1433, user='lutende',
                           password='Joem243@', database='myDataba')
    return data
