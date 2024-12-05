from flask import Flask
import datetime
from flask_jwt_extended import JWTManager
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'sua_chave_secreta'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=15)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(days=7)

jwt = JWTManager(app)

from view.jwt import *

if __name__ == '__main__':
    app.run()