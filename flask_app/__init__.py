import json
import os
from pathlib import Path

from flask import Flask


os.chdir(Path(os.path.abspath(__file__)).parent)

app = Flask(__name__)

with open('../config.json', 'r') as f:
    conf = json.load(f)
app.config['SECRET_KEY'] = conf['SECRET_KEY']
app.config['RECAPTCHA_PUBLIC_KEY'] = conf['RECAPTCHA_PUBLIC_KEY']
app.config['RECAPTCHA_PRIVATE_KEY'] = conf['RECAPTCHA_PRIVATE_KEY']

SEND = True
if not (
    conf.get('EMAIL_SEND') and conf.get('EMAIL_SEND_PASS') and conf.get('EMAILS_RECEIVE')
):
    SEND = False


from flask_app import routes
