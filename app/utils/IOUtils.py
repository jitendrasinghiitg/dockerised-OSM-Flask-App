from flask import Response
from json import JSONEncoder, loads, dumps


def json_response(data={}, status_code=200):
    json_encoded = JSONEncoder().encode(data)
    json_dict = loads(json_encoded)
    return Response(status=status_code, response=dumps(json_dict), mimetype='application/json')
