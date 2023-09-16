from flask import Flask
from tools.database_manager import DatabaseManager


app = Flask(__name__)
app.config["SECRET_KEY"] = '$iZC7t*%3pzO/1k*j(m"6x(^7s\J/iu9)PD'
db_manager = DatabaseManager()
