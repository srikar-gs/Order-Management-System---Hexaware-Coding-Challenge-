import pyodbc

class DBConnUtil:
    @staticmethod
    def create_connection():
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

    @staticmethod
    def close_connection(conn):
        try:
            # Close the database connection
            conn.close()
        except Exception as e:
            # Handle closure errors
            print(f"Error closing the database connection: {str(e)}")
            raise e
