<h1><b>Diabetes Risk Prediction</h1></b>

<h2><b>Overview</h2></b>

This project is a web-based application for predicting diabetes risk based on multiple health-related parameters such as weight, height, blood glucose level, physical activity, diet, and other lifestyle factors. The project consists of a frontend built with React and a backend powered by Flask, using a machine learning model to make predictions.
You can Check out the Project <a href = "https://diabetes-risk-prediction-seven.vercel.app/">here</a>

<h2><b>Tech Stack</h2></b>

<h3><b>Frontend:</h3></b>

>**React:** For building the user interface.

>**CSS:** For styling the application.

<h3><b>Backend:</h3></b>

>**Flask:** A lightweight web framework in Python.

>**Python:** Core Programming Language for Model Development

<h3><b>Machine Learning:</h3></b>

>**Scikit-learn:** Used for Building the Model. This model is based on Random Forest Classifier for classification task

>**Numpy&Pandas:** Data preprocessing and manipulation

<h3><b>Deployment:</h3></b>

>**Frontend:** Deployed React frontend on Vercel.

>**Backend:** Deployed backend API on Render.

<h2><b>Model Pipeline</h2></b>

<h4>1.Data Preprocessing:</h4>
<p> &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;
1.Missing values handled and cleaned.
	
&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;
2.Categorical features encoded if present.
                   
&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;
3.Features standardized for consistent model performance.
</p>

<h4><b>2.Model Training:</h4></b>
<p> &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;
1.Algorithm: Random Forest Classifier.
	
<p> &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;
2.Evaluation Metrices: Accuracy, Confusion Matrix and Classification Report
	
<p> &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;
3.Training Data: Dataset containing health metrics and corresponding diabetes risks.

<h4><b>3.Model Serialization:</h4></b>

 &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;
 Trained model saved using Pickle for deployment.




