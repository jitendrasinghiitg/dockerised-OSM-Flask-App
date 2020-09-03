from flask import Blueprint
from flask_cors import CORS
from utils.IOUtils import json_response
from DB.common import upload_postcode_data

upload_data_apps = Blueprint('upload_data_apps', __name__, url_prefix='/api/v1/upload_data')
CORS(upload_data_apps)


@upload_data_apps.route('/upload_postcode_data', methods=['GET'])
def u_staion_data():
    upload_postcode_data(0)
    return json_response({"status": True})
