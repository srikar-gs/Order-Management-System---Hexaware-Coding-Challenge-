class DBPropertyUtil:
    @staticmethod
    def get_table_names(conn):
        try:
            # Retrieve table names from the database
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sys.tables")
            tables = cursor.fetchall()
            table_names = [table[0] for table in tables]
            return table_names
        except Exception as e:
            # Handle error retrieving table names
            print(f"Error retrieving table names: {str(e)}")
            raise e

    # Other utility functions for retrieving database properties can be added similarly
