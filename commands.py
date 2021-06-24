import requests

http://10.40.7.78:5002/objects/ee349ca0-f8aa-4b83-9fc6-86d727399914
     
r = requests.get('http://10.40.7.78:5002/', params = {"_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914"})
r.text

r = requests.put('http://10.40.7.78:5002/update', json = {"_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914", "fan": "n"})
r.text

HP_json = '{ "_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914", "dis": "Unitary HP", "fan": "m", "heatPump": "m", "siteRef": "6b25c3c7-39e4-4be7-84a9-17e80feecaf5"}'
r = requests.put('http://10.40.7.78:5002/', data = HP_json)
r.text
 
HP_json = '{ "_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914", "dis": "Unitary HP", "equip": "m", "heatPump": "m", "siteRef": "6b25c3c7-39e4-4be7-84a9-17e80feecaf5"}'
r = requests.post('http://10.40.7.78:5002/', data = HP_json)
r.text
 
r = requests.delete('http://10.40.7.78:5002/', params = {"_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914"})
r.text 

r = requests.put('http://10.40.7.78:5002/update', json = {"_id": "bf34cfc8-cfe2-44d0-bf0a-ce462e2dc1c2", "sensorFault": "1"})
r = requests.get('http://10.40.7.78:5002/', params = {"_id": "bf34cfc8-cfe2-44d0-bf0a-ce462e2dc1c2"})
print(r['value'])