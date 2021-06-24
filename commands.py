import requests, warnings

URL = 'http://10.40.7.78:5002/'
#URL = 'http://localhost:5002/'

#web brower functions
#http://10.40.7.78:5002/objects/ee349ca0-f8aa-4b83-9fc6-86d727399914
#http://10.40.7.78:5002/all_objects
print("get request")     
r = requests.get(url=URL, params = {"_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914"})
print(r.json())

print("put request with single json field")
r = requests.put(url=URL+'update', json = {"_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914", "fan": "n"})
if r.status_code != 200:
    warnings.warn(f"Unexpected put error: {r.status_code}")
print("<Response [200]> means success")
print(r)
print(r.json())

print("put request with multiple json fields")
HP_json = '{ "_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914", "dis": "Unitary HP", "equip": "m", "heatPump": "m", "siteRef": "6b25c3c7-39e4-4be7-84a9-17e80feecaf5"}'
r = requests.post(url=URL, data = HP_json)
if r.status_code != 200:
    warnings.warn(f"Unexpected put error: {r.status_code}")
print(r)
print(r.json())

print("put request with different json fields.  update adds new 'fan' field") 
HP_json = '{ "_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914", "dis": "Unitary HP", "fan": "m", "heatPump": "m", "siteRef": "6b25c3c7-39e4-4be7-84a9-17e80feecaf5"}'
r = requests.put(url=URL, data = HP_json)
if r.status_code != 200:
    warnings.warn(f"Unexpected put error: {r.status_code}")
print(r)
print(r.json())
 
print("delete request")
r = requests.delete(url=URL, params = {"_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914"})
print(r)
print(r.json())

print("change sensorFault with bad value")
r = requests.put(url=URL+'update', json = {"_id": "bf34cfc8-cfe2-44d0-bf0a-ce462e2dc1c2", "sensorFault": "1"})
if r.status_code != 200:
    warnings.warn(f"Unexpected put error: {r.status_code}")
print(r.content)    

print("change sensorFault with good value")
r = requests.put(url=URL+'update', json = {"_id": "bf34cfc8-cfe2-44d0-bf0a-ce462e2dc1c2", "sensorFault": True})
if r.status_code != 200:
    warnings.warn(f"Unexpected put error: {r.status_code}")
print(r.content)
    
print("get value after change")
r = requests.get(url=URL, params = {"_id": "bf34cfc8-cfe2-44d0-bf0a-ce462e2dc1c2"})
print(r)
print(r.json()['value'])
print(r.json()['sensorFault'])