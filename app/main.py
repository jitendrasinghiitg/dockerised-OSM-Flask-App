from flask import Flask, render_template
from DB.common import upload_postcode_data
from api.v1.endpoints.search_postcode_processor import search_data_apps
from api.v1.endpoints.upload_data_processor import upload_data_apps

app = Flask(__name__)
app.register_blueprint(search_data_apps)
app.register_blueprint(upload_data_apps)


@app.route('/about')
def welcome():
    return 'Map Webapp using WebOSM'


@app.route('/')
def index():
    return render_template("test.html")


if __name__ == "__main__":
    upload_postcode_data(0)
    app.run()
