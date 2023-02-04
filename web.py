from flask import Flask, request, render_template, jsonify
from testing import MedicalInsurance
import config


app = Flask(__name__)

@app.route('/')    # home api
def home():
    return "Medical Insurance Prediction"


@app.route('/predict_charges', methods = ["GET", "POST"])
def predict_charges():
  
    data = request.form

    print("Data : ", data)
    age      = int(data['age'])
    gender   = data['gender']
    bmi      = eval(data['bmi'])
    children = int(data['children'])
    smoker   = data['smoker']
    region   = data['region']

    medical_ins = MedicalInsurance(age, gender, bmi, children, smoker, region)
    charges = medical_ins.get_predicted_price()[0]

    # return jsonify({"Result" : f"Medical Insurance Charges will be {charges}"})
    return render_template('med_text.html')
        


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug = False)