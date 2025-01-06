import React, { useState } from "react";
import "./App.css"; // Import the CSS file

function App() {
  const [formData, setFormData] =  useState({
    weight:0,
    height:0,
    blood_glucose:0,
    physical_activity:0,
    diet:0,
    medication_adherence:0,
    stress_level:0,
    sleep_hours: 0,
    hydration_level:0,
    bmi:0,
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch("http://localhost:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    });

    const result = await response.json();
    console.log("Response:", result);

    alert(`Predicted Risk: ${result.diabetes_risk}`);
  };

  return (
    <div className="app-container">
      <h1 className="title">
        <span>Diabetes Risk Prediction</span>
      </h1>

      <span className="run run-left" style={{ animationDelay: "0s" }}></span>
      <span className="run run-right" style={{ animationDelay: "0.2s" }}></span>
      <span className="run run-left" style={{ animationDelay: "0.4s" }}></span>
      <span className="run run-right" style={{ animationDelay: "0.6s" }}></span>
      <span className="run run-left" style={{ animationDelay: "0.8s" }}></span>
      <span className="run run-right" style={{ animationDelay: "1s" }}></span>
      <span className="run run-left" style={{ animationDelay: "1.2s" }}></span>
      <span className="run run-right" style={{ animationDelay: "1.4s" }}></span>
      <span className="run run-left" style={{ animationDelay: "1.6s" }}></span>
      <span className="run run-right" style={{ animationDelay: "1.8s" }}></span>
      <span className="run run-left" style={{ animationDelay: "2s" }}></span>
      <span className="run run-right" style={{ animationDelay: "2.2s" }}></span>
      <span className="run run-left" style={{ animationDelay: "2.4s" }}></span>
      <span className="run run-right" style={{ animationDelay: "2.6s" }}></span>
      <span className="run run-left" style={{ animationDelay: "2.8s" }}></span>
      <span className="run run-right" style={{ animationDelay: "3s" }}></span>
      <span className="run run-left" style={{ animationDelay: "3.2s" }}></span>
      <span className="run run-right" style={{ animationDelay: "3.4s" }}></span>
      <span className="run run-left" style={{ animationDelay: "3.6s" }}></span>
      <span className="run run-right" style={{ animationDelay: "3.8s" }}></span>
      <span className="run run-left" style={{ animationDelay: "4s" }}></span>
      <span className="run run-right" style={{ animationDelay: "4.2s" }}></span>

      <div className="form-container">
      <form onSubmit={handleSubmit}>
        {/* weight */}
        <div className="form-group">
          <label>
            Weight:
            <input
              type="number"
              name="Weight"
              onChange={handleChange}
              
              required
            />
          </label>
        </div>

        {/* Height */}
        <div className="form-group">
          <label>
            Height :
            <input
              type="number"
              name="Height"
              onChange={handleChange}
              
              required
            />
          </label>
        </div>

        {/* Blood Glucose */}
        <div className="form-group">
          <label>
            Blood Glucose: 
            <input
              type="number"
              name="blood_glucose"
              onChange={handleChange}
              
              required
            />
          </label>
        </div>

        {/* Physical Activity */}
        <div className="form-group">
          <label>
            Physical Activity (Mins Per Day):
            <input
              type="number"
              name="physical_activity"
              onChange={handleChange}
              required
            />
            
          </label>
        </div>

        {/* Diet */}
        <div className="form-group">
          <label>
            Diet:
            <select id="diet" name="diet" required>
              <option value=""></option>
              <option value="1">Yes</option>
              <option value="0">No</option>
            </select>
          </label>
        </div>

        {/* Medication Adherence */}
        <div className="form-group">
          <label>
            Medication Adherence:
            <select id="medication_adherence" name="medication_adherence" required>
              <option value= ""></option>
              <option value="1">Yes</option>
              <option value="0">No</option>
            </select>
          </label>
        </div>

        {/* Stress level */}
        <div className="form-group">
          <label>
            Stress level:
            <select id="stress_level" name="stress_level" required>
              <option value= ""></option>
              <option value="0">Low</option>
              <option value="1">Medium</option>
              <option value="2">High</option>
            </select>
            
          </label>
        </div>

        {/* Sleep hours */}
        <div className="form-group">
          <label>
            Sleep Hours:
            <input
              type="number"
              name="sleep_hours"
              onChange={handleChange}
              
              required
            />
          </label>
        </div>

        {/* Hydration level */}
        <div className="form-group">
          <label>
            Hydration Level:
            <select id="hydration_level" name="hydration_level" required>
               <option value= ""></option>
               <option value="1">Yes</option>
               <option value="0">No</option>
            </select>
          </label>
        </div>

        {/* BMI */}
        <div className="form-group">
          <label>
          BMI:
            <input
              type="number"
              name="bmi"
              onChange={handleChange}
              required
            />
          </label>
        </div>

        {/* Submit Button */}
        <button type="submit">Predict Risk</button>
      </form>
      </div>

    </div>
  );
}

export default App;