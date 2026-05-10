# 🪷 Mudra NLP – Bharatanatyam Mudra Predictor

## 📌 Overview
Mudra NLP is an **NLP-based multilingual Bharatanatyam Mudra Prediction System** that helps users identify Bharatanatyam mudras from textual descriptions of hand gestures. The system supports **multiple languages** such as **English, Kannada, Hindi, and Tamil**, making Bharatanatyam learning more accessible to beginners.

The project uses **Natural Language Processing (NLP)** techniques to process user input, predict the correct mudra, and display its **meaning, type, and image** through an interactive interface.

---

## 🎯 Problem Statement
Learning Bharatanatyam mudras is difficult for beginners because:

- Understanding mudras requires both **theoretical and visual knowledge**
- Most learning resources are available only in **English**
- Regional language learners face **language barriers**
- There is no simple system to identify mudras from **text descriptions in multiple languages**

This project solves these challenges using **NLP + Machine Learning + Translation**.

---

## ✨ Features
✅ Multilingual Input Support (English, Kannada, Hindi, Tamil)  
✅ NLP-Based Mudra Prediction  
✅ TF-IDF Text Feature Extraction  
✅ Logistic Regression Classification  
✅ Mudra Meaning & Type Display  
✅ Mudra Image Visualization  
✅ Beginner-Friendly Bharatanatyam Learning Support  
✅ Interactive Streamlit UI  

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Streamlit | Frontend UI Development |
| scikit-learn | Machine Learning |
| TF-IDF | Text Feature Extraction |
| Logistic Regression | Mudra Classification |
| deep_translator | Multilingual Translation |
| Pandas | Dataset Handling |

---

## ⚙️ Working Principle

1. User enters a **mudra description** in any supported language  
2. The system translates the input into **English**  
3. **TF-IDF** converts text into numerical features  
4. **Logistic Regression** predicts the correct mudra  
5. The system displays:
   - Predicted Mudra Name
   - Mudra Type
   - Meaning
   - Image

---

## 🧠 NLP Components Used

### TF-IDF (Term Frequency – Inverse Document Frequency)
Used to convert text descriptions into numerical vectors for machine learning.

### Logistic Regression
Used as the classification algorithm to predict the correct Bharatanatyam mudra.

---

## 📂 Project Structure

```text
mudra_nlp_streamlit/
│── app.py
│── model.py
│── dataset.csv
│── images/
│   ├── Pataka.jpg
│   ├── Tripataka.jpg
│   ├── Mushti.jpg
│   └── ...
│── requirements.txt
│── README.md
```

---

## 🚀 Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/mudra-nlp.git
```

### 2️⃣ Navigate to Project Folder
```bash
cd mudra-nlp
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

---

## 🧪 Sample Inputs

### English
```text
Ring finger bent
```

### Kannada
```text
ಉಂಗುರ ಬೆರಳು ಮಡಚಿದೆ
```

### Hindi
```text
अनामिका उंगली मुड़ी हुई है
```

### Tamil
```text
மோதிர விரல் மடக்கப்பட்டுள்ளது
```

---

## 🎭 Supported Mudras
### Asamyutha Hastas
- Pataka
- Tripataka
- Ardhapataka
- Kartarimukha
- Mayura
- Ardhachandra
- Arala
- Shukatunda
- Mushti
- Shikhara
- Hamsasya
- Suchi
- Chandrakala
- Alapadma

### Samyutha Hastas
- Anjali
- Kapota
- Karkata
- Swastika
- Dola
- Pushpaputa
- Utsanga
- Shivalinga
- Katakavardhana
- Garuda
- Nagabandha
- Matsya
- Kurma
- Varaha

---

## 🌍 Applications
- Bharatanatyam Learning Platforms
- Dance Academies
- AI-Based Educational Tools
- Cultural Heritage Preservation
- Smart E-Learning Applications

---

## 🌱 Sustainable Development Goals (SDGs)

### 🎓 SDG 4 – Quality Education
Supports accessible and multilingual dance learning.

### 🏛 SDG 11 – Sustainable Cities & Communities
Helps preserve Indian classical cultural heritage.

### 🤝 SDG 10 – Reduced Inequalities
Breaks language barriers in education.

---

## 🔮 Future Enhancements
- Real-time webcam-based mudra recognition
- Voice-based input support
- More Bharatanatyam mudras
- Mobile application development
- Deep learning-based classification

---

## 👩‍💻 Developed By
**Dhanyashree K.S.**  
Bharatanatyam Enthusiast | Engineering Student | NLP Project Developer

---

## 📜 License
This project is developed for educational and research purposes.
