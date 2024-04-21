from flask import Flask

app = Flask(__name__)

# You can optionally import routes and models here if you want to organize your code
from app import routes
