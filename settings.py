#Store the setting of the applcation

from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/mayank.surana/Documents/Programming/FlaskAPP/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
