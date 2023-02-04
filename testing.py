import pickle
import json
import config
import numpy as np

class MedicalInsurance():
    
    def __init__(self, age, gender, bmi, children, smoker, region):
        self.age    = age
        self.gender = gender
        self.bmi    = bmi
        self.childer = children
        self.smoker  = smoker
        self.region  = region
        return

    def __load_model(self):

        #load model files
        with open(config.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)
            print("Model >> ", self.model[0])
            print("Model >> ", self.model[1])

        #load project data files
        with open(config.JSON_FILE_PATH, 'r') as f:
            self.project_data = json.load(f)
            print("Project Data : ", self.project_data)

        #load normalisation model files
        with open(config.SCALER_MODEL, 'rb') as f:
            self.scaler_model = pickle.load(f)
            print("Scaler model : ", self.scaler_model)

    def get_predicted_price(self):
        self.__load_model()
        test_array = np.zeros((1, self.model[1].n_features_in_))
        test_array[0][0] = self.age
        test_array[0][1] = self.project_data['Gender'][self.gender] 
        test_array[0][2] = self.bmi 
        test_array[0][3] = self.childer 
        test_array[0][4] = self.project_data['Smoker'][self.smoker] 
        region = 'region_' + self.region
        index = self.project_data['Column Names'].index(region)

        test_array[0][index] = 1

        print("Test Array : ", test_array)
        scaled_test_array = self.scaler_model.transform(test_array)

        predicted_charges = np.around(self.model[1].predict(scaled_test_array), 3)
        print("Predicted Charges : ", predicted_charges)

        return predicted_charges


