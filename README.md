# movie-genre-classification


🎬 Movie Genre Classification using Machine Learning

A machine learning-based web application that predicts movie genres from text descriptions using Natural Language Processing (TF-IDF) and a trained classification model. The project is deployed using Streamlit for real-time interaction.


---

📌 Project Overview

This project focuses on classifying movie descriptions into predefined genres using NLP and machine learning techniques. The model learns patterns from text data and predicts the most relevant genre for a given input.

Supported genres include:

Drama

Romance

Action

Horror

Comedy



---

🧠 Problem Statement

Manually categorizing movies into genres is time-consuming and subjective. This project automates the process using machine learning to improve efficiency and consistency.


---

⚙️ System Architecture

Text Input → Text Preprocessing → TF-IDF Vectorization → ML Model → Genre Prediction


---

🛠️ Tech Stack

Python

Pandas, NumPy

Scikit-learn

NLP (TF-IDF Vectorizer)

Streamlit



---

📂 Project Structure

movie-genre-classification/
│
├── app.py                  # Streamlit application
├── model.pkl               # Trained ML model
├── vectorizer.pkl          # TF-IDF vectorizer
├── requirements.txt        # Dependencies
└── README.md               # Project documentation


---

🚀 Installation & Setup

1. Clone the repository

git clone https://github.com/mohithbalakrishnan/movie-genre-classification.git
cd movie-genre-classification

2. Install dependencies

pip install -r requirements.txt

3. Run the application

streamlit run app.py


---

🎯 Usage

Enter a movie description in the input box, and the model will predict the most likely genre in real time.


---

📥 Example

Input: A young couple falls in love but faces emotional struggles and family pressure.

Output: Romance / Drama


---

📊 Model Details

Feature Extraction: TF-IDF Vectorizer

Model Type: Supervised Machine Learning Classifier

Training Data: Movie descriptions with labeled genres



---

📈 Results

The model performs well on text classification tasks. However, similar genres such as Romance and Drama may overlap due to shared linguistic patterns.


---

🚀 Future Improvements

Improve accuracy using Deep Learning (BERT)

Add confidence score for predictions

Improve dataset quality and balancing

Deploy on cloud (Streamlit Cloud / Hugging Face)

Add recommendation system



---

👨‍💻 Author

Developed by Mohith
Engineering Student | Machine Learning Enthusiast


---

📌 Status

Project is actively improving with new features and model enhancements.


---

⭐ Note

If you like this project, consider giving it a ⭐ on GitHub.


---

🚀 Stay Connected

Stay tuned for more Machine Learning and AI projects.


