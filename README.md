# Map app 

A Flask, Leaflet, OpenStreetMap based map app ,where we can search cities using there postcodes.

Postcode data has been taken from:

* [GeoNames](http://download.geonames.org/export/zip/)

## Demo

<p align="center">
   <img src="https://github.com/jitendrasinghiitg/dockerised-OSM-Flask-App/raw/master/app/static/demo.gif" width="800">
</p>

## Run on local machine
Install docker and docker-compose
```
sudo snap install docker
```
###### Run entire app with one command 
```
sh local_env_up.sh
```
###### content of local_env_up.sh
```
sudo docker-compose -f docker-compose.yml up --build
```

It starts a webservice with rest api and listens for messages at localhost:5000


## Usage

After running local_env_up.sh repo will upload allCountries.tsv into mongodb ,this might take 2 min.

after that navigate to localhost:5000

