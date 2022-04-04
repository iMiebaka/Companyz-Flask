import pymongo
from flask import Flask, jsonify, request, Blueprint
from config import config



dev_flag = 'production'
dev_flag = 'default' # Commnent this during deployment

app = Flask(__name__)

client = pymongo.MongoClient("localhost", 27017)
db = client.test_database

from core.api import api

# # Register bleprints
app.register_blueprint(api, url_prefix='/api/v1/')

# database = config[dev_flag].DATABASE_URI

