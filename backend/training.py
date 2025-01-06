from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler 
import pandas as pd
import pickle

data = pd.read_csv("./diabetes_data.csv")
    
# Define a threshold to classify 'diabetes risk'
# Assume risk_score > 30 is high risk (1), else low risk (0)

data['diabetes_risk'] = (data['risk_score'] > 35).astype(int)

# Seperate Features and target 
X = data.drop(columns =['diabetes_risk','risk_score','user_id','date'])
Y = data['diabetes_risk']


#Scale the numerical features 
from sklearn.preprocessing import  StandardScaler

scaler = StandardScaler()
X = scaler.fit_transform(X)

#Split the train and test sets 
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#Build a Random Forest Model
rf_model = RandomForestClassifier(random_state=42, n_estimators=100)
rf_model.fit(X_train,Y_train)

#Evaluate the model 
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(Y_test, y_pred)
conf_matrix = confusion_matrix(Y_test, y_pred)
class_report = classification_report(Y_test, y_pred)

print(f"Accuracy:{accuracy}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)

# Save the model
model_path = 'random_forest_model.pkl'
with open(model_path, 'wb') as file:
    pickle.dump(rf_model, file)
print(f"Model saved to {model_path}")
    
    
#     #numerical columns for transformations
#     numerical = ['blood_glucose','physical_activity','sleep_hours']
#     return X,y,numerical

# #Load the Data 
# X,y,numerial = load_data()

# #Apply the SMOTE to address class imbalance 
# smote = SMOTE(random_state=42)
# X_resampled , y_resampled = smote.fit_resample(X,y)


# numerical = ['blood_glucose','physical_activity','sleep_hours']
# transformer = ColumnTransformer(transformers = [
#     ('num',StandardScaler(),numerical)])
     
# # def smote_transform(X,y):
# #     smote = SMOTE()
# #     return smote.fit_resample(X,y)

# pipeline = Pipeline(steps=[
#     ('scaler', transformer),
#     ('power', PowerTransformer(method='yeo-johnson', standardize=True)),
#     ('model', RandomForestClassifier())
# ])

# def evaluate_model(X,y,model):
#     cv = RepeatedStratifiedKFold(n_splits =10 , n_repeats=3,random_state = 1)
#     scores = cross_val_score(model , X,y,scoring="roc_auc",cv=cv,n_jobs = -1,error_score= 'raise')
#     return scores 

# #Evaluate the model 
# scores = evaluate_model(X_resampled,y_resampled,pipeline)
# print('Random Forest Classifier ROC-AUC: %.3f (%.3f)' % (np.mean(scores),np.std(scores)))

# pipeline.fit(X_resampled,y_resampled)

# dump(pipeline,'diabetes_prediction_model.joblib')



# Preprocessing

# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# import pickle

# data = pd.read_csv("./diabetes_data.csv")

# diabetes_data_cleaned = data.drop(columns =['user_id','date'])

# #Apply MinMax Scaling to Continuous features 

# scaler = MinMaxScaler()
# continuous_features =['weight','height','blood_glucose','physical_activity','sleep_hours','bmi','risk_score']
# diabetes_data_cleaned[continuous_features]= scaler.fit_transform(diabetes_data_cleaned[continuous_features])


# processed_file_path = 'diabetes_preprocessed_model.pkl'
# with open(processed_file_path,'wb') as file:
#     pickle.dump(diabetes_data_cleaned,file)
# print(f"Model saved to {processed_file_path}")


