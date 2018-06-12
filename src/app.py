import uuid

from flask import Flask, session
from src.common.database import Database

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "Ab6C4D3Ef"


@app.before_first_request
def init():
    session['client_id'] = uuid.uuid4().hex
    Database.initialize()


from src.models.payments.views import payment_blueprint
app.register_blueprint(payment_blueprint, url_prefix="/payments")