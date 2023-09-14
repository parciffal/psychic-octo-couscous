from app import app
from api.category import *
from api.product import *
import mysql.connector
from api.register import *
from api.login import *
from models.user import *
from api.index import *
from models.category import *
from models.product import *
from api.logout import *


if __name__ == "__main__":
    app.app_context().push()
    app.run(debug=True)
