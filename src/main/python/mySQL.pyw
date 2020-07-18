import mysql.connector

class MySQLHandler():
    """Provides the interface for the mySQL database this application
    interacts with."""

    def __init__(self):
        """Constructor method."""

        self.create_mysql_connection()
        self.create_cursor()
        self.show_databases()
        self.create_database_connection("zonemod")
        self.create_table("zone_models")

    def create_mysql_connection(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "L!nuxgn0me_815"
        )
    
    def create_database_connection(self, database_name):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "L!nuxgn0me_815",
            database = database_name
        )

    def create_cursor(self):
        """Creates a cursor. Not to sure what this does other than
        let you type in mySQL commands."""

        connection = self.get_mysql_connection()
        self.cursor = connection.cursor()

    def create_database(self, database_name):
        """Creates a new database."""
        
        self.execute_sql_statement("CREATE DATABASE " + database_name)

    def create_table(self, table_name):
        """Creates a new table in a database."""

        self.execute_sql_statement("CREATE TABLE " + table_name + " (" 
            + "zone_model name VARCHAR(10), "
            + "area_code VARCHAR(255), "
            + "district_number VARCHAR(255), "
            + "zone VARCHAR(10)")

    def show_databases(self):
        """Displays all the databases in the system."""
        
        cursor = self.execute_sql_statement("SHOW DATABASES")

        for item_of_info in cursor:
            print(item_of_info[0])

    def get_mysql_connection(self):
        """Returns the connection for mySQL."""
        
        return self.connection

    def get_cursor(self):
        """Returns the cursor responsible for providing mySQL
        commands."""
        
        return self.cursor
    
    def execute_sql_statement(self, sql_statement):
        """Executes an SQL statement using the cursor object."""

        cursor = self.get_cursor()
        cursor.execute(sql_statement)

        return cursor
    
    def insert_database_record(self, table, record):
        
        print("Do stuff and thaaaaannggggssss.")