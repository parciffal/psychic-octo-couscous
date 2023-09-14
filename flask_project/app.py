from flask import Flask
from flask_login import LoginManager
import mysql.connector

# import environ
import os


class DatabaseManager(object):
    def __init__(self):
        self.__db_name = "category"
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
        try:
            self.cur.execute(f"CREATE DATABASE IF NOT EXISTS {self.__db_name}")

            self.conn.commit()
            self.conn.database = self.__db_name
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def query(self, arg, values=None):
        try:
            if values is None:
                self.cur.execute(arg)
            else:
                self.cur.execute(arg, values)
            self.conn.commit()
        except Exception as e:
            print(e)

    def fetchone(self, arg, values=None):
        try:
            if values is None:
                self.cur.execute(arg)
            else:
                self.cur.execute(arg, values)
            return self.cur.fetchone()
        except Exception as e:
            print(e)

    def fetchall(self, arg, values=None):
        try:
            if values is None:
                self.cur.execute(arg)
            else:
                self.cur.execute(arg, values)
            return self.cur.fetchall()
        except Exception as e:
            print(e)

    def __del__(self):
        self.conn.close()


app = Flask(__name__)
app.config["SECRET_KEY"] = '$iZC7t*%3pzO/1k*j(m"6x(^7s\J/iu9)PD'
db_manager = DatabaseManager()

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    user = db_manager.fetchone(f"""SELECT * FROM users WHERE id={user_id}""")
    return user