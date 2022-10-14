import json

from codecarbon import OfflineEmissionsTracker
from flask import jsonify, request

from app import app
from model import CalculFonction



@app.route("/")
def index():
    return "Hello world !"

@app.route("/home")
def home():
    return jsonify({'msg': 'Bienvenue'})

@app.route("/donnee", methods=["POST", "GET"])
def donnee():
    if request.method == "POST":
        param = request.get_json()
        I = param['I']
        WS = param['WS']
        Ta = param['Ta']
        T0 = param['T0']
        Minutes = param['Minutes']
        p = CalculFonction(I, WS, Ta, T0, Minutes)
        # p = CalculFonction(12, 15, 16, 15, 30)
        # valeur = p.Calcul()
        tracker = OfflineEmissionsTracker(country_iso_code="FRA")
        tracker.start()
        valeur2 = p.Calculboucle()
        tracker.stop()
        # for i in (p.Calculboucle):
        #     print(i)
        # return jsonify({"Temperature ":p.I, "Calcul":p.Calcul(), "Boucle":p.Calculboucle()})
        with open('data.json', 'w') as mon_fichier:
            json.dump(valeur2, mon_fichier)
        return jsonify(valeur2)
    if request.method == "GET":
        with open('data.json') as mon_fichier:
            data = json.load(mon_fichier)

        return jsonify(data)
@app.route("/carbone", methods=["POST", "GET"])
def carbone():
    if request.method == "POST":
        param = request.get_json()
        I = param['I']
        WS = param['WS']
        Ta = param['Ta']
        T0 = param['T0']
        Minutes = param['Minutes']
        p = CalculFonction(I, WS, Ta, T0, Minutes)
        tracker = OfflineEmissionsTracker(country_iso_code="FRA")
        tracker.start()
        valeur2 = p.Calculboucle()
        tracker.stop()
        # for i in (p.Calculboucle):
        #     print(i)
        # return jsonify({"Temperature ":p.I, "Calcul":p.Calcul(), "Boucle":p.Calculboucle()})
        return jsonify(tracker.final_emissions_data.emissions, tracker.final_emissions_data.cpu_energy,tracker.final_emissions_data.ram_energy)

if __name__ == "__main__":
    app.run()