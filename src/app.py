from flask import Flask, session
from common.database import Database

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "Ab6C4D3Ef"


@app.before_first_request
def init():
    Database.initialize()
    session['client_id'] = '0x4D3EfAb6C'


from api.api_payment import payment_blueprint
app.register_blueprint(payment_blueprint, url_prefix="/payments")