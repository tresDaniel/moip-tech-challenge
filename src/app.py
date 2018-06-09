from flask import Flask
from src.common.database import Database

app = Flask(__name__)
app.config.from_object('config')

@app.before_first_request
def init_db():
    Database.initialize()