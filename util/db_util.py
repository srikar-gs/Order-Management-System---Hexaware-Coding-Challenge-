import pyodbc
class DBUtil:
    @staticmethod
    def getDBConn():
        # Specify the server name and the database name
        server = 'SRIKAR'
        database = 'OrderManagementSystem'
        
        # Construct the connection string
        conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        
        try:
            # Establish the database connection
            conn = pyodbc.connect(conn_str)
            return conn
        except Exception as e:
            # Handle connection errors
            print(f"Error connecting to the database: {str(e)}")
            raise e
