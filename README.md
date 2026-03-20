# 🛡️ Phishing Website Detector

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100-green?style=for-the-badge&logo=fastapi)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange?style=for-the-badge)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-darkgreen?style=for-the-badge&logo=mongodb)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker)

> An intelligent Machine Learning based web application that detects *Phishing Websites* in real-time using 35 advanced features.

---

## 🚀 Live Demo


http://127.0.0.1:8000


---

## 📌 Features

- 🤖 *ML Model* - XGBoost classifier trained on real phishing data
- 🌐 *REST API* - FastAPI backend with /predict endpoint
- 🎨 *Modern UI* - Beautiful responsive frontend
- 🗄️ *MongoDB* - Stores all prediction history
- 🐳 *Docker* - Fully containerized application
- ⚙️ *CI/CD* - Automated pipeline with GitHub Actions
- 📊 *35 Features* - URL, Domain, Content analysis

---

## 🧠 How It Works


User Input (35 features)
        ↓
   FastAPI Backend
        ↓
  XGBoost ML Model
        ↓
  Phishing / Legitimate
        ↓
   Saved to MongoDB


---

## 📁 Project Structure


Phishing_classifier/
├── 📂 data/
│   ├── phishing_eda.csv
│   └── phishing_featured.csv
├── 📂 models/
│   ├── pipeline.pkl
│   └── phishing_model.pkl
├── 📂 templates/
│   └── index.html
├── 📂 .github/workflows/
│   └── deploy.yml
├── 🐍 app.py              # FastAPI main app
├── 📓 Feature_eng.ipynb   # Feature Engineering
├── 📓 Model_training.ipynb # Model Training
├── 📓 Pipeline.ipynb      # ML Pipeline
├── 🐳 Dockerfile
└── 📄 requirements.txt


---

## 🔍 35 Features Used

| Category | Features |
|----------|----------|
| *URL Based* | having_IP_Address, URL_Length, Shortining_Service, having_At_Symbol, double_slash_redirecting, Prefix_Suffix |
| *Domain Based* | having_Sub_Domain, SSLfinal_State, Domain_registeration_length, DNSRecord, age_of_domain |
| *Page Based* | Favicon, port, HTTPS_token, Request_URL, URL_of_Anchor, Links_in_tags |
| *Content Based* | SFH, Submitting_to_email, Abnormal_URL, Redirect, on_mouseover, RightClick, popUpWidnow, Iframe |
| *Score Based* | URL_Suspicious_Score, Security_Score, Content_Suspicious_Score, Domain_Score, Total_Phishing_Score |

---

## ⚙️ Installation & Setup

### 1. Clone the repository
bash
git clone https://github.com/shrivashadi/Phishing-classifier.git
cd Phishing-classifier


### 2. Create virtual environment
bash
python -m venv myenv
myenv\Scripts\activate  # Windows


### 3. Install dependencies
bash
pip install -r requirements.txt


### 4. Run the application
bash
uvicorn app:app --reload


### 5. Open browser

http://127.0.0.1:8000


---

## 🐳 Docker Setup

bash
docker build -t phishing-classifier .
docker run -p 8000:8000 phishing-classifier


---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home page |
| POST | /predict | Predict phishing or legitimate |
| GET | /history | Get prediction history |

### Example API Call
python
import requests

data = {
    "features": [1, 1, 0, 1, 0, -1, 1, 1, -1, 1, 
                 1, -1, 1, -1, -1, -1, 0, 1, 0, 1,
                 1, 0, 1, -1, -1, 1, 1, 1, 1, 1,
                 1, 1, -1, 1, 1]
}

response = requests.post("http://127.0.0.1:8000/predict", json=data)
print(response.json())  # {"prediction": "Phishing"}


---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Algorithm | XGBoost Classifier |
| Features | 35 |
| Dataset | Phishing Websites Dataset |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.10 | Core Language |
| FastAPI | Backend Framework |
| XGBoost | ML Algorithm |
| Scikit-learn | ML Pipeline |
| Pandas & NumPy | Data Processing |
| MongoDB | Database |
| Docker | Containerization |
| GitHub Actions | CI/CD |

---

## 👨‍💻 Developer

*Aditya Sen*  
🎓 Biotechnology Student | Data Analyst | ML Enthusiast  
📍 GitHub: [@shrivashadi](https://github.com/shrivashadi)

---

## ⭐ Show Your Support

If you found this project helpful, please give it a *⭐ Star* on GitHub!

---

Made with ❤️ by Aditya Sen
