import config
from flask import Flask, request, render_template, jsonify
import traceback
from testing import MedicalInsurance

app = Flask(__name__)

@app.route('/')    # home api
def home():
    return render_template('index.html')
    # return "Medical Insurance"

@app.route('/predict_charges', methods = ['GET','POST'])
def predict_charges():
    try:
        if request.method == "GET":
            data = request.args.get

            print("User Data is :",data)
            age    = eval(data("age"))
            gender = data("gender")
            bmi    = eval(data('bmi'))
            children = eval(data('children'))
            smoker  = data('smoker')
            region  = data('region')

            medical_ins = MedicalInsurance(age, gender, bmi, children, smoker, region)
            charges = medical_ins.get_predicted_price()[0]

            # return jsonify({"Result" : f"Medical Insurance Charges will be {charges}"})
            return render_template('index.html', prediction = charges)

        else:
            data = request.form.get
            print("User Data is ::::",data)

            age      = eval(data('age'))
            gender   = data('gender')
            bmi      = eval(data('bmi'))
            children = eval(data('children'))
            smoker   = data('smoker')
            region   = data('region')

            medical_ins = MedicalInsurance(age, gender, bmi, children, smoker, region)
            charges = medical_ins.get_predicted_price()[0]

            # return  jsonify({"Result" : f"Medical Insurence Charges will be : {charges}"})
            return  render_template('index.html',prediction = charges)
            
    except:
        print(traceback.print_exc())
        return  jsonify({"Message" : "Unsuccessful"})

        
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug = False)