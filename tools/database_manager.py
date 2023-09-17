import mysql.connector


class DatabaseManager(object):
    def __init__(self):
        """
        A simple database manager for MySQL using the mysql-connector-python library.

        Attributes:
            __db_name (str): The database name.
            __db_user (str): The database user.
            __db_pass (str): The database password.
            __db_host (str): The database host.
            __db_port (int): The database port.
            conn: The database connection object.
            cur: The database cursor object.
        """
        """
        Initialize the DatabaseManager instance and establish a database connection.
        """
        self.__db_name = "cookbook"
        self.__db_user = "user"
        self.__db_pass = "password"
        self.__db_host = "127.0.0.1"
        self.__db_port = 3306
        self.conn = mysql.connector.connect(
            user=self.__db_user,
            password=self.__db_pass,
            host=self.__db_host,
            port=self.__db_port,
        )
        self.cur = self.conn.cursor()
        self.check_database()

    def check_database(self):
        """
        Check if the specified database exists and create it if it doesn't.

        Raises:
            mysql.connector.Error: If an error occurs during database creation.
        """
        try:
            self.cur.execute(f"CREATE DATABASE IF NOT EXISTS {self.__db_name}")

            self.conn.commit()
            self.conn.database = self.__db_name
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def query(self, arg, values=None):
        """
        Execute a SQL query.

        Args:
            arg (str): The SQL query to execute.
            values (tuple, optional): The values to bind to the query. Defaults to None.

        Raises:
            Exception: If an error occurs during query execution.
        """
        try:
            if values is None:
                self.cur.execute(arg)
            else:
                self.cur.execute(arg, values)
            self.conn.commit()
        except Exception as e:
            print(e)

    def fetchone(self, arg, values=None):
        """
        Execute a SQL query and fetch one result.

        Args:
            arg (str): The SQL query to execute.
            values (tuple, optional): The values to bind to the query. Defaults to None.

        Returns:
            tuple: The result of the query.

        Raises:
            Exception: If an error occurs during query execution.
        """
        try:
            if values is None:
                self.cur.execute(arg)
            else:
                self.cur.execute(arg, values)
            return self.cur.fetchone()
        except Exception as e:
            print(e)

    def fetchall(self, arg, values=None):
        """
        Execute a SQL query and fetch all results.

        Args:
            arg (str): The SQL query to execute.
            values (tuple, optional): The values to bind to the query. Defaults to None.

        Returns:
            list: A list of tuples containing the results of the query.

        Raises:
            Exception: If an error occurs during query execution.
        """
        try:
            if values is None:
                self.cur.execute(arg)
            else:
                self.cur.execute(arg, values)
            return self.cur.fetchall()
        except Exception as e:
            print(e)

    def __del__(self):
        """
        Close the database connection when the instance is deleted.
        """
        self.conn.close()
