import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Course

app = Flask(__name__)


# Database Configuration using Environment Variables
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_NAME = os.getenv('DATABASE_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:pass@localhost/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return "Welcome to the TA Management System!"

if __name__ == '__main__':
    app.run(debug=True)
