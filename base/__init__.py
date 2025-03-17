from flask import Flask
import warnings
from datetime import timedelta

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app=Flask(__name__)
app.secret_key='mc_net_test'

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.config['TESTING']=True
app.app_context().push()


import base.com.controller