# flask-example

install mongodb
pip install Flask request jsonify json monogoengine
>python app.py

# CLI commands
import json, request

## get
r = requests.get('http://localhost:5002/', params = {"_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914"})
r.text

## put
r = requests.put('http://localhost:5002/update', json = {"_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914", "fan": "n"})
r.text

HP_json = '{ "_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914", "dis": "Unitary HP", "fan": "m", "heatPump": "m", "siteRef": "6b25c3c7-39e4-4be7-84a9-17e80feecaf5"}'
r = requests.put('http://localhost:5002/', data = HP_json)
r.text

## post
HP_json = '{ "_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914", "dis": "Unitary HP", "equip": "m", "heatPump": "m", "siteRef": "6b25c3c7-39e4-4be7-84a9-17e80feecaf5"}'
r = requests.post('http://localhost:5002/', data = HP_json)

##delete
r = requests.delete('http://localhost:5002/', params = {"_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914"})

# browser

http://localhost:5002/objects/ee349ca0-f8aa-4b83-9fc6-86d727399914

