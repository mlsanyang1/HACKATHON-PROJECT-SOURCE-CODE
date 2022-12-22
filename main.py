from flask import Flask, jsonify, request
import  random
best_friends = {'Monica':'Rachel','Joey':'Chandler','Ross':'Phoebe'}

app = Flask(__name__)

@app.route("/")
def hello_from_root():
    #Test through terminal by running: curl http://0.0.0.0:80
    return jsonify({'Energywithdietaryfibre(kJ)':random.randint(30,700),'Energywithoutdietaryfibre(kJ)':random.randint(400,1000),'Moisture (g)':random.randint(40,100),'Protein(g)':random.randint(1,50),'Totalfat(g)':random.randint(0,40),'Availablecarbohydrateswithsugaralcohols(g)':random.randint(0,100),'Availablecarbohydrateswithoutsugaralcohol(g)':random.randint(0,100),'Starch(g)':random.randint(0,50),'Totalsugars(g)':random.randint(0,100),'Addedsugars(g)':random.randint(0,100),'Freesugars(g)':random.randint(0,100),'Dietaryfibre(g)':random.randint(0,30),'Alcohol(g)':random.randint(0,20),'Ash (g)':random.randint(0,100),'Preformed vitamin A (retinol) (礸)':random.randint(0,700),})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)
