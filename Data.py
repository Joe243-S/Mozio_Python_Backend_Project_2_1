import pymssql


def get_connection():
    data = pymssql.connect(server='mysqlserve243.database.windows.net', user='lutende',
                           password='Joem243@', database='myDataba')
    return data
