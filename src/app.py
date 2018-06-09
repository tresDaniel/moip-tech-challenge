from flask import Flask
from src.common.database import Database

app = Flask(__name__)
app.config.from_object('config')

@app.before_first_request
def init_db():
    Database.initialize()

from src.models.payments.views import payment_blueprint
app.register_blueprint(payment_blueprint, url_prefix="/payments")