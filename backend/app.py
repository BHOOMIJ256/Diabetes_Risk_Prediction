from flask import Flask , request,jsonify
import pickle 
from joblib import load
from flask_cors import CORS
import numpy as np 


#initialize the flask app
app = Flask(__name__)
CORS(app)

model = pickle.load(open('random_forest_model.pkl','rb'))


@app.route('/')
def home():
     return "Diabetes Risk Prediction API is Running !"

@app.route('/predict', methods =['POST'])
def predict():
    try:
        data = request.json

        #features from input JSON
        features = [
            data.get('weight',0),
            data.get('height',0),
            data.get('blood_glucose',0),
            data.get('physical_activity',0),
            data.get('diet',0),
            data.get('medication_adherence',0),
            data.get('stress_level',0),
            data.get('sleep_hours',0),
            data.get('hydration_level',0),
            data.get('bmi',0)
        ]

        
        prediction = model.predict([features])[0]
        
        result = {"diabetes_risk": int(prediction)}

        return jsonify (result)
    
    except Exception as e:
        return jsonify({"error": str(e)})
    
if __name__ == '__main__':
     app.run(host='0.0.0.0',port=5000,debug=True) 








































#         if not data:
#              return jsonify({"error": "No Input Data Provided"}),400
        
#         try:
#             #Convert input data to a DataFrame 
#             input_features = pd.DataFrame([data])

            
#             #Map Categorical Fields
#             input_features['medication_adherence'] = input_features["medication_adherence"].map({0:"No" ,1:"Yes"})
#             input_features['stress_level'] = input_features['stress_level'].map({0:"Low", 1:"Medium",})
#             input_features["hydration_level"] = input_features['hydration_level'].map({"No":0,"Yes":1})
#             input_features["diet"] = input_features['diet'].map({"Yes":1,"No":0})
            
#             #Debugging : Print input features
#             print("Input Features After Mapping:",input_features)

#             #Apply preprocessing to the input features
#             preprocessed_features = preprocess.transfrom(input_features)

#             #Print the preprocessed features
#             print("Preprocessed Features:",preprocessed_features)

#            #Make the prediction 
#             prediction = model.predict(input_features)
#             risk = "High Risk" if prediction[0] == 1 else "Low Risk"

#             return jsonify({"diabetes_risk":risk})
        
#         except Exception as e:
#              return jsonify({"error": str(e)}),500

    
    
# @app.route('/')
# def home():
#     return "Welcome to the Diabetes Prediction API"

# if __name__== '__main__':
#     app.run(host='0.0.0.0',port=5000,debug=True) 

