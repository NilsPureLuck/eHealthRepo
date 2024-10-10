from flask import Flask, jsonify, request

app = Flask(__name__)

liste_von_sensoren = [
    {"Id":1, "Name":"Testname", "Sensortyp":"TestSensortyp","Messwert": 42.69}
]

@app.route('/sensors', methods=['GET'])
def getSensoren():
    return jsonify(liste_von_sensoren)

@app.route('/newSensor', methods=['POST'])
def newSensor():
    neuer_eintrag = request.json

    liste_von_sensoren.append(neuer_eintrag)
    return jsonify(liste_von_sensoren)

@app.route('/sensors/<int:Id>', methods=["PUT"])
def updateSensor(Id):
    eintrag = next((s for s in liste_von_sensoren if s['Id'] == Id), None)
    daten = request.json;
    eintrag['Name'] = daten.get('Name', eintrag['Name'])
    eintrag['Sensortyp'] = daten.get('Sensortyp', eintrag['Sensortyp'])
    eintrag['Messwert'] = daten.get('Messwert', eintrag['Messwert'])
    return jsonify(liste_von_sensoren)

@app.route('/sensors/<int:Id>', methods=['DELETE'])
def deleteSensor(Id):
    eintrag = next((s for s in liste_von_sensoren if s['Id'] == Id), None)
    liste_von_sensoren.remove(eintrag)
    return jsonify(liste_von_sensoren)



if __name__ == '__main__':
    app.run()