from pymongo import MongoClient
import pandas as pd
import json
import os

DB = os.getenv('DB_OSM', 'localhost:27017')

BasePath = '/data'
Data_base_name = 'PostCode_database'


def mk_connection(collection_name):
    client = MongoClient(DB)
    db = client[Data_base_name]
    return db[collection_name]


def upload_postcode_data(reupload=0):
    collection = mk_connection("Postcodes")
    if (reupload == 1) or (reupload == 0 and collection.count() == 0):
        collection.remove({})
        data = pd.read_csv("/app/data/allCountries.tsv", sep='\t', error_bad_lines=False)
        data['Postal code'] = data['Postal code'].astype(str)
        data_json = json.loads(data.to_json(orient='records'))
        collection.insert_many(data_json)


def search_post_code(Postcode):
    collection = mk_connection("Postcodes")
    string = "^" + str(Postcode)
    result = list(collection.find({"Postal code": {"$regex": string}}))
    output = []
    for i in range(len(result)):
        if result[i]['Community']:
            community = result[i]['Community']
        else:
            community = ""
        output.append(
            [result[i]['Place'], community, result[i]['Postal code'], result[i]['Country code'], result[i]['Latitude'],
             result[i]['Longitude']])
    return output
