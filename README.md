![image](https://github.com/user-attachments/assets/75fd907f-52e1-4cf2-8161-e7c473b351ff)


🏡Real Estate Price Prediction Dashboard        
This project involves building a Real Estate Price Prediction system using machine learning and deploying it as a web application. It aims to help users estimate property prices based on key features like location, area, number of BHKs, and more. The entire pipeline includes data cleaning, feature engineering, model training, and deployment using Flask, with a clean and user-friendly interface.

🔧 Tools & Technologies Used
Python – Data preprocessing, model building

Pandas, NumPy, Matplotlib, Seaborn – Data analysis and visualization

Scikit-learn – Model training (Linear Regression)

Flask – Backend web framework for deployment

HTML/CSS/JavaScript – Frontend user interface

Jupyter Notebook – Model development and experimentation

📊 Project Features
Cleaned and prepared raw data from the Bengaluru_House_Data.csv dataset by removing outliers and handling missing values.

Engineered features such as location encoding, total square footage, and BHK count to improve model accuracy.

Trained and evaluated multiple models; selected Linear Regression as the best-performing one based on RMSE.

Developed a Flask-based web app to allow users to input property features and get real-time price predictions.

Designed a simple and intuitive frontend UI for better user experience.

Ensured modular code structure for easy maintenance and future scalability.

Deployed the project locally for demonstration and testing purposes.


🚀 How to Run the Project
Clone this repository

Install the required libraries using pip install -r requirements.txt

Run app.py to start the Flask server

Open the browser and go to http://127.0.0.1:5000/

Enter property details and get the predicted price!
