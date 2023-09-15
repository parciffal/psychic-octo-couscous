from flask import Flask
from flask_login import LoginManager
import mysql.connector
from tools.database_manager import DatabaseManager


app = Flask(__name__)
app.config["SECRET_KEY"] = '$iZC7t*%3pzO/1k*j(m"6x(^7s\J/iu9)PD'
db_manager = DatabaseManager()

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    user = db_manager.fetchone(f"""SELECT * FROM users WHERE id={user_id}""")
    return user
