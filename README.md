
# 🌱 Crop Prediction Using Machine Learning and IoT

## Project Overview
This project combines **Machine Learning (ML)** and **Internet of Things (IoT)** to predict the most suitable crop for cultivation based on soil and environmental parameters.  

Users can input values such as:  
- **pH**  
- **Temperature**  
- **Humidity**  
- **Rainfall**  
- **NPK levels**  

The system predicts the optimal crop using a trained ML model.  

Additionally, it demonstrates an **IoT architecture** to collect real-time soil data using sensors, which is fed to the ML model for accurate crop recommendations.


## 🔹 Features
- Predicts crops based on soil and environmental parameters.
- Real-time data collection using IoT sensors.
- Integration of Arduino microcontroller to interface IoT sensors with the ML model.


## 🛠 IoT Architecture
The IoT setup includes:  
- **Sensors Used:**  
  - Temperature sensor  
  - Humidity sensor  
  - pH sensor  
  - Rainfall sensor  
  - NPK sensor  
- **Microcontroller:** Arduino board for data collection and transmission.  

- **Data Flow:**  
Sensors → Arduino → ML Model → Crop Prediction



**IoT Architecture Image:**  
![IoT Architecture](./https://github.com/snehal-145/Machine_Learning_project/blob/main/IOT.png)

**Microcontroller Setup:**  
![Arduino Setup](./path_to_microcontroller_image)

---

## 🧠 Machine Learning Model
- Trained on a **crop dataset** containing historical soil and crop data.
- **Input Features:** pH, Temperature, Humidity, Rainfall, N, P, K values.
- **Output:** Predicted crop.
- **ML Code File:** [ML Code File](./path_to_ml_code_file)



## ⚡ How to Use
1. Clone the repository:  

   git clone https://github.com/snehal-145/Machine_Learning_project.git


2. Install required Python libraries:

   pip install -r requirements.txt

3. Run the ML script:

   python crop_prediction.py

4. Input soil parameters manually or use IoT sensor data.

5. Get the predicted crop recommendation.


🛠 Tools & Technologies
Programming Language: Python

ML Libraries: scikit-learn, pandas, numpy

IoT Platform: Arduino IDE

Sensors: Temperature, Humidity, pH, Rainfall, NPK sensors

📊 Dataset
Contains historical soil parameters and crop data.

Columns: pH, Temperature, Humidity, Rainfall, Nitrogen (N), Phosphorous (P), Potassium (K), Crop.

📷 Project Images
IoT Connection Setup

Arduino Microcontroller

🚀 Future Enhancements
Integrate a web/mobile dashboard to visualize real-time soil data.

Deploy the ML model in cloud or edge devices for automated crop prediction.

Add more environmental parameters for improved accuracy.

👤 Author
Name: Snehal Wagavekar

GitHub: https://github.com/snehal-145




