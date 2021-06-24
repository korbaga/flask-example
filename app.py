# import main Flask class and request object
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

# create the Flask app
app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
        'connect': False,
        'host': 'mongodb://127.0.0.1:27018/test_db?authSource=admin'
}

db = MongoEngine()
db.init_app(app)

class User(db.Document):
    _id = db.StringField()
    dis = db.StringField()
    siteRef = db.StringField()
    equipRef = db.StringField()
    equip = db.StringField()
    heatPump = db.StringField()
    fan = db.StringField()
    point = db.StringField()
    sensor = db.StringField()
    sensorFault = db.StringField()
    speedCmd = db.StringField()
    temp = db.StringField()
    
    def to_json(self):
        return {"_id": self._id,
                "dis": self.dis,
                "siteRef": self.siteRef,
                "equipRef": self.equipRef,
                "equip": self.equip,
                "heatPump": self.heatPump,
                "fan": self.fan,
                "point": self.point,
                "sensor": self.sensor,
                "sensorFault": self.sensorFault,
                "speedCmd": self.speedCmd,
                "temp": self.temp
                }

user = User(_id = "ee349ca0-f8aa-4b83-9fc6-86d727399914",
            dis = "Unitary HP",
            equip = "m",
            heatPump = "m",
            siteRef = "6b25c3c7-39e4-4be7-84a9-17e80feecaf5")
user.save()            
user1 = User(_id = "ce731aa1-fb9c-40b9-8f6b-ec6c42c9eadb",
            dis = "Fan",
            equip = "m",
            fan = "m",
            equipRef = "ee349ca0-f8aa-4b83-9fc6-86d727399914")
user1.save()    
user2 = User(_id = "bf34cfc8-cfe2-44d0-bf0a-ce462e2dc1c2",
             dis = "Return_Air_Temperature_Sensor",
             temp = "m",
             sensor = "m",
             sensorFault = "0",
             point = "m",
             equipRef = "ee349ca0-f8aa-4b83-9fc6-86d727399914")
user2.save()
user3 = User(_id = "af34cfc8-cfe2-44d0-bf0a-ce462e2dc1c1",
            dis = "FanSpeed",
            speedCmd = "m",
            point = "m",
            equipRef = "ce731aa1-fb9c-40b9-8f6b-ec6c42c9eadb")
user3.save()

#
#r = requests.get('http://localhost:5002/', params = {"_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914"})
#r.text
#
@app.route('/', methods=['GET'])
def query_records():
    _id = request.args.get('_id')
    user = User.objects(_id=_id).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())

#
#http://localhost:5002/objects/ee349ca0-f8aa-4b83-9fc6-86d727399914
#
@app.route('/objects/<id>')
def get_one_object(id: str):
    user = User.objects.get_or_404(_id=id)
    return user.to_json(), 200

#
#http://localhost:5002/all_objects
#
@app.route('/all_objects')
def get_all_objects():
    user = User.objects()
    return user.to_json(), 200
    
#
#r = requests.put('http://localhost:5002/update', json = {"_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914", "fan": "n"})
#THIS CHANGES 'fan' -> n'
#
@app.route('/update', methods=['PUT'])
def update_object():
    body = request.get_json()
    _id = body['_id']
    user = User.objects(_id=_id)
    if not user:
        return jsonify({'error': 'data were not found'})
    else:
        user.update(**body)
        return jsonify(user.to_json())
#
##HP_json = '{ "_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914", "dis": "Unitary HP", "fan": "m", "heatPump": "m", "siteRef": "6b25c3c7-39e4-4be7-84a9-17e80feecaf5"}'
#r = requests.put('http://localhost:5002/', data = HP_json)
# THIS ADDS 'fan: m' THRU UPDATE
#
@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    _id = record['_id']
    user = User.objects(_id=_id)
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.update(**record)
        return jsonify(user.to_json())
#
#HP_json = '{ "_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914", "dis": "Unitary HP", "equip": "m", "heatPump": "m", "siteRef": "6b25c3c7-39e4-4be7-84a9-17e80feecaf5"}'
#r = requests.post('http://localhost:5002/', data = HP_json)
#
@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    print(record)
    user = User(**record).save()
    return jsonify(user.to_json())
#
#r = requests.delete('http://localhost:5002/', params = {"_id": "ee349ca0-f8aa-4b83-9fc6-86d727399914"})
#
@app.route('/', methods=['DELETE'])
def delete_record():
    _id = request.args.get('_id')
    user = User.objects(_id=_id)
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
    return jsonify(user.to_json())

if __name__ == '__main__':
    # run app in debug mode on port 5001
    app.run(host='0.0.0.0', port=5002, debug=True)
