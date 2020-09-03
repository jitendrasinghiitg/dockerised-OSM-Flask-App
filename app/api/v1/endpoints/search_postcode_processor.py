from flask import Blueprint, request
from flask_cors import CORS, cross_origin
from utils.IOUtils import json_response
from DB.common import search_post_code

search_data_apps = Blueprint('search_data_apps', __name__, url_prefix='/api/v1/search_data')
CORS(search_data_apps)


@search_data_apps.route('/search', methods=['POST'])
@cross_origin()
def search():
    usrInput = request.get_json()
    postcode = usrInput['textSearch']
    if len(postcode) > 3:
        result = search_post_code(postcode)
    else:
        result = []
    return json_response({"results": result})
